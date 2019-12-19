# This Python file uses the following encoding: utf-8
import sys
import os
import time

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

# This loads your .ui file
# so that PyQt can populate your plugin with the elements from Qt Designer
uiPath = os.path.join(os.path.dirname(__file__), 'form.ui')
FORM_CLASS, _ = uic.loadUiType(uiPath)


class MainDialog(QtWidgets.QDialog, FORM_CLASS):
  def __init__(self, parent=None):
    """Constructor."""
    super(MainDialog, self).__init__(parent)
    # Set up the user interface from Designer through FORM_CLASS.
    # After self.setupUi() you can access any designer object by doing
    # self.<objectname>, and you can use autoconnect slots - see
    # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
    # #widgets-and-dialogs-with-auto-connect
    self.ui = self.setupUi(self)


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    self.setWindowTitle("My Awesome App")
    self.dialog = MainDialog(parent=self)
    self.dialog.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec_()
