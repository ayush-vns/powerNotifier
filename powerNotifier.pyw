import psutil
from win10toast import ToastNotifier
import time
import schedule

ico_path1 = '../icon2.ico'
ico_path2 = '../icon1.ico'

def notify_start():
    toast = ToastNotifier()
    toast.show_toast('Batter Alert', 
                     'Power notifier is running...',
                     duration=5, 
                     icon_path=ico_path1)

def notify_error():
    toast = ToastNotifier()
    toast.show_toast('Battery Notifier Error', 
                     'Unexpected Error Ocurred: Closing Power Notifier...', 
                     duration=5, 
                     icon_path=ico_path1)
    
def power_info():
    battery = psutil.sensors_battery()
    plugged_in = battery.power_plugged
    return plugged_in, battery.percent

def notify_fullcharge():
    toast = ToastNotifier()
    toast.show_toast('Battery Alert (>97%)',
                     'Battery is fully charged: {}%.'.format(battery_percent),
                     duration=5,
                     icon_path=ico_path1)

def notify_batterylow():
    toast = ToastNotifier()
    toast.show_toast('Battery Alert (<15%)',
                     'Battery is about to be discharged: {}%.'.format(battery_percent),
                     duration=5,
                     icon_path=ico_path2)
    
notify_start()
    
try:
    def Battery_Alert():    
        
        plugged_in, battery_percent = power_info()

        # print(plugged_in)

        if plugged_in == True:
            print('Power Plugged_in = True\nBattery Percentage: {}%'.format(battery_percent))
            if battery_percent >= 97:
                notify_fullcharge()

        else:
            _, battery_percent = power_info()
            print('Power plugged_in = False\nBattery Percentage: {}%'.format(battery_percent))
            if battery_percent <= 15:
                notify_batterylow()
                
                
    schedule.every(59).seconds.do(Battery_Alert)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
except:
    print('Unexpected Error Occured: Closing Batter Notifier...')
    notify_error()