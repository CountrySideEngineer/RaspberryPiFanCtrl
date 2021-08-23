import RPi.GPIO as GPIO

class GPIOFan:

	gpio_pin = 0

	def __init__(self):
		self.gpio_pin = 0
		GPIO.setwarnings(False)

	def __init__(self, gpio_pin):
		self.gpio_pin = gpio_pin
		GPIO.setwarnings(False)

	def On(self):
		'''Turn on FAN.
		'''
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.gpio_pin, GPIO.OUT)

		GPIO.output(self.gpio_pin, GPIO.HIGH)

	def Off(self):
		'''Turn off FAN.
		'''
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.gpio_pin, GPIO.OUT)

		GPIO.output(self.gpio_pin, GPIO.LOW)

