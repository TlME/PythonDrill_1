## Simple Time checking GUI
# Displays whether or not branches of an organization are open.
# By Nick Henegar

import time
from Tkinter import *
import ttk
from BizHours import BizHours as bz


class BusinessHours:
    def __init__(self, master):
        #Somewhat sloppy implementation here:
        #instantiating a list of time-stamped objects, mainly just to do it this way.
        portland = bz(-8,"Portland")
        london = bz(0,"London")
        newYork = bz(-5,"New York City")
        locations = [portland, london, newYork]
    #Styling the master window and the two slave frames
        master.title('Business Hours')
        master.resizable(False,False)
        master.configure(background = '#f7f7f7')

        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font = ('Arial', 20))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        # Adding pretty pictures (stored in same folder)
        self.header_img = PhotoImage(file = 'clock.gif')
        self.portland_img = PhotoImage(file = 'portland.gif')
        self.london_img = PhotoImage(file = 'london.gif')
        self.nyc_img = PhotoImage(file = 'nyc.gif')
        # Header
        ttk.Label(self.frame_header, image = self.header_img).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Checking our business hours?', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("You can see the current status of our three branches below:")).grid(row = 1, column = 1)
        #Content
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
     #This loop creates labels for the content frame based on whether or not the business is open at the time of program run.   
        for i in range(0,3):
             ttk.Label(self.frame_content, text = (locations[i].name + ":"),  font = ('Helvetica', 14,'bold') ).grid(row = 0,column = i, padx = 20, sticky = 's')
             if (locations[i].open):
                 ttk.Label(self.frame_content, text = "Open", foreground = 'green', font = ('Impact', 20,'bold')).grid(row = 3,column = (i), padx = 20, sticky = 's')
             else:
                 ttk.Label(self.frame_content, text = "Closed", foreground = 'red', font = ('Impact', 20,'bold')).grid(row = 3,column = (i), padx = 20, sticky = 's')
        ttk.Label(self.frame_content, image = self.portland_img).grid(row = 1, column = 0)
        ttk.Label(self.frame_content, image = self.london_img).grid(row = 1, column = 1)
        ttk.Label(self.frame_content, image = self.nyc_img).grid(row = 1, column = 2) 
                                     

def main():            
    
    root = Tk()
    businessHours = BusinessHours(root)
    root.mainloop()
    
if __name__ == "__main__": main()
