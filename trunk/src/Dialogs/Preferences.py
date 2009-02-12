from PyQt4 import QtGui
from PyQt4 import QtCore
from Dialogs.ui_Preferences import Ui_PrefWindow
import time
import threading
from Settings import Settings

class Preferences(QtGui.QDialog, Ui_PrefWindow):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.settings = Settings()
		
		self.txtHitMissesColor.setText(self.settings.settings.config['Graphs']['HitMiss'])
		self.txtGetsSetsColor.setText(self.settings.settings.config['Graphs']['GetSet'])
		
		tmpText = ''
		for colors in self.settings.settings.config['Graphs']['Pie']:
			tmpText += colors[0] +","+ colors[1] +"\n"
			
		self.txtPieColors.setText(tmpText)
		
		
		self.connect(self.btnSave, QtCore.SIGNAL('clicked()'), self.save)
		
	def save(self):
		self.settings.settings.config['Graphs']['GetSet'] = str(self.txtGetsSetsColor.text())
		self.settings.settings.config['Graphs']['HitMiss'] = str(self.txtHitMissesColor.text())
		
		tmpColor = []
		for row in str(self.txtPieColors.toPlainText()).split("\n"):
			row_s = str(row).split(',')
			if len(row_s) == 2:
				tmpColor.append((row_s[0], row_s[1]))
			
		self.settings.settings.config['Graphs']['Pie'] = tmpColor
		
		self.settings.save()
		self.close()