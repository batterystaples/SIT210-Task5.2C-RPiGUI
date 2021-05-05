#!/usr/bin/python 

import Tkinter
import RPi.GPIO as GPIO

head = Tkinter.Tk()

RED_LED = 3
YELLOW_LED = 5
GREEN_LED = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def light():
	l = led.get()
	for pin in [RED_LED, YELLOW_LED, GREEN_LED]:
		if l == pin:
			GPIO.output(pin, GPIO.HIGH)
		else:
			GPIO.output(pin, GPIO.LOW)

led = Tkinter.IntVar()
red_option = Tkinter.Radiobutton(head, text="Red", variable=led, value=RED_LED, command=light)
yellow_option = Tkinter.Radiobutton(head, text="Yellow", variable=led, value=YELLOW_LED, command=light)
green_option = Tkinter.Radiobutton(head, text="Green", variable=led, value=GREEN_LED, command=light)
red_option.pack()
yellow_option.pack()
green_option.pack()

def turn_off_all():
	red_option.deselect()
	yellow_option.deselect()
	green_option.deselect()
	GPIO.output(RED_LED, GPIO.LOW)
	GPIO.output(YELLOW_LED, GPIO.LOW)
	GPIO.output(GREEN_LED, GPIO.LOW)

turn_off_all()

def exit_callback():
	turn_off_all()
	exit()

exit_button = Tkinter.Button(head, text="Exit", command=exit_callback)
exit_button.pack()

head.mainloop()

