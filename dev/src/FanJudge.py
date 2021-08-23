class FanJudge:

	upper_border_over_count = 0
	lower_border_under_count = 0

	upper_border = 48.0
	lower_border = 44.0
	
	def __init__(self):
		print("FanJudge")

	def judge(self, temperature):
		if self.upper_border < temperature:
			self.upper_border_over_count += 1
		elif temperature < self.lower_border:
			self.lower_border_under_count += 1
		else:
			self.upper_border_over_count = 0
			self.lower_border_under_count = 0

		judge_mode = 2		# No operation
		if 10 < self.upper_border_over_count:
			judge_mode = 1	#Turn On
			self.upper_border_over_count = 10

		if 10 < self.lower_border_under_count:
			judge_mode = 0	#Turn Off
			self.lower_border_under_count = 10

		print('temperature = %f' % temperature)
		print('under_count = %d' % self.lower_border_under_count)
		print('over_count = %d' % self.upper_border_over_count)
		print('judge_mode = %d' % judge_mode)


		return judge_mode

