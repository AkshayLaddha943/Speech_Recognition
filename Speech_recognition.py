# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:51:48 2020

@author: Admin
"""
import operator
import speech_recognition as sr
sr.__version__

r = sr.Recognizer() # purpose of a Recognizer instance is, to recognize speech
mic = sr.Microphone()

sr.Microphone.list_microphone_names()    #To get a list of microphone names

#Recognizer class has seven methods for recognizing speech
#recognize_bing(): Microsoft Bing Speech
#recognize_google(): Google Web Speech API
#recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
#recognize_houndify(): Houndify by SoundHound
#recognize_ibm(): IBM Speech to Text
#recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
#recognize_wit(): Wit.ai

#Using audio file as input
song = sr.AudioFile('D:\\Speech_Recognition\\Avicii - Hey Brother.wav')    #context manager opens the file and reads its contents, storing the data in an AudioFile instance called source
with song as source:
    r.adjust_for_ambient_noise(source , duration=0.5)
    audio = r.record(source)                                                #record() method records the data from the entire file into an AudioData instance.
    
r.recognize_google(audio , show_all=True)

#Using mic as input
with mic as source:
    r.adjust_for_ambient_noise(source)    
    audio = r.listen(source, timeout=3)                                               #listen method to capture input from microphone
    
word = r.recognize_google(audio)
word = word.split()
word[0] = int(word[0])
word[2] = int(word[2])
word[1] = operator.add
"".join(word)