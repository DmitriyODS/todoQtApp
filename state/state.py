from models.keep import Keep
from models.user import User

SECTION_KEEPS = 1
SECTION_USERS = 2


class State:
    def __init__(self):
        self.cur_user: User | None = None
        self.cur_section: int = SECTION_KEEPS
        self.select_user: User | None = None
        self.select_keep: Keep | None = None
