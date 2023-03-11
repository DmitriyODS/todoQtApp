from PyQt5.QtWidgets import QDialog

from ui_base.ui_dialog_notifi import Ui_notifiDialog


class NotifiDialog(QDialog, Ui_notifiDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)
        self.okBtn.clicked.connect(self.close_notifi)

    def show_notifi(self, title, text):
        self.setWindowTitle(title)
        self.textNotifiTextBrowser.setText(text)
        self.show()

    def close_notifi(self):
        self.close()
