from tkinter import *
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

from subprocess import call

cmd_beg= 'espeak '
cmd_end= ' 2>/dev/null' # To dump the std errors to /dev/null

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def up():
    count1 = 'Move'
    count2 = 'Up'
    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+count1+count2+cmd_end], shell=True)
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)

def down():
    count1 = 'Move'
    count2 = 'Down'
    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+count1+count2+cmd_end], shell=True)
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,False)

def left():
    count1 = 'Move'
    count2 = 'Left'
    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+count1+count2+cmd_end], shell=True)
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)

def right():
    count1 = 'Move'
    count2 = 'Right'
    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+count1+count2+cmd_end], shell=True)
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)

def wait():
    count1 = 'Wait'
    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+count1+cmd_end], shell=True)
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)

button1 = Button(topFrame,text="Left",fg="red",command=left)
button2 = Button(topFrame,text="Up",fg="blue",command=up)
button3 = Button(topFrame,text="Right",fg="green",command=right)
button4 = Button(bottomFrame,text="Down",fg="purple",command=down)
button5 = Button(bottomFrame,text="Quit",fg="black",command=quit)
button6 = Button(bottomFrame,text="Wait",fg="brown",command=wait)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
button5.pack(side=BOTTOM)
button6.pack(side=BOTTOM)

root.mainloop()

#Close down curses properly, inc turn echo back on!
GPIO.cleanup()
