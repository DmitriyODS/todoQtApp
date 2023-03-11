BEGIN;

CREATE TABLE IF NOT EXISTS users
(
    id          INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
    login       TEXT UNIQUE NOT NULL,
    password    TEXT        NOT NULL,
    is_admin    INTEGER     NOT NULL DEFAULT 0 CHECK ( is_admin >= 0 AND is_admin < 2 ),
    date_create INTEGER     NOT NULL DEFAULT (strftime('%s', 'now'))
);

INSERT INTO users(id, login, password, is_admin)
VALUES (1, 'admin', 'admin', 1)
ON CONFLICT (id) DO UPDATE SET id=excluded.id,
                               login=excluded.login,
                               password=excluded.password,
                               is_admin=excluded.is_admin;

UPDATE sqlite_sequence
SET seq = (SELECT MAX(id) FROM users)
WHERE name = 'users';

CREATE TABLE IF NOT EXISTS keeps
(
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    text        TEXT    NOT NULL DEFAULT '',
    user_id     INTEGER NOT NULL,
    date_create INTEGER NOT NULL DEFAULT (strftime('%s', 'now')),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT;