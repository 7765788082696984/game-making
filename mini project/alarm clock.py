# import required library
from tkinter import *
import datetime
import time
import winsound
# multiple tasks
from threading import *

# Create object
# an object is simply a collection of data (variables) and methods(functions) that act on those data.
# similarly, a class is a blueprint for that object.
root = Tk()

# set geometry
root.geometry("400x200")


# use threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    # infinite loop
    while True:
        # set alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # wait for one seconds
        time.sleep(1)

        # Get current time
        # used to convert date and time objects to their string representation
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

        # add labels, frame, button, optionmenus


# fg= foreground
# declares the position of widgits in relation to each other:==pack
# pady:== How many pixels to pad widget, horizontally and vertically, ouside v's borders
Label(root, text="Alarm Clock", font=("Helvetica 2 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

# used to organize the group of widgets
frame = Frame(root)
frame.pack()

# helps you manage the value of a widget such as a Label or Entry more effectively
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()