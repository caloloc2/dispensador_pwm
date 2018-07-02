#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

pwm1 = GPIO.PWM(24, 100)
pwm1.start(0)

pause_time = 0.02
bandera = 0

def lectura():
	dato = ''
	hora = ''

	horario = open("horarios.rasp", "r")
	for linea in horario.readlines():
		hora+= linea

	a,b,c = hora.split('/')

	actual = time.strftime("%H:%M")

	if (actual==a):
		print "horario 1"
		pwm()
	elif (actual==b):
		print "horario 2"
		pwm()
	elif (actual==c):
		print "horario 3"
		pwm()
	else:
		print "ninguno"
		bandera=0

def pwm():
	if (bandera==0):
		bandera=1
		for i in range(0,101):
			pwm1.ChangeDutyCycle(i)
			time.sleep(pause_time)

		time.sleep(0.2)

		for i in range(100,-1,-1):
			pwm1.ChangeDutyCycle(i)
			time.sleep(pause_time)

try:
	while(1):
		lectura()
		time.sleep(0.5)

except KeyboardInterrupt:
	pwm1.stop()
	GPIO.cleanup() ## Hago una limpieza de los GPIO
	print "Script detenido."