#import datetime module
import datetime
from tkinter import *
from tkinter import messagebox
#calculations
def setFullAge(y,m,d):
    fullDay.set(str(d))
    fullMonth.set(str(m))
    fullYear.set(str(y))


def calculateAge():
    #get the current date
    currentdate = datetime.datetime.now()
    #take input
    birthday = inputfield.get()
    try:
        birthdayDate=datetime.datetime.strptime(birthday,'%d-%m-%Y')
    except:
        setFullAge(0,0,0)
        messagebox.showerror("Error","Wrong Value of Birthday")
        return
    nextBirthday = str(birthdayDate.day)+'-'+str(birthdayDate.month)+'-'+str(currentdate.year+1)
    nextBirthdayDate=datetime.datetime.strptime(nextBirthday,'%d-%m-%Y')

    #calculate years
    years = (currentdate-birthdayDate).total_seconds()/3600/24/365.242
    yearsInt = int(years)

    #calculate months
    months = (years-yearsInt)*12
    monthsInt = int(months)

    #calculate days
    days = (months-monthsInt)*(365.242/12)
    daysInt = int(days)

    # #outputs 
    setFullAge(yearsInt,monthsInt,daysInt)

#default window size
HEIGHT = 350
WIDTH = 600

#init the tkinter
root = Tk()
root.title("Age Calculator")

#init the canvas
canvas = Canvas(root,width = WIDTH, height = HEIGHT)
canvas.pack()

#setup frontend
#set frame
frame = Frame(root,bg="#ececec")
frame.place(relheight=1,relwidth=1,relx=0,rely=0)
#set heading
headingLabel = Label(frame,text="Your Details",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel.pack(fill = X, expand =False, ipady = 18)
#set inputlabel
inputLabel = Label(frame,text="Enter Your Date Of Birth (dd-MM-yyyy) :",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel.place(relheight=.05,relwidth=.55,relx=.06,rely=.22)
#set input
inputfield = StringVar()
myInput = Entry(frame,font = 'AppleGothic 16 italic',textvariable = inputfield,bg="#fcfcfc",fg="#000000")
myInput.place(relheight = .10,relwidth=.30,relx=.62,rely=.20)
#calculateAge button
calculateButton = Button(frame,text="Calculate Age",font = 'AppleGothic 16',bg="#ffffff",fg="red",activebackground="#ffffff",command=calculateAge)
calculateButton.place(relheight=.12,relwidth=.25,relx=.375,rely=.37)

headingLabel1 = Label(frame,text="Your Age",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel1.place(relx=.41,rely=.52)

#output screen
textAgeLabel=Label(frame,textvariable="fullAge",text="You are : ",bg="#ececec",fg="#000000",font='AppleGothic 16')
textAgeLabel.place(relheight=.05,relwidth=.15,relx=.14,rely=.70)



#for years
fullYear=StringVar()
fullYearOutput = Label(frame,textvariable =fullYear,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullYearOutput.place(relheight=.05,relwidth=.06,relx=.27,rely=.70)
fullYearText=Label(frame,text="Years",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullYearText.place(relheight=.05,relwidth=.1,relx=.33,rely=.70)



#for month
fullMonth=StringVar()
fullMonthOutput = Label(frame,textvariable =fullMonth,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullMonthOutput.place(relheight=.05,relwidth=.05,relx=.43,rely=.70)
fullMonthText=Label(frame,text="Months",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullMonthText.place(relheight=.05,relwidth=.13,relx=.48,rely=.70)



#for days
fullDay=StringVar()
fullDayOutput = Label(frame,textvariable =fullDay,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullDayOutput.place(relheight=.05,relwidth=.05,relx=.61,rely=.70)
fullDayText=Label(frame,text="Days   Old",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullDayText.place(relheight=.05,relwidth=.15,relx=.69,rely=.70)
#set default value
setFullAge(0,0,0)



#copyright text
copyrightText = Label(frame,text = "Developed By Group 3",bg="#ececec",fg="#000000",font='AppleGothic 12')
copyrightText2=Label(frame,text="Teacher's Name : Joyjit Patra, Department - CSE(B), BCET, 2019",bg="#ececec",fg="#000000",font='AppleGothic 12')
copyrightText.place(relx=.09,rely=.85,relwidth=.8,relheight=.1)
copyrightText2.place(relx=.09,rely=.93,relwidth=.8,relheight=.05)


root.mainloop()