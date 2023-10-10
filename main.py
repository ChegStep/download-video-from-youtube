from des1 import *
import os
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from qyoutubedl import QLogger, QHook, QYoutubeDL

class gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #actions
        self.download_folder = None
        self.ui.btn_dwld.clicked.connect(self.download)
        self.ui.btnPathFile.clicked.connect(self.get_folder)
        self.ui.progressBar.hide()
        self.ui.plainEdit.hide()

        self.ytdl = QYoutubeDL()

    def download(self):
        if not self.ui.pathFile.text():
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Вы не выбрали папку!")
            return
        if len(self.ui.pathVideo.text()) < 10:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Ссылка на видео указана неправильно!")
            return

        qhook = QHook()
        qlogger = QLogger()
        url = self.ui.pathVideo.text()

        options = {
            "format": "bestvideo/best",
            "noplaylist": True,
            "noprogress": True,
            "logger": qlogger,
            "progress_hooks": [qhook],
        }
        self.ytdl.download([url], options)
        qhook.infoChanged.connect(self.handle_info_changed)
        qlogger.messageChanged.connect(self.ui.plainEdit.appendPlainText)

        self.ui.progressBar.setRange(0, 1)

    def handle_info_changed(self, d):
        print(d["status"])
        if d["status"] == "downloading":
            self.ui.progressBar.show()
            total = d["total_bytes"]
            downloaded = d["downloaded_bytes"]
            self.ui.progressBar.setMaximum(total)
            self.ui.progressBar.setValue(downloaded)
        if d["status"] == "finished":
            QtWidgets.QMessageBox.information(self, "Готово!", "Загрузка завершена")

    def get_folder(self):
        try:
            self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выбрать папку')
            os.chdir(self.download_folder)
            self.ui.pathFile.setText(os.getcwd())
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Вы не выбрали папку!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())
    win = gui()
    win.show()
    sys.exit(app.exec())

