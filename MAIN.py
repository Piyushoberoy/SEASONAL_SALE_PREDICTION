# --------------------------------------------------------------------LAYOUT MODULES------------------------------------------------------------------------
import tkinter as tk
from PIL import ImageTk, Image

# ------------------------------------------------------------PREDICTION & ANALYSATION MODULES--------------------------------------------------------------
import numpy as np
import joblib

model = joblib.load(r"K:\PROGRAMS\PYTHON\SSP\SEASONAL_SALE_PREDICTION\Model.pkl")

class features:
    def __init__(self, frame):
        self.main_frame = frame
        self.frame = tk.Frame(self.main_frame)
        self.frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

        self.sub_frame = tk.Frame(self.main_frame)
        self.sub_frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

        self.font_style = "Gamorand"
        self.font_size = "18"
        self.bg_color = "white"
        self.fg_color = "black"

        self._year_label = tk.Label(self.frame, text="Year")
        self._year = tk.IntVar(value=2002)
        self.year = tk.Entry(self.frame, textvariable=self._year, font=(self.font_style, self.font_size), bg=self.bg_color, fg=self.fg_color)
        self.year.bind('<FocusOut>', self.validate_year)
        
        self._week_label = tk.Label(self.frame, text="Week")
        self._week = tk.IntVar(value = 16)
        self.week = tk.Entry(self.frame, textvariable=self._week, font=(self.font_style, self.font_size), bg=self.bg_color, fg=self.fg_color)
        self.week.bind('<FocusOut>', self.validate_week)

        self.find = tk.Button(self.frame, text="Find", command=self.show_result_form1, font=(self.font_style, self.font_size))
        self.find.grid(row=6, column=1, columnspan=4)
        self.home_btn = tk.Button(self.frame, text="Home", command=self.home, font=(self.font_style, self.font_size))
        self.home_btn.grid(row=7, column=1, columnspan=4)
        
    def validate_year(self, event):
        year = int(self.year.get())
        if year <= 1900:
            self._year.set(1901)
        elif year > 2200:
            self._year.set(2200)

    def validate_week(self, event):
        week = int(self.week.get())
        if week <= 0:
            self._week.set(1)
        elif week > 52:
            self._week.set(52)

    
    def home(self):
        self.frame.destroy()
        self.sub_frame.destroy()
        self.home_class = Home(self.main_frame)

    def form1(self):
        self._year_label.grid(row=1, column=0)
        self.year.grid(row=1, column=1)
        self._week_label.grid(row=1, column=2)
        self.week.grid(row=1, column=3)

    def show_result_form1(self):
        _result = tk.StringVar()
        _result.set("")
        result = tk.Label(self.frame, textvariable=_result)
        
        try:
            _ans = np.array(model.predict([[self._year.get(), self._week.get(), 1]]))
            temp = ""
            for a in _ans:
                temp+=a
            _ans = temp
            _result.set("Food suitable for selected month: "+str(_ans).capitalize())
        except:
            _result.set("ERROR! Enter valid year and week number.")

        result.grid(row=5, column=1, columnspan=4)


class Home:
    def __init__(self, main_window):
        self.main_window = main_window
        self.font_style = "Times New Roman"
        self.font_size = "18"
        self.bg_color = "white"
        self.fg_color = "black"
        self.middle_frame()

    # --------------------------------------------------------------TOP FRAME---------------------------------------------------------------
    def top_frame(self):
        self._top_frame = tk.Frame(self.main_window)
        self._top_frame.pack(side=tk.TOP)
        self.logo = tk.Label(self._top_frame, text="SSP: SEASONAL SALE PREDICTION", compound='top', font=("Algerian", 24))
        self.logo.pack()

    # ------------------------------------------------------------MIDDLE FRAME--------------------------------------------------------------
    def middle_frame(self):
        self._middle_frame = tk.Frame(self.main_window)
        self._middle_frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

        _main_preict_ = tk.Button(self._middle_frame, text="Predict Trending Food", command=self.main_predict, font=(self.font_style, self.font_size))
        _main_preict_.pack()


    def main_predict(self):
        self._middle_frame.destroy()
        _main_predict = features(self.main_window)
        _main_predict.form1()


    # ------------------------------------------------------------BOTTOM FRAME--------------------------------------------------------------

    def bottom_frame(self):
        self._bottom_frame = tk.Frame(self.main_window)
        self._bottom_frame.pack(side=tk.BOTTOM)

        
        self.origin = tk.Label(self._bottom_frame, text="Made with", compound='right', font=("Garamond", 16))
        self.origin.pack()
        self.made_in = tk.Label(self._bottom_frame, text="In India", compound='right', font=("Garamond", 16))
        self.made_in.pack()

        
        self.made_by = tk.Label(self._bottom_frame, text="By Piyush", compound='right', font=("Garamond", 16))
        self.made_by.pack()

def image(img):
    path = "K:\PROGRAMS\PYTHON\SSP\SEASONAL_SALE_PREDICTION\PHOTOS"+"\\"
    im = path+str(img)
    return ImageTk.PhotoImage(Image.open(im))


window = tk.Tk()

window.title("SSP: SEASONAL SALE PREDICTION")
window.geometry("1028x720")

main_window = Home(window)

main_window.top_frame()
lg = image("Logo.png")
main_window.logo.configure(image=lg)

main_window.bottom_frame()
heart = image("Heart.png")
Indian_flag = image("Indian_flag.png")
smile = image("Smile.png")
main_window.origin.configure(image=heart)
main_window.made_in.configure(image=Indian_flag)
main_window.made_by.configure(image=smile)

window.mainloop()
