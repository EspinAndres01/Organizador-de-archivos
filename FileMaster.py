import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
from file_organizer import FileOrganizer  # import FileOrganizer class from file_organizer module


class FileOrganizerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('EL ORGANIZADOR ')

        # Create button to select the folder for organizing files
        self.btn_file = QPushButton('Selecciona la carpeta a Ordenar')
        self.btn_file.clicked.connect(self.select_file)

        # Create button to organize files
        self.btn_organize = QPushButton('Organizar')

        # Create label to display selected folder
        self.lbl_file = QLabel('Carpeta: No Seleccionada')

        # Create layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_file)
        vbox.addWidget(self.lbl_file)
        vbox.addWidget(self.btn_organize)

        self.setLayout(vbox)

        # Connect signal to slot
        self.btn_organize.clicked.connect(self.organize_file)

    def select_file(self):
        # Open file dialog to select folder
        file_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lbl_file.setText('Folder: ' + file_path)

    def organize_file(self):
        file_path = self.lbl_file.text()[8:]

        file_organizer = FileOrganizer(file_path, file_path)
        file_organizer.organize_file()

app = QApplication(sys.argv)

gui = FileOrganizerGUI()
gui.show()

sys.exit(app.exec_())
