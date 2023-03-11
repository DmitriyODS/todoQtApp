from PyQt5.QtWidgets import QWidget

from ui_base.ui_item_list import Ui_ItemList


class ItemView(QWidget, Ui_ItemList):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def set_data(self, text: str):
        self.titleItem.setText(text)
