# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:11:51 2020

@author: Admin
"""
import speech_recognition as sr
r = sr.Recognizer()                   # purpose of a Recognizer instance is, to recognize speech
mic = sr.Microphone()

   

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Instructions : ")
print("\n")
print("Pronounce 143 as : One Hundred and forty three (for clarity)")
print("\n")
print("Pronounce 107 as : One Zero seven (for clarity)")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    
    with mic as source:
         choice = input("Enter choice(Plus/minus/multipy/Divide): ")
         r.adjust_for_ambient_noise(source)    
         audio = r.listen(source, timeout=3) 
    select_1 = r.recognize_google(audio)
    print(select_1)
    
    if select_1 == 'Plus':
        with mic as source:
         num_1 = input("Enter 1st Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_1 = r.listen(source, timeout=3)
        num1 = r.recognize_google(audio_1)
        num1 = int(num1)
        print(num1)
        with mic as source:
         num_2 = input("Enter 2nd Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_2 = r.listen(source, timeout=3)
        num2 = r.recognize_google(audio_2)
        num2 = int(num2)
        print(num2)
        print(num1, "+", num2, "=", add(num1, num2))
        
    elif select_1 == '-':
        with mic as source:
         num_1 = input("Enter 1st Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_1 = r.listen(source, timeout=3)
        num1 = r.recognize_google(audio_1)
        num1 = int(num1)
        print(num1)
        with mic as source:
         num_2 = input("Enter 2nd Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_2 = r.listen(source, timeout=3)
        num2 = r.recognize_google(audio_2)
        num2 = int(num2)
        print(num2)
        print(num1, "-", num2, "=", subtract(num1, num2))
        
    elif select_1 == 'multiply':
        with mic as source:
         num_1 = input("Enter 1st Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_1 = r.listen(source, timeout=3)
        num1 = r.recognize_google(audio_1)
        num1 = int(num1)
        print(num1)
        with mic as source:
         num_2 = input("Enter 2nd Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_2 = r.listen(source, timeout=3)
        num2 = r.recognize_google(audio_2)
        num2 = int(num2)
        print(num2)
        print(num1, "*", num2, "=", multiply(num1, num2))
        
    elif select_1 == 'divide':
        with mic as source:
         num_1 = input("Enter 1st Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_1 = r.listen(source, timeout=3)
        num1 = r.recognize_google(audio_1)
        num1 = int(num1)
        print(num1)
        with mic as source:
         num_2 = input("Enter 2nd Number : ")
         r.adjust_for_ambient_noise(source)    
         audio_2 = r.listen(source, timeout=3)
        num2 = r.recognize_google(audio_2)
        num2 = int(num2)
        print(num2)
        print(num1, "/", num2, "=", divide(num1, num2))



        
        


