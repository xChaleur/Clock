from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import datetime

def is_first_or_third_friday(date):
    if date.weekday() != 4:  # Check if it's Friday
        return False

    day = date.day

    # Check if it's the 1st or 3rd Friday
    if 1 <= day <= 7 or 15 <= day <= 21:
        return True

    return False

class AlarmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Alarm Status: Not Set")
        layout.add_widget(self.label)
        
        alarm_button = Button(text="Check and Set Alarm")
        alarm_button.bind(on_press=self.check_and_set_alarm)
        layout.add_widget(alarm_button)
        
        return layout

    def check_and_set_alarm(self, instance):
        today = datetime.date.today()

        if is_first_or_third_friday(today):
            self.label.text = "Alarm Status: Set for Today"
        else:
            self.label.text = "Alarm Status: Skipping Today"

if __name__ == '__main__':
    AlarmApp().run()
