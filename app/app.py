from models.keep import Keep
from models.user import User
from state.state import State, SECTION_USERS, SECTION_KEEPS
from store.store import Store


class App:
    def __init__(self, store: Store):
        self._store = store
        self._state = State()

    def is_login(self) -> bool:
        return self._state.cur_user is not None

    def login(self, login, password) -> bool:
        cur_user = User(login=login, password=password)
        cur_user = self._store.get_user_by_name_pass(cur_user)

        if cur_user.id:
            self._state.cur_user = cur_user
            return True
        return False

    def register(self, login, password) -> bool:
        cur_user = User(login=login, password=password)
        cur_user.id = self._store.add_user(cur_user)

        if cur_user.id:
            self._state.cur_user = cur_user
            return True
        return False

    def get_login_cur_user(self) -> str:
        if self._state.cur_user is None:
            return ''
        return self._state.cur_user.login

    def get_id_cur_user(self) -> int:
        if self._state.cur_user is None:
            return 0
        return self._state.cur_user.id

    def logout(self):
        self._state.cur_user = None

    def login_is_admin(self) -> bool:
        if self._state.cur_user is None:
            return False
        return self._state.cur_user.is_admin

    def get_cur_section(self) -> int:
        return self._state.cur_section

    def set_cur_section(self, section: int):
        self._state.cur_section = section
        self._state.select_keep = None
        self._state.select_user = None

    def save_keep(self, title, text) -> int:
        if self._state.cur_user is None:
            return 0

        cur_keep = Keep(title=title, text=text, user_id=self._state.cur_user.id)
        if self._state.select_keep is None:
            return self._store.add_keep(cur_keep)

        cur_keep.id = self._state.select_keep.id
        return self._store.update_keep_by_id(cur_keep)

    def get_select_keep(self) -> Keep | None:
        return self._state.select_keep

    def get_select_user(self) -> User | None:
        return self._state.select_user

    def set_select_item(self, it_id: int) -> bool:
        if self._state.cur_section == SECTION_USERS:
            self._state.select_user = self._store.get_user_by_id(it_id)
            if self._state.select_user.id == 0:
                return False
        elif self._state.cur_section == SECTION_KEEPS:
            self._state.select_keep = self._store.get_keep_by_id(it_id)
            if self._state.select_keep.id == 0:
                return False

        return True

    def clear_selection(self):
        self._state.select_user = None
        self._state.select_keep = None

    def delete_item(self) -> bool:
        if self._state.cur_section == SECTION_USERS:
            if self._state.select_user is not None:
                return self._store.del_user_by_id(self._state.select_user.id)
        elif self._state.cur_section == SECTION_KEEPS:
            if self._state.select_keep is not None:
                return self._store.del_keep_by_id(self._state.select_keep.id)

        return False

    def get_keeps_list(self) -> list[Keep]:
        if self._state.cur_user is None:
            return list()

        return self._store.get_keeps(self._state.cur_user.id)

    def get_users_list(self) -> list[User]:
        return self._store.get_users()
