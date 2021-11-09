import time
from notification import notifications

class importantUtilities:
    def __init__(self):
        pass

    def power_info(self):
        battery = psutil.sensors_battery()
        plugged_in = battery.power_plugged
        return plugged_in, battery.percent

    def cpu_info(self):
        pass

    def memory_info(self):
        pass