import psutil
import time
import schedule

notify_start()

def power_info():
    battery = psutil.sensors_battery()
    plugged_in = battery.power_plugged
    return plugged_in, battery.percent
    
try:
    def Battery_Alert():    
        
        plugged_in, battery_percent = power_info()

        if plugged_in == True:
            if battery_percent >= 97:
                notify_fullcharge()

        else:
            _, battery_percent = power_info()
            if battery_percent <= 15:
                notify_batterylow()
                
                
    schedule.every(59).seconds.do(Battery_Alert)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
except:
    notify_error()