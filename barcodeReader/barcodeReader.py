from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtNetwork
import sys
import os
from barcodeUI import Ui_barcodeUI


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

class Gui(QtWidgets.QMainWindow):

    ## Signals
    #closeGui = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.m_device = QtMultimedia.QAudioDeviceInfo.defaultOutputDevice()
        self.m_output = None
        ## Instantiate classes
        self.ui = Ui_barcodeUI()
        self.ui.setupUi(self)
        self.initializeAudio()
        ## Video stuff
        #self._timer = QtCore.QTimer( self )
        #self._timer.timeout.connect( self.play )
        #self._timer.start(27)
        #self.update()
        self.ui.play.clicked.connect(self.playSound)
        self.beep = {
                     'Group 1': QtMultimedia.QSound(resource_path(os.path.join('data',"group1.wav"))),
                     'Group 2': QtMultimedia.QSound(resource_path(os.path.join('data',"group2.wav"))),
                     'Group 3': QtMultimedia.QSound(resource_path(os.path.join('data',"group3.wav")))
                     }

        self.ui.barcode.returnPressed.connect(self.playSound)
    def initializeAudio(self):


        self.m_format = QtMultimedia.QAudioFormat()
        self.m_format.setSampleRate(44100)
        self.m_format.setChannelCount(1)
        self.m_format.setSampleSize(16)
        self.m_format.setCodec('audio/pcm')
        self.m_format.setByteOrder(QtMultimedia.QAudioFormat.LittleEndian)
        self.m_format.setSampleType(QtMultimedia.QAudioFormat.SignedInt)

        info = QtMultimedia.QAudioDeviceInfo(QtMultimedia.QAudioDeviceInfo.defaultOutputDevice())
        if not info.isFormatSupported(self.m_format):
            QtWidgets.QMessageBox.information( self, "Invalid format", "Default audio format not supported, trying something else")

            self.m_format = info.nearestFormat(self.m_format)

        #self.m_generator = QtMultimedia.Generator(self.m_format,
        #        self.DurationSeconds * 1000000, self.ToneSampleRateHz, self)

        self.createAudioOutput()
    def createAudioOutput(self):
        self.m_audioOutput = QtMultimedia.QAudioOutput(self.m_device, self.m_format)
        #self.m_audioOutput.notify.connect(self.notified)
        #self.m_audioOutput.stateChanged.connect(self.handleStateChanged)

        #self.m_generator.start()
        #self.m_audioOutput.start(self.m_generator)
        #self.m_volumeSlider.setValue(self.m_audioOutput.volume() * 100)

    #def deviceChanged(self, index):
    #    self.m_pullTimer.stop()
    #    self.m_generator.stop()
    #    self.m_audioOutput.stop()
    #    self.m_device = self.m_deviceBox.itemData(index)

    #    self.createAudioOutput()

    
    def playSound( self ):
        #self.ui.statusbar.showMessage('')
        val = self.ui.barcode.text()
        try:
            self.beep[str(val)].play()
        except KeyError:
            QtWidgets.QMessageBox.information( self, "Invalid barcode read", "Barcode scanner output doesn't match a group")
            
        self.ui.barcode.setText('') 
        #self.ui.statusbar.showMessage('Ready for input')
def main():
    app = QtWidgets.QApplication( sys.argv )
    #filter = ValEventFilter()
    #app.installEventFilter(filter)
    g = Gui()
    g.show()
    sys.exit( app.exec_() )

if __name__ == '__main__':
    main()
