from datetime import datetime
import time
import tkinter as tk


class Alarm(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Alarm")
        self.time = {"hour": None, "minute": None}

        self.hstr = tk.StringVar()
        self.hstr.set("hour")
        self.mstr = tk.StringVar()
        self.mstr.set("minute")
        self.sstr = tk.StringVar()
        self.sstr.set("second")

        self.hour_label = tk.Label(self, textvariable=self.hstr, padx=20,
                font=("Monocpace", 30), pady=20)
        self.min_label = tk.Label(self, textvariable=self.mstr, padx=20,
                font=("Monocpace", 30), pady=20)
        self.sec_label = tk.Label(self, textvariable=self.sstr, padx=20,
                font=("Monocpace", 30), pady=20)

        self.hour_label.grid(row=1, column=1)
        self.min_label.grid(row=1, column=2)
        self.sec_label.grid(row=1, column=3)
        self.btn = tk.Button(self, text="Set Alarm", command=self.set_frame)
        self.btn.grid(row=2, columnspan=5)


        self.clock()


    def set_frame(self):
        self.topl = tk.Toplevel(self)
        self.topl.title("new Alarm")

        hour_label = tk.Label(self.topl, text="Hour", pady=10)
        min_label = tk.Label(self.topl, text="minute", pady=10)

        hour_label.grid(row=1, column=1)
        min_label.grid(row=1, column=2)

        self.hour_entr = tk.Entry(self.topl)
        self.hour_entr.focus()
        self.min_entr = tk.Entry(self.topl)

        self.hour_entr.grid(row=2, column=1)
        self.min_entr.grid(row=2, column=2)

        btn = tk.Button(self.topl, text="Save", command=self.save_alarm)
        btn.grid(row=3, columnspan=5)


    def save_alarm(self):
        hour = int(self.hour_entr.get())
        minute = int(self.min_entr.get())
        self.topl.destroy()
        self.time = {"hour": hour, "minute": minute}
        print(self.time)




    def clock(self):
        while True:
            current = datetime.now()
            hour = current.strftime("%H")
            minute = current.strftime("%M")
            if self.time["hour"] == int(hour):
                if self.time["minute"] == int(minute):
                    print("Wake Up ... sunshine")
                    break
            second = current.strftime("%S")
            self.hstr.set(hour)
            self.mstr.set(minute)
            self.sstr.set(second)
            self.update()

if __name__ == "__main__":
    app = Alarm()
    app.mainloop()
