from PyQt5.QtWidgets import QApplication

from app.app import App
from store.store import Store
from widgets.main_window import MainWindow


def main():
    store = Store("./store/db")
    app = App(store)
    q_app = QApplication([])

    window = MainWindow(app)
    window.run()

    q_app.exec()


if __name__ == "__main__":
    main()
