import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from frames import MetersToFeet

# Frame Class
class FeetToMeters(ttk.Frame):
    # Constructor
    def __init__(self,container,controller):
        super().__init__(container)

         # String Var Values
        self.feet_val = tk.StringVar()
        self.meters_val = tk.StringVar()

        # Feets
        ttk.Label(self,text="Feets: ").grid(column=1,row=1,ipadx=5,sticky=tk.W)
        feet_inputs = ttk.Entry(self,textvariable=self.feet_val,width=10)
        feet_inputs.grid(column=2,row=1,sticky=tk.EW)
        feet_inputs.focus()

        # Meters 
        ttk.Label(self,text="Meters: ").grid(column=1,row=2,ipadx=5,sticky=tk.W)
        meters_inputs = ttk.Label(self,textvariable=self.meters_val,width=10)
        meters_inputs.grid(column=2,row=2,sticky=tk.EW)

        # Button calculate
        ttk.Button(self,text="Convert to Meters",command=lambda: self.feet_to_mts()).grid(
            column=1,
            row=3,
            sticky=tk.EW
        )

        # Button switch frames
        ttk.Button(self,text="Switch converter",command=lambda :controller.show_frames(MetersToFeet.MetersToFeet)).grid(
            column=2,
            row=3,
            sticky=tk.EW
        )


    # Function convert feet to meters
    def feet_to_mts(self):
        try:
            mts  = int(self.feet_val.get()) * 0.3048
            self.meters_val.set('{:.3f}'.format(mts))
        except ValueError:
            messagebox.showerror(title="Operation not allowed",message="Invalid values")
            return