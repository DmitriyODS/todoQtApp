from PyQt5.QtWidgets import QDialog

from ui_base.ui_dialog_reg import Ui_authDialog
from widgets.notifi_dialog import NotifiDialog


def validate(login, password) -> bool:
    return login.strip() != '' and password.strip() != ''


class RegDialog(QDialog, Ui_authDialog):
    def __init__(self, parent, on_login):
        super().__init__(parent)

        self.setupUi(self)
        self.setModal(True)

        self.notifi_form = NotifiDialog(self)
        self.on_login_handler = on_login
        self.loginBtn.clicked.connect(self.on_login)
        self.registerBtn.clicked.connect(self.on_login)

    def incorrect_login_or_password(self):
        self.notifi_form.show_notifi("Не удалось войти",
                                     "Не удалось выполнить вход, неверный логин, или пароль")

    def show_err(self):
        self.notifi_form.show_notifi("Неизвестная ошибка",
                                     "Произошла неизвестная ошибка, попробуйте ещё раз")

    def on_login(self):
        login = self.loginEdit.text()
        password = self.passEdit.text()

        if not validate(login, password):
            self.notifi_form.show_notifi("Не заполнены поля",
                                         "Не все поля корректно заполнены, попробуйте ещё раз")
            return

        self.on_login_handler(login, password, self.sender().objectName())

    def close(self):
        self.loginEdit.setText('')
        self.passEdit.setText('')
        self.loginEdit.setFocus()

        super().close()
