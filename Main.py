import sys
from PyQt5.QtWidgets import QApplication
from vol_trap_form import VolTrapForm

#This is the entry point of the program. It creates the QApplication, creates and shows the form, and starts the event loop.
#The if __name__ == '__main__': block ensures this only runs if the script is executed directly (not imported).


def main():
    app = QApplication(sys.argv)
    form = VolTrapForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
