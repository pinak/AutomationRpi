from django.shortcuts import render
import RPi.GPIO as GPIO
from django.http import HttpResponse

def toggle(request):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

    mode = request.GET['mode']
    pin = int(request.GET['pin'])
    #TODO: add some validations to check if pin is valid

    if mode == 'on':
        print('turning on')
        GPIO.output(pin, True)

    if mode == 'off':
        print('turning off')
        GPIO.output(pin, False)

    return HttpResponse('done')
