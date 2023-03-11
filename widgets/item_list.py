from PyQt5.QtWidgets import QListWidgetItem


class ItemList(QListWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)

        self._it_id: int = 0

    def set_item_id(self, it_id):
        self._it_id = it_id

    def get_item_id(self) -> int:
        return self._it_id
