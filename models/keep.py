import datetime
from dataclasses import dataclass


@dataclass
class Keep:
    id: int = 0
    title: str = ''
    text: str = ''
    user_id: int = 0
    date_create: datetime.datetime = datetime.datetime.now()

    def __str__(self):
        return f"id={self.id}\ntitle={self.title}\ntext={self.text}\nuser_id={self.user_id}"

    def __repr__(self):
        return self.__str__()

    def select_placeholder(self, *args) -> bool:
        if len(args) < 5:
            return False

        self.id = args[0]
        self.title = args[1]
        self.text = args[2]
        self.user_id = args[3]
        self.date_create = datetime.datetime.fromtimestamp(args[4])

        return True

    def insert_placeholder(self) -> tuple:
        return self.title, self.text, self.user_id

    def update_placeholder(self) -> tuple:
        return self.title, self.text, self.id

    def date_create_str(self) -> str:
        return self.date_create.strftime("%d-%m-%Y %H:%M")

    def date_create_timestamp(self) -> int:
        return self.date_create.timetuple()
