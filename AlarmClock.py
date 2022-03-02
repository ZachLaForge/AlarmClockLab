
class AlarmClock:

    def __init__(self):
        self.current_time = '2:00pm'
        self.alarm_on_or_off = 'True'
        self.alarm_set_to ='4:00pm'
    
    def time_update(self, updated_time): # Set / Change Current time
        self.current_time = updated_time
        print(updated_time)

    def toggle_alarm_on_or_off(self):
        is_on = True
        if is_on == True:
            print(f'This alarm is on and set to{}')