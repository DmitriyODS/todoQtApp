import datetime
from dataclasses import dataclass


@dataclass
class User:
    id: int = 0
    login: str = ''
    password: str = ''
    is_admin: bool = False
    date_create: datetime.datetime = datetime.datetime.now()

    def __str__(self):
        return f"id={self.id}\nlogin={self.login}\nis_admin={self.is_admin}"

    def __repr__(self):
        return self.__str__()

    def select_placeholder(self, *args) -> bool:
        if len(args) < 4:
            return False

        self.id = args[0]
        self.login = args[1]
        self.is_admin = bool(args[2])
        self.date_create = datetime.datetime.fromtimestamp(args[3])

        return True

    def insert_placeholder(self) -> tuple:
        return self.login, self.password

    def auth_placeholder(self) -> tuple:
        return self.insert_placeholder()

    def date_create_str(self) -> str:
        return self.date_create.strftime("%d-%m-%Y %H:%M")

    def date_create_timestamp(self) -> int:
        return self.date_create.timetuple()
