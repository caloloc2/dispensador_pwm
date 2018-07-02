#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) ## GPIO 2 como salida
GPIO.setup(25, GPIO.OUT) ## GPIO 2 como salida

pwm1 = GPIO.PWM(24, 100)   # Creamos el objeto 'pwm1' en el pin 25 a 100 Hz  
pwm2 = GPIO.PWM(25, 100)     # Creamos el objeto 'pwm2' en el pin 24 a 100 Hz 
  
pwm1.start(0)              # Iniciamos el objeto 'pwm1' al 0% del ciclo de trabajo (completamente apagado)  
pwm2.start(0)              # Iniciamos el objeto 'pwm2' al 0% del ciclo de trabajo (completamente apagado)

pause_time = 0.02           # Declaramos un lapso de tiempo para las pausas

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
	elif (actual==b):
		print "horario 2"
	elif (actual==c):
		print "horario 3"
	else:
		print "ninguno"

def pwm():
	for i in range(0,101):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
            pwm1.ChangeDutyCycle(i)      # LED #1 = i
            pwm2.ChangeDutyCycle(100 - i)  # LED #2 resta 100 - i
            sleep(pause_time)             # Pequeña pausa para no saturar el procesador
        for i in range(100,-1,-1):        # Desde i=100 a i=0 en pasos de -1  
            pwm1.ChangeDutyCycle(i)      # LED #1 = i
            pwm2.ChangeDutyCycle(100 - i)  # LED #2 resta 100 - i  
            sleep(pause_time)             # Pequeña pausa para no saturar el procesador  

try:
	while(1):
		lectura()
		time.sleep(0.1)

except KeyboardInterrupt:
	pwm1.stop()
    pwm2.stop()  
	GPIO.cleanup() ## Hago una limpieza de los GPIO
	print "Script detenido."