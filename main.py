# This Python file uses the following encoding: utf-8
import sys
import os
import time

from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# This loads your .ui file
# so that PyQt can populate your plugin with the elements from Qt Designer
uiPath = os.path.join(os.path.dirname(__file__), 'form.ui')
FORM_CLASS, _ = uic.loadUiType(uiPath)


class MathTextLabel(QtWidgets.QWidget):
  ''' Widget that displays LaTex equations

      Source: https://stackoverflow.com/questions/14097463/displaying-nicely-an-algebraic-expression-in-pyqt '''

  def __init__(self, mathText, parent=None, **kwargs):
    super(QtWidgets.QWidget, self).__init__(parent, **kwargs)

    l = QVBoxLayout(self)
    l.setContentsMargins(0,0,0,0)

    r,g,b,a = self.palette().base().color().getRgbF()

    self._figure = Figure(edgecolor = (r,g,b), facecolor = (r,g,b))
    self._canvas = FigureCanvas(self._figure)
    l.addWidget(self._canvas)
    self._figure.clear()
    text = self._figure.suptitle(
      mathText,
      x = 0.0,
      y = 1.0,
      horizontalalignment = 'left',
      verticalalignment = 'top',
      size = QtGui.QFont().pointSize()*2
    )
    self._canvas.draw()

    (x0, y0),(x1, y1) = text.get_window_extent().get_points()
    w = x1 - x0
    h = y1 - y0

    self._figure.set_size_inches(w/80, h/80)
    self.setFixedSize(w,h)


class FileDialog(QtWidgets.QWidget):
  ''' Open new window to choose / save file(s) from / to filesystem

      Source: https://pythonspot.com/pyqt5-file-dialog/ '''

  def __init__(self):
    # TO DO: Выбор способа работы через аргумент при инициализации
    # экземпляра класса
    super().__init__()
    self.title = 'Select data'
    self.left = 10
    self.top = 10
    self.width = 640
    self.height = 480
    self.initUI()

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    # uncomment other calls to apply different behavior to Dialog
    self.openFileNameDialog()  # choose (open) one file
    # self.openFileNamesDialog()  # choose (open) many files
    # self.saveFileDialog()  # save file

    # TO DO: Проверить нужен ли здесь self.show() вообще
    # self.show()

  def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self,"Select data", "","All Files (*);;Excel Files (*.xlsx)", options=options)
    if fileName:
      print(fileName)
      return fileName

  def openFileNamesDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    files, _ = QFileDialog.getOpenFileNames(self,"Select data", "","All Files (*);;Excel Files (*.xlsx)", options=options)
    if files:
      print(files)
      return files

  def saveFileDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(self,"Select data","","All Files (*);;Excel Files (*.xlsx)", options=options)
    if fileName:
      print(fileName)
      return filename


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
