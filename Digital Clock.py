import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(600, 300, 700, 250)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignVCenter)

        self.time_label.setStyleSheet("""
                    font-size: 150px;
                    font-weight: bold;
                    color: white;
                    background: transparent;
                """)

        self.setStyleSheet("""
                    background: qlineargradient(
                        spread:pad, x1:0, y1:0, x2:1, y2:1,
                        stop:0 #0e001a,
                        stop:0.3 #220044,
                        stop:0.6 #cc3b3f,
                        stop:1 #cc7700
                    );
                """)

        font_id= QFontDatabase.addApplicationFont("D:\PyCharmProjects\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
