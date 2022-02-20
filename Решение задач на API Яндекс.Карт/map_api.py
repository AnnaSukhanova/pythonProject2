import os
import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map_api.ui', self)
        self.x, self.y, self.m, self.l = '37.530887', '55.70311', '0.002', 'map'
        self.image.installEventFilter(self)
        self.getImage()
        self.initUI()

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.x},{self.y}&spn={self.m},{self.m}&l={self.l}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if float(self.m) + 0.01 >= 17:
                print('предел')
            else:
                self.m = float(self.m) + 0.01
                self.initUI()

        if event.key() == Qt.Key_PageDown:
            if float(self.m) - 0.01 < 0:
                print('предел')
            else:
                self.m = float(self.m) - 0.01
                self.initUI()

    def initUI(self):
        self.getImage()
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
