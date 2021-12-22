from tkinter import *
import datetime
import time
import winsound

clock=Tk()
clock.title("set alarm ")
clock.geometry('500x400')
time_formate=Label(clock,text='input time in 24 hr format ',fg='red',bg='black',font='Arial').place(x=120,y=150)
add_time=Label(clock,text='hrs  min  sec ',font=60).place(x=200,y=35)
set_alaram=Label(clock,text='when you want to wake up ',fg="blue",relief='solid',font=('helevetica',9,'bold')).place(x=0,y=70)

def alarm(set_alarm_timer):
    while True:
         time.sleep(1)
         current_time = datetime.datetime.now()
         now=current_time.strftime("%H:%M:%S")
         date=current_time.strftime("%d:%m:%y")
         print(now)
         print(set_alarm_timer)
         if now==set_alarm_timer:
            print("time to wake up ")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break


def actual_time():
    set_alarm_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


hour=StringVar()
min=StringVar()
sec=StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 8).place(x=190,y=70)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 8).place(x=230,y=70)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 8).place(x=270,y=70)
submit_button=Button(clock,text='submit',font=('Arial',10),command=actual_time).place(x=230,y=100)


clock.mainloop()
