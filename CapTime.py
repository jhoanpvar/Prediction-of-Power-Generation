import time
import cv2
from tkinter import *
from tkinter import messagebox

def play():
    global bolean
    messagebox.askyesno("Estado de captura", "Realizar captura?")
    cap = cv2.VideoCapture(0)
    i = 0
    while(bolean):
        TIMER = 0
        prev = time.time()
        while TIMER >= 0:
            cur = time.time()
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1
        else:
            ret, img = cap.read()
            cv2.imwrite(f'camera{i}.jpg', img)
            i = i + 1
            TIMER = TIMER + 2 ##editar

def stop():
    messagebox.askyesno("Estado de captura", "Finalizar captura?")
    global bolean
    if(bolean):
        bolean = False
        print("False")

bolean=True