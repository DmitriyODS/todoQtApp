from PyQt5.QtWidgets import QDialog

from ui_base.ui_dialog_edit import Ui_editDialog
from widgets.notifi_dialog import NotifiDialog


def validate(title) -> bool:
    return title.strip() != ''


class EditDialog(QDialog, Ui_editDialog):
    def __init__(self, parent, on_save):
        super().__init__(parent)

        self.setupUi(self)
        self.setModal(True)
        self.on_save_handler = on_save
        self.saveBtn.clicked.connect(self.on_save)
        self.cancelBtn.clicked.connect(self.close)

        self.notifi_dialog = NotifiDialog(self)

    def on_save(self):
        title = self.titleTextEdit.text()
        text = self.textTextEdit.toPlainText()

        if validate(title):
            self.on_save_handler(title, text)
        else:
            self.show_err("Ошибка формы", "Заголовок не может быть пустым, попробуйте ещё раз")

    def show_err(self, title, text):
        self.notifi_dialog.show_notifi(title, text)

    def show_create(self):
        self.setWindowTitle("Создать")
        self.titleLabel.setText("Создать заметку")
        self.show()

    def show_edit(self, title: str, text: str):
        self.setWindowTitle("Изменить")
        self.titleLabel.setText("Изменить заметку")
        self.titleTextEdit.setText(title)
        self.textTextEdit.setText(text)
        self.show()

    def close(self):
        self.titleTextEdit.setText('')
        self.textTextEdit.setText('')
        super().close()
