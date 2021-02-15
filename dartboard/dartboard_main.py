###################
# The entry point for our dartboard
# application. This should kick off all
# of the main processes of our application.
###################
from backend import django_setup
from Hub import Hub
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import Qt
import sys

# Note: this is used to make our workflows actually grab all the classes
# Some classes may not be directly called by our code and adding those
# to the extra_imports file allows those to be picked up by the installer
import extra_imports

# Opens a DartboardView window
# This should be the last thing executed here or should
# be moved to execute on it's own thread




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = Hub()

    sys.exit(app.exec_())
