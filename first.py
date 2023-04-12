from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

app = QApplication([])

window = QMainWindow()
window.resize(500,400)
window.move(300,200)
window.setWindowTitle("Salary total")

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("Please input salay:")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton("total",window)
button.move(380, 80)

window.show()
app.exec_()
