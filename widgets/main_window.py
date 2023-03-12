from PyQt5.QtWidgets import QWidget, QListWidgetItem

from app.app import App
from state.state import SECTION_KEEPS, SECTION_USERS
from ui_base.ui_main_window import Ui_keepMain
from widgets.edit_dialog import EditDialog
from widgets.item_list import ItemList
from widgets.item_view import ItemView
from widgets.notifi_dialog import NotifiDialog
from widgets.reg_dialog import RegDialog


class MainWindow(QWidget, Ui_keepMain):
    def __init__(self, app: App):
        super().__init__()

        self.app = app
        self.setupUi(self)

        self.reg_dialog = RegDialog(self, self.on_login)
        self.edit_dialog = EditDialog(self, self.on_save)
        self.notifi_dialog = NotifiDialog(self)

        self.logoutBtn.clicked.connect(self.on_logout)
        self.keepsBtn.clicked.connect(self.on_select_keeps_section)
        self.usersBtn.clicked.connect(self.on_select_users_section)
        self.addBtn.clicked.connect(self.on_add_keep)
        self.delBtn.clicked.connect(self.on_delete)
        self.editBtn.clicked.connect(self.on_edit_keep)

        self.itemsListWidget.itemSelectionChanged.connect(self.on_select)

    def on_select(self):
        selections = self.itemsListWidget.selectedItems()
        if len(selections) > 0:
            res = self.app.set_select_item(selections[0].get_item_id())
            if res:
                self.update_info_selection_item()
            else:
                self.notifi_dialog.show_notifi("Ошибка", "Выбранный элемент не найден")
                self.update_list_view()

    def set_info_view(self, title, date, text):
        self.itemTitleLabel.setText(title)
        self.itemTextBrowser.setText(text)
        self.itemDateCreateLabel.setText(date)

    def update_info_selection_item(self):
        cur_section = self.app.get_cur_section()
        if cur_section == SECTION_KEEPS:
            cur_keep = self.app.get_select_keep()
            if cur_keep is not None:
                self.set_info_view(cur_keep.title, cur_keep.date_create_str(), cur_keep.text)
                return
        elif cur_section == SECTION_USERS:
            cur_user = self.app.get_select_user()
            if cur_user is not None:
                self.set_info_view(cur_user.login, cur_user.date_create_str(), 'Пользователь системы')
                return

        self.set_info_view("Элемент не выбран", '', '')

    def update_list_view_users(self):
        items = self.app.get_users_list()
        user_id = self.app.get_id_cur_user()
        for it in items:
            if user_id == it.id:
                continue

            item_view = ItemView()
            item_view.set_data(it.login)

            q_list_item = ItemList(self.itemsListWidget)
            q_list_item.setSizeHint(item_view.sizeHint())
            q_list_item.set_item_id(it.id)

            self.itemsListWidget.addItem(q_list_item)
            self.itemsListWidget.setItemWidget(q_list_item, item_view)

    def update_list_view_keeps(self):
        items = self.app.get_keeps_list()
        for it in items:
            item_view = ItemView()
            item_view.set_data(it.title)

            q_list_item = ItemList(self.itemsListWidget)
            q_list_item.setSizeHint(item_view.sizeHint())
            q_list_item.set_item_id(it.id)

            self.itemsListWidget.addItem(q_list_item)
            self.itemsListWidget.setItemWidget(q_list_item, item_view)

    def clear_selection(self):
        self.itemsListWidget.clearSelection()
        self.app.clear_selection()

    def update_list_view(self):
        cur_section = self.app.get_cur_section()
        self.clear_selection()
        self.itemsListWidget.clear()
        self.update_info_selection_item()
        if cur_section == SECTION_KEEPS:
            self.update_list_view_keeps()
        elif cur_section == SECTION_USERS:
            self.update_list_view_users()

    def on_save(self, title, text):
        if not self.app.save_keep(title, text):
            self.edit_dialog.show_err("Ошибка создания", "Не удалось создать заметку, попробуйте ещё раз")
        else:
            self.edit_dialog.close()

        self.update_list_view()

    def on_add_keep(self):
        self.clear_selection()
        self.edit_dialog.show_create()

    def on_edit_keep(self):
        select_keep = self.app.get_select_keep()
        if select_keep is None:
            self.notifi_dialog.show_notifi("Элемент не выбран", "Выберите элемент для изменения")
            return

        self.edit_dialog.show_edit(select_keep.title, select_keep.text)

    def on_delete(self):
        select_keep = self.app.get_select_keep() or self.app.get_select_user()
        if select_keep is None:
            self.notifi_dialog.show_notifi("Элемент не выбран", "Выберите элемент для удаления")
            return

        if not self.app.delete_item():
            self.notifi_dialog.show_notifi("Ошибка удаления!",
                                           "Произошла ошибка уделения записи, попробуйте ещё раз позже")
        self.update_list_view()

    def on_login(self, login, password, type_action):
        res: bool = False

        if type_action == self.reg_dialog.loginBtn.objectName():
            res = self.app.login(login, password)
        elif type_action == self.reg_dialog.registerBtn.objectName():
            res = self.app.register(login, password)

        if res:
            self.reg_dialog.close()
            self.show_main_window()
        else:
            self.reg_dialog.incorrect_login_or_password()

    def on_logout(self):
        self.app.logout()
        self.close()

        self.reg_dialog.show()

    def show_main_window(self):
        self.loginLabel.setText(self.app.get_login_cur_user())

        if self.app.login_is_admin():
            self.usersBtn.show()
        else:
            self.usersBtn.hide()

        self.on_select_keeps_section()
        self.update_list_view()

        self.show()

    def on_select_keeps_section(self):
        self.app.set_cur_section(SECTION_KEEPS)
        self.on_cur_section()

    def on_select_users_section(self):
        self.app.set_cur_section(SECTION_USERS)
        self.on_cur_section()

    def on_cur_section(self):
        cur_section = self.app.get_cur_section()
        if cur_section == SECTION_KEEPS:
            self.mainTitleLabel.setText("Мои заметки")
            self.editBtn.show()
            self.keepsBtn.setDisabled(True)
            self.usersBtn.setDisabled(False)
            self.addBtn.show()
        elif cur_section == SECTION_USERS:
            self.mainTitleLabel.setText("Пользователи")
            self.editBtn.close()
            self.keepsBtn.setDisabled(False)
            self.usersBtn.setDisabled(True)
            self.addBtn.close()
        else:
            self.mainTitleLabel.setText("Неизвестная секция")
            self.editBtn.show()
            self.addBtn.show()
            self.keepsBtn.setDisabled(True)
            self.usersBtn.setDisabled(True)
        self.update_list_view()

    def run(self):
        if self.app.is_login():
            self.show()
        else:
            self.reg_dialog.show()
