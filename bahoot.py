
import tkinter as tk
import time 
from tkinter import Radiobutton, scrolledtext
score = 0

mainwindow = tk.Tk()
mainwindow.title("Multi-window demo code - 3")
mainwindow.geometry("600x500")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)

def showFirstQuestion():
    Q1.tkraise()


# bottom Frame ----------------------------------------------------
bottom_frame = tk.Frame(mainwindow, bg="yellow", padx=5, pady=5)
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)


# Red frame(first question) ----------------------------------------------------

Q1 = tk.Frame(bottom_frame, bg="yellow", padx=5, pady=5)
Q1.place(x=0, y=0, relwidth=1.0, relheight=1.0)


#creating functions that will be used when a button is pressed

label_1 = tk.Label(Q1, text="Question One")
label_1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other_label = tk.Label(Q1, text="What is the average hieght of a Giraffe?")
other_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer1=tk.IntVar()

#The answers 
my_radio_1 = tk.Radiobutton(Q1,text="18 FT",variable=answer1,value=1)
my_radio_1.grid(row=6, column=5,padx=(6),pady=12)

my_radio_2 = tk.Radiobutton(Q1, text="2 FT",variable=answer1,value=3)
my_radio_2.grid(row=7, column=5,padx=(7),pady=12)

my_radio_3 = tk.Radiobutton(Q1, text="16.4 FT",variable=answer1,value=2)
my_radio_3.grid(row=8, column=5,padx=(8),pady=12)

my_radio_4 = tk.Radiobutton(Q1,text="20 FT",variable=answer1,value=4)
my_radio_4.grid(row=9, column=5,padx=(9),pady=12)

def Q2():
    result1=answer1.get()
    if result1!=2:
        Q1.configure(bg="red")
    if result1==2:
        Q1.configure(bg="green")
        global score
        score += 1
        print(score)
    Q1.update()
    Q1.after(1000,Q2.tkraise())

NextButt = tk.Button(Q1, text="Next Question",command=Q2)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# green Frame (second Question)----------------------------------------------------

Q2 = tk.Frame(bottom_frame, bg="black", padx=5, pady=5)
Q2.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_2 =tk.Label(Q2,text="Question Two")
label_2.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other2_label = tk.Label(Q2, text="When did the American Revolution begin?")
other2_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer2=tk.IntVar()

#The answers 
myRadio1_Q2 = tk.Radiobutton(Q2,text="Mar 13, 1756",variable=answer2,value=1)
myRadio1_Q2.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q2 = tk.Radiobutton(Q2, text="Feb 4, 2002",variable=answer2,value=3)
myRadio2_Q2.grid(row=7, column=5,padx=(7),pady=12)

myRadio3_Q2 = tk.Radiobutton(Q2, text="Jan 4, 1864",variable=answer2,value=4)
myRadio3_Q2.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q2 = tk.Radiobutton(Q2,text="Mar 22, 1765",variable=answer2,value=2)
myRadio4_Q2.grid(row=9, column=5,padx=(9),pady=12)

def Q3():
    result2=answer2.get()
    if result2!=2:
        Q2.configure(bg="red")
    if result2==2:
        Q2.configure(bg="green")
        global score
        score += 1
        print(score)
    Q2.update()
    Q2.after(1000,Q3.tkraise())

NextButt = tk.Button(Q2, text="Next Question", command=Q3)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#blue Frame (third Question) ----------------------------------------------------
Q3 = tk.Frame(bottom_frame, bg="blue", padx=5, pady=5)
Q3.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_3 = tk.Label(Q3, text="Question Three")
label_3.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other3_label = tk.Label(Q3, text="Who is the highest paid actor?")
other3_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer3=tk.IntVar()

#The answers 
myRadio1_Q3 = tk.Radiobutton(Q3,text="Dwayne “The Rock” Johnson",variable=answer3,value=2)
myRadio1_Q3.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q3 = tk.Radiobutton(Q3, text="Shah Rukh Khan",variable=answer3,value=1)
myRadio2_Q3.grid(row=7, column=5,padx=(7),pady=12)

myRadio3_Q3 = tk.Radiobutton(Q3, text="Tom Cruise",variable=answer3,value=3)
myRadio3_Q3.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q3 = tk.Radiobutton(Q3,text="Daniel Craig",variable=answer3,value=4)
myRadio4_Q3.grid(row=9, column=5,padx=(9),pady=12)

def Q4():
    result3=answer3.get()
    if result3!=2:
        Q3.configure(bg="red")
    if result3==2:
        Q3.configure(bg="green")
        global score
        score += 1
        print(score)
    Q3.update()
    Q3.after(1000,Q4.tkraise())
    
NextButt = tk.Button(Q3, text="Next Question",command=Q4)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#Yellow frame(Fourth Question)--------------------------------------

Q4 = tk.Frame(bottom_frame, bg="yellow", padx=5, pady=5)
Q4.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_4 = tk.Label(Q4, text="Question Four")
label_4.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other4_label = tk.Label(Q4, text="Who is the funniest actor?")
other4_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer4=tk.IntVar()

#The answers 
myRadio1_Q4 = tk.Radiobutton(Q4,text="Jack Black",variable=answer4,value=1)
myRadio1_Q4.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q4 = tk.Radiobutton(Q4, text="Ryan Reynolds",variable=answer4,value=2)
myRadio2_Q4.grid(row=7, column=5,padx=(7),pady=12)

myRadio3_Q4 = tk.Radiobutton(Q4, text="Kevin Hart",variable=answer4,value=3)
myRadio3_Q4.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q4 = tk.Radiobutton(Q4,text="Chris Evans",variable=answer4,value=4)
myRadio4_Q4.grid(row=9, column=5,padx=(9),pady=12)

def Q5():
    result4=answer4.get()
    if result4!=2:
        Q4.configure(bg="red")
    if result4==2:
        Q4.configure(bg="green")
        global score
        score += 1
        print(score)
    Q4.update()
    Q4.after(1000,Q5.tkraise())

    
NextButt = tk.Button(Q4, text="Next Question",command=Q5)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#Pink frame (Fifth Question)--------------------------------------------------

Q5 = tk.Frame(bottom_frame, bg="pink", padx=5, pady=5)
Q5.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_5 = tk.Label(Q5, text="Question Five")
label_5.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other5_label = tk.Label(Q5, text="Where is Mount Everest")
other5_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer5=tk.IntVar()

#The answers 
myRadio1_Q5 = tk.Radiobutton(Q5,text="Russia",variable=answer5,value=1)
myRadio1_Q5.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q5 = tk.Radiobutton(Q5, text="China",variable=answer5,value=3)
myRadio2_Q5.grid(row=7, column=5,padx=(7),pady=12)

myRadio3_Q5 = tk.Radiobutton(Q5, text="India",variable=answer5,value=4)
myRadio3_Q5.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q5 = tk.Radiobutton(Q5,text="Nepal",variable=answer5,value=2)
myRadio4_Q5.grid(row=9, column=5,padx=(9),pady=12)

def Q6():
    result5=answer5.get()
    if result5!=2:
        Q5.configure(bg="red")
    if result5==2:
        Q5.configure(bg="green")
        global score
        score += 1
        print(score)
    Q5.update()
    Q5.after(1000,Q6.tkraise())
    
NextButt = tk.Button(Q5, text="Next Question",command=Q6)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


Q6 = tk.Frame(bottom_frame, bg="purple", padx=5, pady=5)
Q6.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_6 = tk.Label(Q6, text="Question Six")
label_6.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other6_label = tk.Label(Q6, text="What’s the shortcut for the “copy” function on most computers?")
other6_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer6=tk.IntVar()

#The answers 
myRadio1_Q6 = tk.Radiobutton(Q6,text="Ctrl V",variable=answer6,value=1)
myRadio1_Q6.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q6 = tk.Radiobutton(Q6, text="Ctrl C ",variable=answer6,value=2)
myRadio2_Q6.grid(row=7, column=5,padx=(8),pady=13)

myRadio3_Q6 = tk.Radiobutton(Q6, text="Ctrl X",variable=answer6,value=4)
myRadio3_Q6.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q6 = tk.Radiobutton(Q6,text="Ctrl P",variable=answer6,value=3)
myRadio4_Q6.grid(row=9, column=5,padx=(9),pady=12)

def Q7():
    result6=answer6.get()
    if result6!=2:
        Q6.configure(bg="red")
    if result6==2:
        Q6.configure(bg="green")
        global score
        score += 1
        print(score)
    Q6.update()
    Q6.after(1000,Q7.tkraise())
    
NextButt = tk.Button(Q6, text="Next Question",command=Q7)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#Cyan ( Quesiton 7)---------------------------------------

Q7 = tk.Frame(bottom_frame, bg="cyan", padx=5, pady=5)
Q7.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_7 = tk.Label(Q7, text="Question Seven")
label_7.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other7_label = tk.Label(Q7, text="Which planet is the hottest in our solar system?")
other7_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer7=tk.IntVar()

#The answers 
myRadio1_Q7 = tk.Radiobutton(Q7,text="Venus",variable=answer7,value=2)
myRadio1_Q7.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q7 = tk.Radiobutton(Q7, text="Earth",variable=answer7,value=1)
myRadio2_Q7.grid(row=7, column=5,padx=(8),pady=13)

myRadio3_Q7 = tk.Radiobutton(Q7, text="Saturn",variable=answer7,value=3)
myRadio3_Q7.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q7 = tk.Radiobutton(Q7,text="Pluto",variable=answer7,value=4)
myRadio4_Q7.grid(row=9, column=5,padx=(9),pady=12)

def Q8():
    result7=answer7.get()
    if result7!=2:
        Q7.configure(bg="red")
    if result7==2:
        Q7.configure(bg="green")
        global score
        score += 1
        print(score)
    Q7.update()
    Q7.after(1000,Q8.tkraise())
    
NextButt = tk.Button(Q7, text="Next Question",command=Q8)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# dark violet ( Question 8)-----------------------------------

Q8 = tk.Frame(bottom_frame, bg="dark violet", padx=5, pady=5)
Q8.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_8 = tk.Label(Q8, text="Question Eight")
label_8.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other8_label = tk.Label(Q8, text="Which cartoon character lives in a pineapple under the sea?")
other8_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer8=tk.IntVar()

#The answers 
myRadio1_Q8 = tk.Radiobutton(Q8,text="Sally",variable=answer8,value=1)
myRadio1_Q8.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q8 = tk.Radiobutton(Q8, text="Bob",variable=answer8,value=3)
myRadio2_Q8.grid(row=7, column=5,padx=(8),pady=13)

myRadio3_Q8 = tk.Radiobutton(Q8, text="Mr.Crabs",variable=answer8,value=4)
myRadio3_Q8.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q8 = tk.Radiobutton(Q8,text="Spongebob Squarepants",variable=answer8,value=2)
myRadio4_Q8.grid(row=9, column=5,padx=(9),pady=12)

def Q9():
    result8=answer8.get()
    if result8!=2:
        Q8.configure(bg="red")
    if result8==2:
        Q8.configure(bg="green")
        global score
        score += 1
        print(score)
    Q8.update()
    Q8.after(1000,Q9.tkraise())
    
NextButt = tk.Button(Q8, text="Next Question",command=Q9)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Brown (Question 9)---------------------------------------

Q9 = tk.Frame(bottom_frame, bg="Brown", padx=5, pady=5)
Q9.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_9 = tk.Label(Q9, text="Question Nine")
label_9.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other9_label = tk.Label(Q9, text="Which auto brand was the first to offer seat belts?")
other9_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer9=tk.IntVar()

#The answers 
myRadio1_Q9 = tk.Radiobutton(Q9,text="Toyota",variable=answer9,value=1)
myRadio1_Q9.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q9 = tk.Radiobutton(Q9, text="Nash Motors",variable=answer9,value=2)
myRadio2_Q9.grid(row=7, column=5,padx=(8),pady=13)

myRadio3_Q9 = tk.Radiobutton(Q9, text="Ford",variable=answer9,value=3)
myRadio3_Q9.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q9 = tk.Radiobutton(Q9,text="Tesla",variable=answer9,value=4)
myRadio4_Q9.grid(row=9, column=5,padx=(9),pady=12)

def Q10():
    result9=answer9.get()
    if result9!=2:
        Q9.configure(bg="red")
    if result9==2:
        Q9.configure(bg="green")
        global score
        score += 1
        print(score)
    Q9.update()
    Q9.after(1000,Q10.tkraise())
    
NextButt = tk.Button(Q9, text="Next Question",command=Q10)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# OrangeRed3 (Question 10)--------------------------------------

Q10 = tk.Frame(bottom_frame, bg="OrangeRed3", padx=5, pady=5)
Q10.place(x=0, y=0, relwidth=1.0, relheight=1.0)


label_10 = tk.Label(Q10, text="Question Ten")
label_10.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

other10_label = tk.Label(Q10, text="What percentage of our bodies is made up of water?")
other10_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

answer10=tk.IntVar()

#The answers 
myRadio1_Q10 = tk.Radiobutton(Q10,text="15%",variable=answer10,value=1)
myRadio1_Q10.grid(row=6, column=5,padx=(6),pady=12)

myRadio2_Q10 = tk.Radiobutton(Q10, text="60-65%",variable=answer10,value=2)
myRadio2_Q10.grid(row=7, column=5,padx=(8),pady=13)

myRadio3_Q10 = tk.Radiobutton(Q10, text="75%",variable=answer10,value=3)
myRadio3_Q10.grid(row=8, column=5,padx=(8),pady=12)

myRadio4_Q10 = tk.Radiobutton(Q10,text="30%",variable=answer10,value=4)
myRadio4_Q10.grid(row=9, column=5,padx=(9),pady=12)

# End Screen-------------------------------------------------------
endscreen = tk.Frame(bottom_frame, bg="green", padx=5, pady=5)
endscreen.place(x=0, y=0, relwidth=1.0, relheight=1.0)

finishLabel = tk.Label(endscreen, text="You Finished! Your Score is: " + str(score) + "/10", font=('arial', 20))
finishLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

def changeScore():
    global score
    finishLabel.config(text="You Finished! Your Score is: " + str(score) + "/10", font=('arial, 20'))

finalscore = score
# Finish Button
def finish():
    global score
    result10=answer10.get()
    if result10!=2:
        Q10.configure(bg="red")
        changeScore()
    if result10==2:
        Q10.configure(bg="green")
        score += 1
        changeScore()
        print(score)
    Q10.update()
    Q10.after(1000,endscreen.tkraise())

NextButt = tk.Button(Q10, text="FINISH!",command=finish)
NextButt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# HOME FRAME------------------------------------------------------
blueFrame = tk.Frame(bottom_frame, bg="blue", padx=5, pady=5)
blueFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)


my_tkVar = tk.IntVar()

# sets which button will be selected by default
my_tkVar.set(2)

def doButt():
    Q1.tkraise()

L1 = tk.Label(blueFrame, text="Bahoot!", font=('arial', 20))
L1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

#placing the radio buttons in the center

B1 = tk.Button(blueFrame, text="Start Game", command=doButt)
B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

blueFrame.tkraise()




mainwindow.mainloop()
