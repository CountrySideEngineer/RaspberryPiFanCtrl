import subprocess
import time
import sys
import re

class CpuMonitor:
	
	def __init__(self):
		'''Constructor
		'''

	def GetCpuTemperature(self):

		cpuinfos = subprocess.getoutput("vcgencmd measure_temp").split('=')
		temperature = cpuinfos[1]		#Get CPU temperature
		temperature = temperature[:-2]	#Remove unit from temperature string.

		temperature_float = float(temperature)	#Convert string to float type.

		return temperature_float

