# Unit Converter (Temperature, Area, Speed  and more.)
# This is a simple graphical unit converter that converts various units between one another.
# Developer: Upesh Maharana 
# Dated: 2021/04/25
# ------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from math import * 


root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x600")
root.config(background='wheat1')

# A function for updating the dropdown lists upon selecting the operation.
def updateSubLists(self):
    y.set('')
    z.set('')
    subUnitListFrom['menu'].delete(0,'end')
    subUnitListTo['menu'].delete(0,'end')
     
    for item in list(listOfUnits.get(x.get())):
        subUnitListFrom['menu'].add_command(label=item,command=tk._setit(y,item))
        subUnitListTo['menu'].add_command(label=item,command=tk._setit(z,item))
    
    y.set('Please select an option')
    z.set('Please select an option')
    
    fromVar.set("")
# A callback function to validate if the data entered is only digit or not.
def validateUserInput(input):
    """This method validates the data entered by the User to check if the entered data is a number or not."""
    if input.isdigit() == True:
        return True
    elif input == "":
        return True
    else:
        messagebox.showinfo("Information","Only number is allowed")
        return False
  

# A function for resetting the entries selected.
def resetEntries():
    """ This method helps in resetting the entries given as a input or selected by the User"""
    x.set("")
    unitList["menu"].delete(0,'end')
    for item in list(listOfUnits.keys()):
        unitList['menu'].add_command(label=item,command=tk._setit(x,item,updateSubLists))
    x.set(list(listOfUnits.keys())[0])
    updateSubLists('')
    #fromEntry.delete(0,'end')
    #ToEntry.delete(0,'end')

    fromVar.set("")
    result_Window.delete('1.0','end')

def calcArea(frm,to,val):
    if frm == 'SquareKilometer' and to == "SquareMeter":
	    result = float(val) * 1000000
    elif frm == 'SquareKilometer' and to == "SquareMile":
	    result = float(val) * 0.386102
    elif frm == 'SquareKilometer' and to == "SquareYard":
	    result = float(val) * 1195990.05    
    elif frm == 'SquareKilometer' and to == "SquareFoot":
	    result = float(val) * 10763910.41671
    elif frm == 'SquareKilometer' and to == "SquareInch":
	    result = float(val) * 1550003100.0062
    elif frm == 'SquareKilometer' and to == "Hectare":
	    result = float(val) * 100
    elif frm == 'SquareKilometer' and to == "Acre":
	    result = float(val) * 247.105     
    elif frm == 'SquareMeter' and to == "SquareKilometer":
	    result = float(val) * 0.0000010     
    elif frm == 'SquareMeter' and to == "SquareMile":
	    result = float(val) * 0.00000038610215854245     
    elif frm == 'SquareMeter' and to == "SquareYard":
	    result = float(val) * 1.19599     
    elif frm == 'SquareMeter' and to == "SquareFoot":
	    result = float(val) * 10.764   
    elif frm == 'SquareMeter' and to == "SquareInch":
	    result = float(val) * 1550    
    elif frm == 'SquareMeter' and to == "Hectare":
	    result = float(val) * 0.0001    
    elif frm == 'SquareMeter' and to == "Acre":
	    result = float(val) * 0.000247105    
    elif frm == 'SquareMile' and to == "SquareKilometer":
	    result = float(val) * 2.59    
    elif frm == 'SquareMile' and to == "SquareMeter":
	    result = float(val) * 2589988.110336
    elif frm == 'SquareMile' and to == "SquareYard":
	    result = float(val) * 3097600
    elif frm == 'SquareMile' and to == "SquareFoot":
	    result = float(val) * 27878400
    elif frm == 'SquareMile' and to == "SquareInch":
	    result = float(val) * 4014489599.4792
    elif frm == 'SquareMile' and to == "Hectare":
	    result = float(val) * 259
    elif frm == 'SquareMile' and to == "Acre":
	    result = float(val) * 640
    elif frm == 'SquareYard' and to == "SquareKilometer":
	    result = float(val) * 0.00000083612736
    elif frm == 'SquareYard' and to == "SquareMeter":
	    result = float(val) * 1.196
    elif frm == 'SquareYard' and to == "SquareMile":
	    result = float(val) * 3.2283058 * pow(10,-7) 
    elif frm == 'SquareYard' and to == "SquareFoot":
	    result = float(val) * 9
    elif frm == 'SquareYard' and to == "SquareInch":
	    result = float(val) * 1296
    elif frm == 'SquareYard' and to == "Hectare":
	    result = float(val) / 11960
    elif frm == 'SquareYard' and to == "Acre":
	    result = float(val) / 4840
    elif frm == 'SquareFoot' and to == "SquareKilometer":
	    result = float(val) * 0.00000009290304
    elif frm == 'SquareFoot' and to == "SquareMeter":
	    result = float(val) / 10.764
    elif frm == 'SquareFoot' and to == "SquareYard":
	    result = float(val) / 9
    elif frm == 'SquareFoot' and to == "SquareMile":
	    result = float(val) * 0.000000035870064279155
    elif frm == 'SquareFoot' and to == "SquareInch":
	    result = float(val) * 144
    elif frm == 'SquareFoot' and to == "Hectare":
	    result = float(val) / 107639
    elif frm == 'SquareFoot' and to == "Acre":
	    result = float(val) / 43560
    elif frm == 'SquareInch' and to == "SquareKilometer":
	    result = float(val) * 6.4516 * pow(10,-10)
    elif frm == 'SquareInch' and to == "SquareMeter":
	    result = float(val) * 0.00064516
    elif frm == 'SquareInch' and to == "SquareYard":
	    result = float(val) * 0.00077160494
    elif frm == 'SquareInch' and to == "SquareMile":
	    result = float(val) * 2.4909767 * pow(10,-10)
    elif frm == 'SquareInch' and to == "SquareFoot":
	    result = float(val) * 0.0069444444
    elif frm == 'SquareInch' and to == "Hectare":
	    result = float(val) * 6.4516 * pow(10,-8)
    elif frm == 'SquareInch' and to == "Acre":
	    result = float(val) * 1.5942251 * pow(10,-7)
    elif frm == 'Hectare' and to == "SquareKilometer":
	    result = float(val) / 100
    elif frm == 'Hectare' and to == "SquareMeter":
	    result = float(val) / 10000
    elif frm == 'Hectare' and to == "SquareYard":
	    result = float(val) * 11960
    elif frm == 'Hectare' and to == "SquareMile":
	    result = float(val) / 259
    elif frm == 'Hectare' and to == "SquareFoot":
	    result = float(val) * 107639
    elif frm == 'Hectare' and to == "SquareInch":
	    result = float(val) * 15500031
    elif frm == 'Hectare' and to == "Acre":
	    result = float(val) * 2.471
    elif frm == 'Acre' and to == "SquareKilometer":
	    result = float(val) / 247
    elif frm == 'Acre' and to == "SquareMeter":
	    result = float(val) * 4047
    elif frm == 'Acre' and to == "SquareYard":
	    result = float(val) * 4840
    elif frm == 'Acre' and to == "SquareMile":
	    result = float(val) / 640
    elif frm == 'Acre' and to == "SquareFoot":
	    result = float(val) * 43560
    elif frm == 'Acre' and to == "SquareInch":
	    result = float(val) * 6272640
    elif frm == 'Acre' and to == "Hectare":
	    result = float(val) / 2.471
    
    return round(result,10)

def calcEnergy(frm,to,val):
    if frm == 'Joule' and to == "KiloJoule":
    	result = float(val) / 1000
    elif frm == 'Joule' and to == "GramCalorie":
        result = float(val) / 4.184
    elif frm == 'Joule' and to == "KiloCalorie":
        result = float(val) / 4184
    elif frm == 'KiloJoule' and to == "Joule":
        result = float(val) * 1000
    elif frm == 'KiloJoule' and to == "GramCalorie":
        result = float(val) * 239
    elif frm == 'KiloJoule' and to == "KiloCalorie":
        result = float(val) / 4.184
    elif frm == 'GramCalorie' and to == "Joule":
        result = float(val) * 4.184
    elif frm == 'GramCalorie' and to == "KiloJoule":
        result = float(val) / 239
    elif frm == 'GramCalorie' and to == "KiloCalorie":
        result = float(val) / 1000
    elif frm == 'KiloCalorie' and to == "Joule":
        result = float(val) * 4184
    elif frm == 'KiloCalorie' and to == "KiloJoule":
        result = float(val) * 4.184
    elif frm == 'KiloCalorie' and to == "GramCalorie":
        result = float(val) / 1000
    
    return round(result,10)

def calcFrequency(frm,to,val):
    if frm == 'Hertz' and to == "Kilohertz":
        result = float(val) / 1000
    elif frm == 'Hertz' and to == "Megahertz":
        result = float(val) / 1000000
    elif frm == 'Hertz' and to == "Gigahertz":
        result = float(val) / 1000000000
    elif frm == 'Kilohertz' and to == "Hertz":
        result = float(val) * 1000
    elif frm == 'Kilohertz' and to == "Megahertz":
        result = float(val) / 1000
    elif frm == 'Kilohertz' and to == "Gigahertz":
        result = float(val) / 1000000
    elif frm == 'Megahertz' and to == "Hertz":
        result = float(val) / 1000000
    elif frm == 'Megahertz' and to == "Kilohertz":
        result = float(val) * 1000
    elif frm == 'Megahertz' and to == "Gigahertz":
        result = float(val) / 1000
    elif frm == 'Gigahertz' and to == "Hertz":
        result = float(val) / 1000000000
    elif frm == 'Gigahertz' and to == "Kilohertz":
        result = float(val) / 1000000
    elif frm == 'Gigahertz' and to == "Megahertz":
        result = float(val) * 1000
        
        
    return round(result,10)

def calcLength(frm,to,val):
    
    if frm == 'Kilometer' and to == "Meter":
        result = float(val) * 1000
    elif frm == 'Kilometer' and to == "Centimeter":
        result = float(val) * 100000
    elif frm == 'Kilometer' and to == "Millimeter":
        result = float(val) * 1000000
    elif frm == 'Kilometer' and to == "Micrometer":
        result = float(val) * 1000000000
    elif frm == 'Kilometer' and to == "Nanometer":
        result = float(val) * 1000000000000
    elif frm == 'Kilometer' and to == "Mile":
        result = float(val) / 1.609
   
    
    #------
    if frm == 'Meter' and to == "Kilometer":
        result = float(val) / 1000
    elif frm == 'Meter' and to == "Centimeter":
        result = float(val) * 100
    elif frm == 'Meter' and to == "Millimeter":
        result = float(val) * 1000
    elif frm == 'Meter' and to == "Micrometer":
        result = float(val) * 1000000
    elif frm == 'Meter' and to == "Nanometer":
        result = float(val) * 1000000000
    elif frm == 'Meter' and to == "Mile":
        result = float(val) / 1609
    
    #----
    if frm == 'Centimeter' and to == "Kilometer":
        result = float(val) / 100000
    elif frm == 'Centimeter' and to == "Meter":
        result = float(val) / 100
    elif frm == 'Centimeter' and to == "Millimeter":
        result = float(val) * 10
    elif frm == 'Centimeter' and to == "Micrometer":
        result = float(val) * 10000
    elif frm == 'Centimeter' and to == "Nanometer":
        result = float(val) * 10000000
    elif frm == 'Centimeter' and to == "Mile":
        result = float(val) / 160934
    
    
    #----------
    if frm == 'Millimeter' and to == "Kilometer":
        result = float(val) * 0.000001
    elif frm == 'Millimeter' and to == "Meter":
        result = float(val) * 0.001
    elif frm == 'Millimeter' and to == "Centimeter":
        result = float(val) * 0.10
    elif frm == 'Millimeter' and to == "Micrometer":
        result = float(val) * 1000
    elif frm == 'Millimeter' and to == "Nanometer":
        result = float(val) * 1000000
    elif frm == 'Millimeter' and to == "Mile":
        result = float(val) * 0.00000062137
    
    
     #----------
    if frm == 'Micrometer' and to == "Kilometer":
        result = float(val) / 1000000000
    elif frm == 'Micrometer' and to == "Meter":
        result = float(val) / 1000000
    elif frm == 'Micrometer' and to == "Centimeter":
        result = float(val) / 10000
    elif frm == 'Micrometer' and to == "Millimeter":
        result = float(val) / 1000
    elif frm == 'Micrometer' and to == "Nanometer":
        result = float(val) * 1000
    elif frm == 'Micrometer' and to == "Mile":
        result = float(val) * 0.00000000062137
    
    
      #----------
    if frm == 'Nanometer' and to == "Kilometer":
        result = float(val) / 1000000000000
    elif frm == 'Nanometer' and to == "Meter":
        result = float(val) / 1000000000
    elif frm == 'Nanometer' and to == "Centimeter":
        result = float(val) / 10000000
    elif frm == 'Nanometer' and to == "Millimeter":
        result = float(val) / 1000000
    elif frm == 'Nanometer' and to == "Micrometer":
        result = float(val) / 1000
    elif frm == 'Nanometer' and to == "Mile":
        result = float(val) * 1/1609344000000
    
    
      #----------
    if frm == 'Mile' and to == "Kilometer":
        result = float(val) * 1.609
    elif frm == 'Mile' and to == "Meter":
        result = float(val) * 1609
    elif frm == 'Mile' and to == "Centimeter":
        result = float(val) * 160934
    elif frm == 'Mile' and to == "Millimeter":
        result = float(val) * 1609344
    elif frm == 'Mile' and to == "Micrometer":
        result = float(val) * 1609344000
    elif frm == 'Mile' and to == "Nanometer":
        result = float(val) * 1609344000000
   
        
    return round(result,10)

def calcMass(frm,to,val):
    if frm == 'Tonne' and to == "Kilogram":
        result = float(val) * 1000
    elif frm == 'Tonne' and to == "Gram":
        result = float(val) * 1000000
    elif frm == 'Tonne' and to == "Pound":
        result = float(val) * 2205
    elif frm == 'Kilogram' and to == "Tonne":
        result = float(val) / 1000
    elif frm == 'Kilogram' and to == "Gram":
        result = float(val) * 1000
    elif frm == 'Kilogram' and to == "Pound":
        result = float(val) * 2.205
    elif frm == 'Gram' and to == "Tonne":
        result = float(val) / 1000000
    elif frm == 'Gram' and to == "Kilogram":
        result = float(val) / 1000
    elif frm == 'Gram' and to == "Pound":
        result = float(val) / 454
    elif frm == 'Pound' and to == "Tonne":
        result = float(val) / 2205
    elif frm == 'Pound' and to == "Kilogram":
        result = float(val) / 2.205
    elif frm == 'Pound' and to == "Gram":
        result = float(val) * 454
    
    return round(result,10)

def calcPressure(frm,to,val):
    if frm == 'Bar' and to == "Pascal":
        result = float(val) * 100000
    elif frm == 'Pascal' and to == "Bar":
        result = float(val) * 454
    return round(result,10)

def calcSpeed(frm,to,val):
    if frm == 'MilesPerHour' and to == "MeterPerSecond":
        result = float(val) / 2.237
    elif frm == 'MilesPerHour' and to == "KilometerPerHour":
        result = float(val) * 1.607
    elif frm == 'MeterPerSecond' and to == "MilesPerHour":
        result = float(val) * 2.237
    elif frm == 'MeterPerSecond' and to == "KilometerPerHour":
        result = float(val) * 3.6
    elif frm == 'KilometerPerHour' and to == "MilesPerHour":
        result = float(val) / 1.609
    elif frm == 'KilometerPerHour' and to == "MeterPerSecond":
        result = float(val) / 3.6
    return round(result,10)

def calcTemperature(frm,to,val):
    if frm == 'Celcius' and to == "Farhenheit":
        result = (float(val) * 9/5) + 32
    elif frm == 'Celcius' and to == "Kelvin":
        result = float(val) + 273.15
    elif frm == 'Farhenheit' and to == "Celcius":
        result = (float(val) - 32) * 5/9
    elif frm == 'Farhenheit' and to == "Kelvin":
        result = (float(val) - 32) * 5/9 + 273.15
    elif frm == 'Kelvin' and to == "Farhenheit":
        result = (float(val) - 273.15) * 9/5 + 32
    elif frm == 'Kelvin' and to == "Celcius":
        result = float(val) - 273.15
    
    return round(result,10)

def calculateValue(arg,f,t,v):
    """This method here is responsible for calculating the conversions and producing a result."""
    switcher = {
               "Area":lambda:calcArea(f,t,v),
               "Energy":lambda:calcEnergy(f,t,v),
               "Frequency":lambda:calcFrequency(f,t,v),
               "Length":lambda:calcLength(f,t,v),
               "Mass":lambda:calcMass(f,t,v),
               "Pressure":lambda:calcPressure(f,t,v),
               "Speed":lambda:calcSpeed(f,t,v),
               "Temperature":lambda:calcTemperature(f,t,v)
               }
    func = switcher.get(arg,lambda :'Invalid')
    resText = str(v) +' '+ str(f)+ " after conversion becomes " + str(func()) +' '+ str(t)+'s.'
    result_Window.delete(1.0,'end')
    result_Window.insert(1.0,resText)

# Lists and Sub-lists creation 

listOfUnits = {"Area":['SquareKilometer','SquareMeter','SquareMile','SquareYard','SquareFoot','SquareInch','Hectare','Acre'],
            "Energy":['Joule','KiloJoule','GramCalorie','KiloCalorie'],
            "Frequency":['Hertz','Kilohertz','Megahertz','Gigahertz'],
            "Length":['Kilometer','Meter','Centimeter','Millimeter','Micrometer','Nanometer','Mile'],
            "Mass":['Tonne','Kilogram','Gram','Pound'],
            "Pressure":['Bar','Pascal'],
            "Speed":['MilesPerHour','MeterPerSecond','KilometerPerHour'],
            "Temperature":['Celcius','Farhenheit','Kelvin']
           }

# label text for header title
headerLbl = tk.Label(root,text="UNIT CONVERTER",bg='wheat1',fg="black",font = ("Times New Roman", 30,"bold","underline"))
headerLbl.grid(row = 0,column = 1,columnspan = 3)

# Label text for conversion tye selection 
lbl1 = tk.Label(root,text="Conversion Type:",bg='wheat1')
lbl1.grid(row = 1,column = 0,padx=20,pady=20)


# OptionMenu creation for the list of Units to select
global x 
x = tk.StringVar()
x.set(list(listOfUnits.keys())[0])
unitList = tk.OptionMenu(root,x,*listOfUnits.keys(),command=updateSubLists)
unitList.grid(row = 1,column = 1,padx=20,pady=40)

# Label text for conversion type selection 
lbl2 = tk.Label(root,text="From",bg='wheat1')
lbl2.grid(row = 2,column = 0)


# OptionMenu creation for the list of Sub Units to select.
global y 
y = tk.StringVar()
y.set('Please select an option')
subUnitListFrom = tk.OptionMenu(root,y,*listOfUnits.get(x.get()))
subUnitListFrom.grid(row=2,column=1,padx=20,pady=40)


# Entry widget for From label
global fromVar
fromVar = tk.StringVar()
fromEntry = tk.Entry(root,width=20,textvariable=fromVar)
valid_info = root.register(validateUserInput)   # register the function for the validation
fromEntry.config(validate="key",validatecommand=(valid_info,'%P'))  # Adding the properties for validation elements
fromEntry.grid(row=2,column=2)

# Label text for conversion type selection 
lbl3 = tk.Label(root,text="To",bg='wheat1')
lbl3.grid(row = 3,column = 0)

# OptionMenu creation for the list of Sub Units to select.
global z 
z = tk.StringVar()
z.set('Please select an option')
subUnitListTo = tk.OptionMenu(root,z,*listOfUnits.get(x.get()))
subUnitListTo.grid(row=3,column=1)

# Text widget to show the result
global result_Window
result_Window = tk.Text(root,fg='black',bg='snow',width=50,height=5,font=("Arial",10))
result_Window.grid(row=5,column=1,columnspan=3)


# Logic for the convert button
convert_button = tk.Button(root,text="CONVERT",fg="black",bg ="yellow",font=("Times New Roman",12,"bold"),command=lambda:calculateValue(x.get(),y.get(),z.get(),fromVar.get()))
convert_button.grid(row=4,column=1,padx=20,pady=40)

# Logic for the reset button
reset_button = tk.Button(root,text="RESET",fg="black",bg="yellow",font=("Times New Roman",12,"bold"),command=resetEntries)
reset_button.grid(row=4,column=2,padx=20,pady=40)

root.mainloop()
