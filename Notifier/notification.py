from win10toast import ToastNotifier

class notifications:

    def notify_start():
    toast = ToastNotifier()
    toast.show_toast('Batter Alert',
                     'Power notifier is starting...',
                     duration=10, 
                     icon_path="../icon1.ico")

    def notify_error():
        toast = ToastNotifier()
        toast.show_toast('Battery Notifier Error', 
                        'Unexpected Error Ocurred: Closing Power Notifier...', 
                        duration=10, 
                        icon_path="../icon1.ico")

    def notify_fullcharge():
        toast = ToastNotifier()
        toast.show_toast('Battery Alert (>97%)',
                        'Battery is fully charged: {}%.'.format(battery_percent),
                        duration=10,
                        icon_path="../icon1.ico")

    def notify_batterylow():
        toast = ToastNotifier()
        toast.show_toast('Battery Alert (<15%)',
                        'Battery is about to be discharged: {}%.'.format(battery_percent),
                        duration=10,
                        icon_path="icon2.ico")