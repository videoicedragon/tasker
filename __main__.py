"""
creates tasks for the user to complete and keeps track of them
"""
from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3
version = "1.0.0"
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(100, 100, 600, 400)
        self.tasks = []
        self.initUI()

    def initUI(self):
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.task_input = QtWidgets.QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.layout.addWidget(self.task_input)

        self.add_task_button = QtWidgets.QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        self.task_list = QtWidgets.QListWidget()
        self.layout.addWidget(self.task_list)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.tasks.append(task_text)
            self.task_list.addItem(task_text)
            self.task_input.clear()
    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.tasks.remove(item.text())
            self.task_list.takeItem(self.task_list.row(item))
        def clear_tasks(self):
            self.tasks.clear()
            self.task_list.clear()



app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()  
