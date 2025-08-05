import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.helloList = [
            "Hallo Welt",
            "Hei maailma",
            "Hola Mundo",
            "Привет мир",
            "Hello World!",
        ]

        self.setWindowTitle("My app")

        self.pushButton = QtWidgets.QPushButton("Click Me...")
        self.textLabel = QtWidgets.QLabel(
            "Hello World!", alignment=QtCore.Qt.AlignCenter
        )

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.textLabel)
        self.layout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.textLabel.setText(random.choice(self.helloList))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
