import datetime

class RegistData:
	
	data_name = ""
	file_name = ""

	def __init__(self):
		self.data_name = 'none'
		self.file_name = './monitor_data.csv'

	def Regist(self, temperature, mode):
		dt_now = datetime.datetime.now()
		write_data = '%s,%.2f,%d\n' % (dt_now, temperature, mode)
		with open(self.file_name, 'a') as f:
			f.write(write_data)

