import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from frames import FeetToMeters

# Frame Class
class MetersToFeet(ttk.Frame):
    # Constructor
    def __init__(self,container,controller):
        controller = controller
        super().__init__(container)

        # String Var Values
        self.feet_val = tk.StringVar()
        self.meters_val = tk.StringVar()

        # Meters
        ttk.Label(self,text="Metros: ").grid(column=1,row=1,ipadx=5,sticky=tk.W)
        meters_input = ttk.Entry(self,textvariable=self.meters_val,width=10)
        meters_input.grid(column=2,row=1,sticky=tk.EW)
        meters_input.focus()

        # Feet 
        ttk.Label(self,text="Feet: ").grid(column=1,row=2,ipadx=5,sticky=tk.W)
        feet_input = ttk.Label(self,textvariable=self.feet_val,width=10)
        feet_input.grid(column=2,row=2,sticky=tk.EW)

        # Button calculate
        ttk.Button(self,text="Convert to feet",command=self.mts_to_feet).grid(
            column=1,
            row=3,
            sticky=tk.EW
        )

        # Button switch frames
        ttk.Button(self,text="Switch converter",command=lambda :controller.show_frames(FeetToMeters.FeetToMeters)).grid(
            column=2,
            row=3,
            sticky=tk.EW,
            padx=5
        )

    # Function convert meters to feet
    def mts_to_feet(self):
        try: 
            self.feet_val.set('{:.3f}'.format(int(self.meters_val.get()) * 3.2808))
        except ValueError:
            messagebox.showerror(title="Operation not allowed",message="Invalid values")
            return  
