# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:33:02 2020

@author: Admin
"""
import operator
import speech_recognition as s_r
r = s_r.Recognizer()
my_mic_device = s_r.Microphone()
with my_mic_device as source:
    print("Say what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=2)
my_string=r.recognize_google(audio)
print(my_string)
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'multiply' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

print(eval_binary_expr(*(my_string.split())))
