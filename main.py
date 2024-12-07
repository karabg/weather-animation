import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox
from PyQt6.QtGui import QAction  # Update import
from PyQt6.QtCore import QTimer, QPoint
from PyQt6.QtGui import QPainter, QColor

class AnimationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Animation")
        self.setGeometry(100, 100, 800, 600)

        # Initialize variables for animation
        self.snowflakes = []
        self.raindrops = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.animation_type = None

        # Create menu
        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()

        # About menu
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        about_menu = menu_bar.addMenu("About")
        about_menu.addAction(about_action)

        # Animation menu
        animation_menu = menu_bar.addMenu("Weather")
        snow_action = QAction("Snow", self)
        snow_action.triggered.connect(self.start_snowing)
        rain_action = QAction("Rain", self)
        rain_action.triggered.connect(self.start_raining)

        animation_menu.addAction(snow_action)
        animation_menu.addAction(rain_action)

    def show_about(self):
        QMessageBox.information(self, "About", "This project demonstrates weather animations with PyQt.")

    def start_snowing(self):
        self.animation_type = "snow"
        self.snowflakes = [QPoint(random.randint(0, self.width()), random.randint(0, self.height())) for _ in range(100)]
        self.timer.start(50)

    def start_raining(self):
        self.animation_type = "rain"
        self.raindrops = [QPoint(random.randint(0, self.width()), random.randint(0, self.height())) for _ in range(100)]
        self.timer.start(50)

    def update_animation(self):
        if self.animation_type == "snow":
            for i in range(len(self.snowflakes)):
                self.snowflakes[i].setY(self.snowflakes[i].y() + 2)
                if self.snowflakes[i].y() > self.height():
                    self.snowflakes[i].setY(0)
                    self.snowflakes[i].setX(random.randint(0, self.width()))
        elif self.animation_type == "rain":
            for i in range(len(self.raindrops)):
                self.raindrops[i].setY(self.raindrops[i].y() + 5)
                if self.raindrops[i].y() > self.height():
                    self.raindrops[i].setY(0)
                    self.raindrops[i].setX(random.randint(0, self.width()))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.animation_type == "snow":
            painter.setBrush(QColor("white"))
            for flake in self.snowflakes:
                painter.drawEllipse(flake, 5, 5)
        elif self.animation_type == "rain":
            painter.setBrush(QColor("blue"))
            for drop in self.raindrops:
                painter.drawRect(drop.x(), drop.y(), 2, 10)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec())
