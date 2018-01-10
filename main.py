import GUI
import os
import sys
import numpy as np
from scipy.io import wavfile
import scipy.signal as sc
from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
from PyQt4 import QtGui, QtCore

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
from PyQt4 import QtGui,QtCore
from IPython.display import Audio
import wave
import os
import struct
import numpy as np
from scipy.io.wavfile import read,write
from scipy.fftpack import fft
import pylab as plt
from scipy.fftpack import rfft, irfft, fftfreq , fftshift , ifft,fft
import scipy.io.wavfile
import wave
import os
from scipy.io import wavfile as wav #libraries to upload .wav sound file
from IPython.display import Audio
import sounddevice as sd
from xml.dom import minidom



length = int	#holds lenght of the signal array
samples = np.array	#holds the data of the signal array (imported or rec)
FSample = int 		#holds the sampling frequency
scaled = np.array  #holds the data after scaling for playing

class hello(QtGui.QMainWindow, GUI.Ui_Form): 

    def __init__(self):
        super(hello, self).__init__()
        self.setupUi(self)
        self.Import.clicked.connect(self.ImportFn)  #button import click calls ImportFn function
        self.Listen.clicked.connect(self.ListenFn)	#button Listen click calls ListenFn function
        self.Record.clicked.connect(self.RecordFn)	#button Record click calls RecordFn function
        self.Save.clicked.connect(self.FunctionSave)	#button Save click calls FunctionSave function

        self.FirstOption.clicked.connect(self.onFilterChanged) #onFilterChanged is called when any filter is selected
        self.SecondOption.clicked.connect(self.onFilterChanged)
        self.ThirdOption.clicked.connect(self.onFilterChanged)
 
        self.files = ["Lowpass.xml", "Highpass.xml", "Butterworth.xml"]		#the XML files that holds the filtered data
        self.zeros, self.poles = [], [] #array that holds zeros and poles

        self.Num, self.Dom = [], [] #arrays to hold numenerators and denomenators of the transfere dunction


        #figuers code for ploting

        #data frequency figure
        figure = plt.figure()  
        plt.grid(True)
        self.axis_f_1 = figure.add_subplot(111)  
        self.axis_f_1.set_ylim(0, 2)
        self.axis_f_1.set_xlim(0, np.pi)
        self.frequency_widget = FigureCanvas(figure)
        self.mplvlf.addWidget(self.frequency_widget)
        self.frequency_widget.draw()

        #data phase figure
        self.axis_f_2 = figure.add_subplot(111)
        self.axis_f_2.set_ylim(0, 2)
        self.axis_f_2.set_xlim(0, np.pi)
        self.phase_widget = FigureCanvas(figure)
        self.mplvlp.addWidget(self.phase_widget)
        self.phase_widget.draw()

        #filter frequency figure
        figure = plt.figure()
        plt.grid(True)
        self.axis_s_ttf_before = figure.add_subplot(111)
        self.frequency_widget_b = FigureCanvas(figure)
        self.mplvlfb.addWidget(self.frequency_widget_b)
        self.frequency_widget_b.draw()

        #filter phase responce figure
        figure = plt.figure()
        plt.grid(True)
        self.axis_p_ttf_before = figure.add_subplot(111)
        self.phase_widget_b = FigureCanvas(figure)
        self.mplvlpb.addWidget(self.phase_widget_b)
        self.phase_widget_b.draw()

        #output signal frequency figure
        figure = plt.figure()
        plt.grid(True)
        self.axis_s_ttf_after = figure.add_subplot(111)
        self.frequency_widget_a = FigureCanvas(figure)
        self.mplvlfa.addWidget(self.frequency_widget_a)
        self.frequency_widget_a.draw()

        #output signal phase figure
        figure = plt.figure()
        plt.grid(True)
        self.axis_p_ttf_after = figure.add_subplot(111)
        self.phase_widget_a = FigureCanvas(figure)
        self.mplvlpa.addWidget(self.phase_widget_a)
        self.phase_widget_a.draw()

        self.length = int
        self.samples = np.array
        self.FSample = int
        self.weHaveSample = False
        self.outputSignal = []

	

    def ImportFn(self):
        global samples #deal with global samples array
        global FSample #deal with global sampling frequency
        global length

        self.outputSignal=[]

        filePath = QtGui.QFileDialog.getOpenFileNames(self, 'Choose a file', "~/Documents/Study/DSP/Bilal$", '*.WAV') #get file path

        fileName = ''.join(map(str, filePath)) #get desired to import file name
        sys.path.append(str(filePath))

        FSample, samples = read(str(fileName)) #read .wav sound file samples

        time = (len(samples))/float(FSample) #Calculate files duration

        length = len(samples) #calculating files lenght

        print("imported")

        self.weHaveSample = True  #boolen variable set true when data is imported
        sd.play(samples, FSample)
        self.gotSignal([self.axis_s_ttf_before, self.axis_p_ttf_before], [self.frequency_widget_b, self.phase_widget_b], samples)
        #to print the frequencies and phases of my signal 

    def gotSignal(self, axis, widgets, data):
        axis[0].cla() #clear axis before drawing
        mysamples = np.array #np array to hold the fourier transform of the data
        myData = data #get a copy of the data
        mysamples = fft(myData) #fourier transforming the data
        mysamples2 = abs(mysamples[0:len(mysamples)/2].copy()) #taking half the absolute of the fourier domain for ploting 
        axis[0].plot(mysamples2) #plotting the frequencies
        widgets[0].draw() 
        phase = [] #array to hold the phases
        
        axis[1].cla() #clearing axis
        phase = np.angle(mysamples) #getting the phases form the angle between real and imag components of the fourier array
  
        axis[1].plot(phase)
        widgets[1].draw()

    def FunctionSave(self): #the function to save the data after filtering
    	filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".conf") #gets file name and path
        scipy.io.wavfile.write(filename, FSample, scaled) #save the file 

    def RecordFn(self): #function to record 5 seconds the input data
        global samples	#deal with global samples array
        global FSample	#deal with global sampling frequency
        self.weHaveSample = True   #boolen variable set true when data is imported
        

        duration = 5 #duration of the audio in seconds
        FSample = 44100 #sampling frequency of the recorded audio
        
        
        samples = sd.rec(duration * FSample, samplerate=FSample, channels=1,blocking=True,dtype='float64') #recording
        
        
        self.gotSignal([self.axis_s_ttf_before, self.axis_p_ttf_before], [self.frequency_widget_b, self.phase_widget_b], samples)
        #draw the recorded audio
        sd.play(samples,FSample) #play recorded audio

    def onFilterChanged(self): #Read files depending on the user selection
        self.reset() #calls reset functions to clear previous zeros and poles
        if self.FirstOption.isChecked():
            self.readFile(1)
        if self.SecondOption.isChecked():
            self.readFile(2)
        if self.ThirdOption.isChecked():
            self.readFile(3)

    def ListenFn(self): #function applies the filter on the signal
        if self.weHaveSample: #checks  if we have data
            global samples         
            global scaled

            length = len(samples)
            y = np.zeros(length)
            self.Num = self.Num / self.Num[0]
            self.Dom = self.Dom / self.Num[0]
            ##cycling over all the samples , for every sample accumelate the terms of coeefecients a and b
            for i in range(0,length):
				for j in range(1,len(self.Num)):
					if (i - j > 0):
						y[i] = y[i] - y[i-j] * self.Num[j]

				for j in range(0,len(self.Dom)):
					if (i - j > 0):
						y[i] = y[i] + samples[i]*self.Dom[j]

            self.outputSignal = y




            '''
            cDom = 0 #pointer moves along the Demonerator array of the transfere function 
            
            while cDom < len(self.Dom)+1:
            	self.outputSignal.append(0) #puts zeros in the first outputs as new outputs depends on older ones
            	cDom += 1


            i = len(self.Num) #starts in the read array from the element = order of the numenerator

            while i < len(samples): #to the last sample
            	outputElement = 0.0 #zeroing the temp value
                cNum = 0 #zeroing the numenerator pointer
                cDom = 1 #zeroing the Demonerator pointer

                while cNum < len(self.Num): #moves along the numenerator

                    outputElement += samples[i-cNum-1].copy() * self.Num[cNum].copy() #adding the sample multiplied by its numenerator coeff.
                    cNum += 1 #incrementing pointer

                while cDom < len(self.Dom):#moves along the numenerator
                	outputElement -= self.outputSignal[len(self.outputSignal)-cDom] * self.Dom[cDom].copy()#adding the older outputs multiplied by its Demonerator coeff.
                	cDom += 1  #incrementing pointer

                self.outputSignal.append(outputElement) #adding the calculated element to the output array
                i += 1 #incrementing pointer
                '''
        self.gotSignal([self.axis_s_ttf_after, self.axis_p_ttf_after], [self.frequency_widget_a, self.phase_widget_a], self.outputSignal)#drawing signal after filtering
        scaled = (self.outputSignal / (0.85* np.max(np.abs(self.outputSignal)))) #scale signal for audio playing
        sd.play(scaled, FSample) #play filtered audio

    def reset(self): #reset function called when filter is selected or changed
        self.frequency_widget.draw()  #clearing drawing
        self.zeros, self.poles = [], [] #clearing zeroes and poles
        self.outputSignal = [] #emptying the output signal 

    def readFile(self, type): #read xml files function (gets file number in the file list)
        xmldoc = minidom.parse(self.files[type - 1]) #parsing 
        myKValue = xmldoc.getElementsByTagName('Filter') #getting elements with tag Filter 
        zerosList = xmldoc.getElementsByTagName('zero') #get zeroes tag 
        polesList = xmldoc.getElementsByTagName('pole') #get poles tag
        k = float(myKValue[0].attributes['k'].value) #
        for zero in zerosList: #get all zeroes
            x = round(float(zero.attributes['x'].value), 5)
            y = round(float(zero.attributes['y'].value), 5)
            zero = complex(x, y) 
            self.zeros.append(zero) #dd zeroes to the zeroes list
        for pole in polesList: #get all poles
            x = round(float(pole.attributes['x'].value), 5)
            y = round(float(pole.attributes['y'].value), 5)
            pole = complex(x, y)
            self.poles.append(pole) #dd poles to the poles list

        

        self.drawFilterResponse(k) #call function to draw the filters frequency and phase responce

    def drawFilterResponse(self, k): #takes the filter file number and draw the phase and freq responce
        self.axis_f_1.cla() #clearing axis before drawing
        self.Num, self.Dom = sc.zpk2tf(self.zeros, self.poles, k) #get the transfere function from zeroes and poles


        w, h = sc.freqz(self.Num, self.Dom) #gets signal values at different frequencies
        
        phaseImpulse = np.angle(h) # gets the phases
        self.axis_f_2.cla()		#clear old figures

        self.axis_f_2.plot(phaseImpulse) #draw phase  responce
        self.phase_widget.draw()

        self.axis_f_1.cla()		#clear old figures        
        self.axis_f_1.set_ylim(0, 2)
        self.axis_f_1.set_xlim(0, np.pi)
        self.axis_f_1.plot(w, abs(h)) #draw freq responce
        self.frequency_widget.draw()       
	


def main():
	App = QtGui.QApplication(sys.argv)
	form = hello()
	form.show()
	App.exec_()


if __name__ == '__main__':
	main()







