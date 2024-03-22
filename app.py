# Dependencies
import tkinter as tk
from tkinter import ttk

# Frames
from frames.MetersToFeet import MetersToFeet
from frames.FeetToMeters import FeetToMeters

# Main app 
class DistanceConverter(tk.Tk):
     
    # Constructor.
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.frames = dict()
        self.title("Distance Converter")

        # Container Frame
        container = ttk.Frame(self)
        container.grid(padx=10,pady=10,sticky=tk.EW)
        
        # Add frames to a dictionary
        for FrameClass in (MetersToFeet,FeetToMeters):
            # Param:container => frame where it will be placed 

            frame = FrameClass(container,self) #Instantaties the frame by passing  it some parameters
            self.frames[FrameClass] = frame # Global dictionary assigning values by key.
            frame.grid(column=0,row=0,sticky=tk.NSEW) # layout frame
        # Call function
        self.show_frames(MetersToFeet)

    # Function that will help us change and move between different frames
    def show_frames(self,frameClass):
        # assigns the value to the variable, accessing the dictionary through its value key 
        # which will be equivalent to the name of the frame.
        frame = self.frames[frameClass]
        frame.tkraise()




if __name__ == "__main__":
    root = DistanceConverter()
    root.mainloop()