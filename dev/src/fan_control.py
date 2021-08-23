import GPIOFan
import CpuInformation
import FanJudge
import RegistData
import time

def fan_control_method():
	cpuInfo = CpuInformation.CpuMonitor()
	fan_judge = FanJudge.FanJudge()
	gpio_fan = GPIOFan.GPIOFan(2)
	regist_data = RegistData.RegistData()
	
	while (1):
		cpu_temp = cpuInfo.GetCpuTemperature()
		fan_action = fan_judge.judge(cpu_temp)
		if 1 == fan_action:
			gpio_fan.On()
		elif 0 == fan_action:
			gpio_fan.Off()

		regist_data.Regist(cpu_temp, fan_action)

		time.sleep(1)


if __name__ == '__main__':
	fan_control_method()


