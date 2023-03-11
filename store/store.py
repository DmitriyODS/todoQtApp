import sqlite3

from models.keep import Keep
from models.user import User

INSERT_USER = """
INSERT INTO users (login, password)
VALUES (?, ?)
RETURNING id;
"""

INSERT_KEEP = """
INSERT INTO keeps (title, text, user_id)
VALUES (?, ?, ?)
RETURNING id;
"""

UPDATE_KEEP_BY_ID = """
UPDATE keeps
SET title = ?,
    text = ?
WHERE id = ?;
"""

DELETE_USER_BY_ID = """
DELETE
FROM users
WHERE id = ?;
"""

DELETE_KEEP_BY_ID = """
DELETE
FROM keeps
WHERE id = ?;
"""

SELECT_USER_BY_NAME_PASS = """
SELECT id,
       login,
       is_admin,
       date_create
FROM users
WHERE login = ?
  AND password = ?;
"""

SELECT_USER_BY_ID = """
SELECT id,
       login,
       is_admin,
       date_create
FROM users
WHERE id = ?;
"""

SELECT_KEEP_BY_ID = """
SELECT id,
       title,
       text,
       user_id,
       date_create
FROM keeps
WHERE id = ?;
"""

SELECT_USERS = """
SELECT id,
       login,
       is_admin,
       date_create
FROM users
ORDER BY date_create DESC;
"""

SELECT_KEEPS = """
SELECT id,
       title,
       text,
       user_id,
       date_create
FROM keeps
WHERE user_id = ?
ORDER BY date_create DESC;
"""

FOREIGN_ON = """
PRAGMA foreign_keys = ON;
"""


class Store:
    db = None

    def __new__(cls, *args, **kwargs):
        if cls.db is None:
            cls.db = super().__new__(cls)
        return cls.db

    def __init__(self, path_db: str):
        self._connect = sqlite3.connect(path_db)
        self._connect.row_factory = sqlite3.Row
        self._init_db()
        self._connect.execute(FOREIGN_ON)

    def _init_db(self):
        with open("./store/init_db.sql") as sql_script:
            self._connect.executescript(sql_script.read())

    def add_user(self, user: User) -> int:
        try:
            with self._connect:
                cur = self._connect.execute(INSERT_USER, user.insert_placeholder())
                data: sqlite3.Row = cur.fetchone()
                if data is None:
                    return 0
                return data[0]
        except sqlite3.Error as err:
            print(err)
            return 0

    def add_keep(self, keep: Keep) -> int:
        try:
            with self._connect:
                cur = self._connect.execute(INSERT_KEEP, keep.insert_placeholder())
                data: sqlite3.Row = cur.fetchone()
                if data is None:
                    return 0
                return data[0]
        except sqlite3.Error as err:
            print(err)
            return 0

    def update_keep_by_id(self, keep: Keep) -> bool:
        try:
            with self._connect:
                self._connect.execute(UPDATE_KEEP_BY_ID, keep.update_placeholder())
        except sqlite3.Error as err:
            print(err)
            return False
        return True

    def del_user_by_id(self, user_id: int) -> bool:
        try:
            with self._connect:
                self._connect.execute(DELETE_USER_BY_ID, (user_id,))
        except sqlite3.Error as err:
            print(err)
            return False
        return True

    def del_keep_by_id(self, keep_id: int) -> bool:
        try:
            with self._connect:
                self._connect.execute(DELETE_KEEP_BY_ID, (keep_id,))
        except sqlite3.Error as err:
            print(err)
            return False
        return True

    def get_user_by_name_pass(self, user: User) -> User:
        try:
            with self._connect:
                cur = self._connect.execute(SELECT_USER_BY_NAME_PASS, user.auth_placeholder())
                data: sqlite3.Row = cur.fetchone()
                if data is None:
                    return user
                user.select_placeholder(*data)
        except sqlite3.Error as err:
            print(err)
        return user

    def get_user_by_id(self, user_id: int) -> User:
        user: User = User()

        try:
            with self._connect:
                cur = self._connect.execute(SELECT_USER_BY_ID, (user_id,))
                data: sqlite3.Row = cur.fetchone()
                if data is None:
                    return user
                user.select_placeholder(*data)
        except sqlite3.Error as err:
            print(err)
        return user

    def get_keep_by_id(self, keep_id: int) -> Keep:
        keep: Keep = Keep()

        try:
            with self._connect:
                cur = self._connect.execute(SELECT_KEEP_BY_ID, (keep_id,))
                data: sqlite3.Row = cur.fetchone()
                if data is None:
                    return keep
                keep.select_placeholder(*data)
        except sqlite3.Error as err:
            print(err)
        return keep

    def get_users(self) -> list[User]:
        users_lst: list[User] = list()

        try:
            with self._connect:
                cur = self._connect.execute(SELECT_USERS)
                for item in cur:
                    user = User()
                    user.select_placeholder(*item)
                    users_lst.append(user)
        except sqlite3.Error as err:
            print(err)
        return users_lst

    def get_keeps(self, user_id: int) -> list[Keep]:
        keeps_lst: list[Keep] = list()

        try:
            with self._connect:
                cur = self._connect.execute(SELECT_KEEPS, (user_id,))
                for item in cur:
                    keep = Keep()
                    keep.select_placeholder(*item)
                    keeps_lst.append(keep)
        except sqlite3.Error as err:
            print(err)
        return keeps_lst

    def __del__(self):
        self._connect.close()
