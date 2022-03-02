
class AlarmClock:

    def __init__(self):
        self.current_time = '2:00pm'
        self.alarm_on_or_off = 'False'
        self.alarm_set_to ='4:00pm'
    

    def time_update(self, updated_time): # Set / Change Current time
        self.current_time = updated_time
        print(f' The current time is now {self.current_time}')


    def alarm_toggle(self):
        if self.alarm_on_or_off == False:
            self.alarm_on_or_off = True
            print(f'Your alarm is on')
        else:
            print(f' Your alarm is off ')


    def set_alarm(self, time):
        self.alarm_set_to = time
        print(f' The alarm is now set to:{self.alarm_set_to}')


