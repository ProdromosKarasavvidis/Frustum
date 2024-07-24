from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from vol_trap import VolTrap

#This defines the VolTrapForm class, which inherits from QWidget.
#The constructor calls the parent constructor and then calls initUI to set up the user interface.

class VolTrapForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #This method sets up the user interface. It creates labels, input fields, a button, and a label for the result.    

    def initUI(self):
        self.setWindowTitle('Volume of Truncated Pyramid Calculator')
        
        self.label_E = QLabel('Area 1 (E) m²:')
        self.input_E = QLineEdit()
        self.label_e = QLabel('Area 2 (e) m²:')
        self.input_e = QLineEdit()
        self.label_u = QLabel('Height (h) m:')
        self.input_u = QLineEdit()
        self.calc_button = QPushButton('Calculate Volume')
        self.result_label = QLabel('Volume: ')

        # Create and set up the image
        self.image_label = QLabel(self)
        pixmap = QPixmap('Pyr.png')  # Replace with your actual filename
        scaled_pixmap = pixmap.scaled(250, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # Create layout
        #This sets up the layout of the widgets. It creates a vertical layout (vbox)
        #and adds horizontal layouts (hbox) for each label-input pair. 
        #Then it adds the button and result label to the vertical layout.

        vbox = QVBoxLayout()
        vbox.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        vbox.addWidget(self.image_label)
        vbox.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        for label, input_field in [(self.label_E, self.input_E), 
                                   (self.label_e, self.input_e), 
                                   (self.label_u, self.input_u)]:
            hbox = QHBoxLayout()
            hbox.addWidget(label)
            hbox.addWidget(input_field)
            vbox.addLayout(hbox)
        
        vbox.addWidget(self.calc_button)
        vbox.addWidget(self.result_label)
        self.setLayout(vbox)

        # Connect the button to the calculation function
        #This connects the button's click event to the calculate_volume method.

        self.calc_button.clicked.connect(self.calculate_volume)


    #This method is called when the button is clicked. It tries to convert the input to floats, creates a VolTrap object, 
    #calculates the volume, and displays the result.
    #If there's an error (e.g., non-numeric input), it displays an error message.
        
    def calculate_volume(self):
        try:
            E = float(self.input_E.text())
            e = float(self.input_e.text())
            u = float(self.input_u.text())
            vol_trap = VolTrap(E, e, u)
            volume = vol_trap.calcVol()
            self.result_label.setText(f'Volume: {volume} m³')
        except ValueError:
            self.result_label.setText('Please enter valid numbers')
