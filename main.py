from tkinter import *
from tkinter import StringVar
import os
import time


root = Tk()
root.title('Numerical Analysis Calculator')
root.iconbitmap('C:/Users/User/PycharmProjects/Trial 2/logo.ico')  #Change This according to your logo directory
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.grid_columnconfigure(0, weight=1)

options = ["Bisection Method",  # 0 1
           "Newton Raphson Method",  # 1 2
           "False Position Method",  # 2 3
           "Secant Method",  # 3 4
           "Fixed Point Iteration Method"] # 5
elapsed_time=0
x0=0
x1=0

global x2
def instruct():
    response = Toplevel()
    response.title('Instructions')
    lable = Label(response, text="Instructions:"
                                       "\n1. Use the calculator or keyboard to type in"
                                       "\n your equation  with the following legend:"
                                       "\n"
                                       "\n'**' \t= pow\n'cos()'\t= cos\n'sin()'\t= sin\n'E'\t= Exponential/Exp\n(+, -, *, /) = Math Symbol"
                                        "\n\n2. If showing errors in table, click restart."
                                        "\n\n3. For Fixed Point Iteration Method, type using g(f)."
                                        "\n\nNOTE: PROGRAM GETS ERROR IF USING WRONG SYMBOL!"
                                        "\n\nEnjoy!!"
                        ,font=("Courier", 10), bg="#b9dbfa", bd=5, justify="left").grid(row=0, sticky=E)


def window1():
    def button_click(char_):
        temp = myEntry.get()
        myEntry.delete(0, END)
        myEntry.insert(0, temp + char_)

    def clear():
        myEntry.delete(0, END)

    #***************Frame 1- Calculator*************************

    Frame1= LabelFrame(root,bg="#b9dbfa", padx=10, pady=10)
    Frame1.grid(row=1, sticky= NS, padx=5, pady=5)
    Frame1.rowconfigure(0, weight=1)
    group_num=Label(Frame1,text="Project in Numerical Analysis\nGroup 8", width=42, font=("Courier", 10), fg="Blue", relief="groove").grid(row=0, column=0, columnspan=5)
    intructions= Button(Frame1, text="Instructions", fg="White", bg="Blue", command=instruct, font=("helvetica",8)).grid(row=1, column=0)

    myEntry=Entry(Frame1,font=("Courier", 9), width=38,borderwidth=5 )
    myEntry.grid(row=1, column=1, columnspan=4)


    #Define Buttons
    button_1=Button(Frame1, text= "1", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("1")).grid(row=2, column=0)
    button_2=Button(Frame1, text= "2", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("2")).grid(row=2, column=1)
    button_3=Button(Frame1, text= "3", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("3")).grid(row=2, column=2)

    button_5=Button(Frame1, text= "5", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("5")).grid(row=3, column=1)
    button_6=Button(Frame1, text= "6", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("6")).grid(row=3, column=2)

    button_4=Button(Frame1, text= "4", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("4")).grid(row=3, column=0)
    button_7=Button(Frame1, text= "7", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("7")).grid(row=4, column=0)
    button_8=Button(Frame1, text= "8", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("8")).grid(row=4, column=1)
    button_9=Button(Frame1, text= "9", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("9")).grid(row=4, column=2)

    button_point=Button(Frame1, text= ".", bg="#006dcc", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click(".")).grid(row=5, column=0)
    button_0=Button(Frame1, text= "0", bg="#3a9af0", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("0")).grid(row=5, column=1)
    button_x=Button(Frame1, text= "X", bg="#006dcc", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("x")).grid(row=5, column=2)

    button_plus=Button(Frame1, text= "+", bg="#006dcc", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("+")).grid(row=2, column=3)
    button_minus=Button(Frame1, text= "-", bg="#006dcc", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("-")).grid(row=3, column=3)
    button_times=Button(Frame1, text= "*", bg="#006dcc", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("*")).grid(row=4, column=3)
    button_divide=Button(Frame1, text= "/", bg="#006dcc", font=("Courier", 15), padx=20, pady=10, command=lambda: button_click("/")).grid(row=5, column=3)

    button_sin=Button(Frame1, text= "sin", bg="#006dcc", font=("arial", 10), padx=19, pady=16, command=lambda: button_click("sin(")).grid(row=2, column=4)
    button_cos=Button(Frame1, text= "cos", bg="#006dcc", font=("Arial", 10), padx=17, pady=15, command=lambda: button_click("cos(")).grid(row=3, column=4)
    button_pow=Button(Frame1, text= "pow", bg="#006dcc", font=("arial", 10), padx=17, pady=15, command=lambda: button_click("**")).grid(row=4, column=4)
    button_exp=Button(Frame1, text= "exp", bg="#006dcc", font=("arial", 10), padx=18, pady=16, command=lambda: button_click("E")).grid(row=5, column=4)

    leftbrace = Button(Frame1, text="(", bg="#006dcc", font=("Courier", 15), padx=20, pady=10,
                        command=lambda: button_click("(")).grid(row=6, column=0)
    rightbrace = Button(Frame1, text=")", bg="#006dcc", font=("Courier", 15), padx=20, pady=10,
                        command=lambda: button_click(")")).grid(row=6, column=1)
    button_clear = Button(Frame1, text="CLEAR", bg="#006dcc", font=("Courier", 15), padx=65, pady=10,
                        command=clear).grid(row=6, column=2, columnspan=3)

    Label1=Label(Frame1,text="Define Method", bg="#b9dbfa",font=("Courier", 10)).grid(row=7, column=0, columnspan=2)
    Label2=Label(Frame1,text="Tolerance", bg="#b9dbfa",font=("Courier", 10)).grid(row=8, column=0, columnspan=2)
    Label3=Label(Frame1,text="Iterations", bg="#b9dbfa",font=("Courier", 10)).grid(row=9, column=0, columnspan=2)

    #**************Choose Method************************

    choice= StringVar()
    choice.set('Bisection Method')
    choices = OptionMenu(Frame1, choice, "Bisection Method",  # 0 1
                                        "Newton Raphson Method",  # 1 2
                                       "False Position Method",  # 2 3
                                      "Secant Method",  # 3 4
                                     "Fixed Point Iteration Method")
    choices.grid(row=7, column=2, columnspan=3)

    tolerance =Entry(Frame1,font=("Courier", 11), width=19,borderwidth=5)
    tolerance.grid(row=8, column=2, columnspan=3)
    iterations =Entry(Frame1,font=("Courier", 11), width=19,borderwidth=5 )
    iterations.grid(row=9, column=2, columnspan=3)

    Show_Results=Button(Frame1, text= "Show Results", bg="#006dcc", font=("Courier", 11), padx=40, command=lambda : Submit(choice.get(), myEntry.get(), tolerance.get(), iterations.get()))
    Show_Results.grid(row=10, column=0, columnspan=5)


    #************************************** End of Frame1 Calculator***********************************

def Submit(choice, myEntry, t, i):

    if choice == options[0]:
        Window1_Ext(1, myEntry, t, i)
    elif choice == options[1]:
        Window1_Ext(2, myEntry, t, i)
    elif choice == options[2]:
        Window1_Ext(3, myEntry, t, i)
    elif choice == options[3]:
        Window1_Ext(4, myEntry, t, i)
    elif choice == options[4]:
        Window1_Ext(5, myEntry, t, i)

def Window1_Ext( type, myEntry, tolerance, iterations):

    Frame2 = LabelFrame(root, bg="#b9dbfa", padx=59, pady=1)
    Frame2.grid(row=2,  sticky= NS,padx=5, pady=5)

    #*************************Frame 2- Input A&B *********************************
    if type == 1 or type == 3 or type == 4:

        Label4=Label(Frame2,text="Add Initial Guess/es", bg="#b9dbfa",font=("Courier", 10)).grid(row=0, column=0, columnspan=3)
        Label5=Label(Frame2,text="Input 'a'", bg="#b9dbfa",font=("Courier", 10)).grid(row=1, column=0)
        Label6=Label(Frame2,text="Input 'b'", bg="#b9dbfa",font=("Courier", 10)).grid(row=2, column=0)

        guess_1=Entry(Frame2,font=("Courier", 11), width=10,borderwidth=5)
        guess_1.grid(row=1, column=1)
        guess_2=Entry(Frame2,font=("Courier", 11), width=10,borderwidth=5 )
        guess_2.grid(row=2, column=1)
        if type ==1:
            button_ok = Button(Frame2, text="OKAY", bg="#006dcc", font=("Courier", 11), command= lambda :bisection_(Frame2, type, myEntry, tolerance, iterations, guess_1.get(), guess_2.get()))
            button_ok.grid(padx=15, row=1, column=2,rowspan=2)
        elif type == 3:
            button_ok = Button(Frame2, text="OKAY", bg="#006dcc", font=("Courier", 11), command= lambda :falsepos_(Frame2,type, myEntry, tolerance, iterations, guess_1.get(), guess_2.get()))
            button_ok.grid(padx=15, row=1, column=2,rowspan=2)
        elif type == 4:
            button_ok = Button(Frame2, text="OKAY", bg="#006dcc", font=("Courier", 11), command= lambda : secant_(Frame2,type, myEntry, tolerance, iterations, guess_1.get(), guess_2.get()))
            button_ok.grid(padx=15, row=1, column=2,rowspan=2)

    elif type==2 or type==5:
        Label4=Label(Frame2,text="Add Initial Guess/es", bg="#b9dbfa",font=("Courier", 10)).grid(row=0, column=0, columnspan=3)
        Label5=Label(Frame2,text="Input 'a'", bg="#b9dbfa",font=("Courier", 10)).grid(row=1, column=0)
        guess_1=Entry(Frame2,font=("Courier", 11), width=10,borderwidth=5)
        guess_1.grid(row=1, column=1)
        if type ==2:
            button_ok = Button(Frame2, text="OKAY", bg="#006dcc", font=("Courier", 11), command= lambda :newton_(Frame2,type, myEntry, tolerance, iterations, guess_1.get()))
            button_ok.grid(padx=15, row=1, column=2,rowspan=2)
        elif type ==5:
            button_ok = Button(Frame2, text="OKAY", bg="#006dcc", font=("Courier", 11), command= lambda :fixedpos_(Frame2,type, myEntry, tolerance, iterations, guess_1.get()))
            button_ok.grid(padx=15, row=1, column=2,rowspan=2)


        #************************************** End of Frame2 Calculator***********************************

import BisectionMethod
import falseposition
import secant
import NewtonRaphson
import fixedpoint

def bisection_(Frame2, type, myEntry, tolerance, iterations, guess_1, guess_2):
    imax = 50
    ea = 0.00001
    global elapsed_time
    global x0
    x0 = float(guess_1)
    global x1
    x1 = float(guess_2)
    if tolerance != '':
        ea = float(tolerance)
    if iterations != '':
        imax = int(iterations)

    start = time.perf_counter()
    BisectionMethod.body(myEntry, float(guess_1), float(guess_2), float(tolerance), float(iterations))
    end = time.perf_counter()
    elapsed_time = end - start
    print(elapsed_time)

    window2(Frame2, type)

def newton_(Frame2,type, myEntry, tolerance, iterations, guess_1):
    imax = 50
    ea = 0.00001
    global elapsed_time
    global x0
    x0 = float(guess_1)
    if tolerance != '':
        ea = float(tolerance)
    if iterations != '':
        imax = int(iterations)

    start = time.perf_counter()
    NewtonRaphson.body(myEntry, float(guess_1),  float(tolerance), float(iterations))
    end = time.perf_counter()
    elapsed_time = end - start

    window2(Frame2, type)

def falsepos_(Frame2,type, myEntry, tolerance, iterations, guess_1, guess_2):

    imax = 50
    ea = 0.00001
    global elapsed_time
    global x0
    x0 = float(guess_1)
    global x1
    x1 = float(guess_2)
    print("guess 1:", guess_1)
    print("guess 2: ", guess_2)
    if tolerance != '':
        ea = float(tolerance)
    if iterations != '':
        imax = int(iterations)

    start = time.perf_counter()
    falseposition.body(myEntry, float(guess_1), float(guess_2), float(tolerance), float(iterations))
    end = time.perf_counter()
    elapsed_time = end - start
    print(elapsed_time)

    window2(Frame2,type)

def secant_(Frame2,type, myEntry, tolerance, iterations, guess_1, guess_2):
    print(type)
    imax = 50
    ea = 0.00001
    global elapsed_time
    global x0
    x0 = float(guess_1)
    global x1
    x1 = float(guess_2)
    print("guess 1:", guess_1)
    print("guess 2: ", guess_2)
    if tolerance != '':
        ea = float(tolerance)
    if iterations != '':
        imax = int(iterations)

    start = time.perf_counter()
    secant.body(myEntry, float(guess_1), float(guess_2), float(tolerance), float(iterations))
    end = time.perf_counter()
    elapsed_time = end - start
    print(elapsed_time)

    window2(Frame2,type)

def fixedpos_(Frame2,type, myEntry, tolerance, iterations, guess_1):
    imax = 50
    ea = 0.00001
    global elapsed_time
    global x0
    x0 = float(guess_1)
    if tolerance != '':
        ea = float(tolerance)
    if iterations != '':
        imax = int(iterations)

    start = time.perf_counter()
    fixedpoint.body(myEntry, float(guess_1), float(tolerance), float(iterations))
    end = time.perf_counter()
    elapsed_time = end - start

    window2(Frame2,type)

def window2(Frame2, type):
    def back_btn():
        window1()
        Frame3.destroy()

    Frame2.destroy()
    Frame3 = LabelFrame(root, bg="#b9dbfa", padx=90)
    Frame3.grid(row=1,  sticky= NS,padx=5, pady=5)

    Title = Label(Frame3, text="")
    Iteration = Label(Frame3, text="")
    Xi = Label(Frame3, text="")
    Xii = Label(Frame3, text="")
    Error = Label(Frame3, text="")
    Root =Label(Frame3, text="")
    Answer = Label(Frame3, text="")
    Iteration = Label(Frame3, text="")
    Time = Label(Frame3, text="")
    back= Button(Frame3, text="RETURN", bg="#006dcc", font=("Courier", 12),command=back_btn)
    back.grid(row=0 , column=0)
    global table
    #*************** BISECTION METHOD *************************
    if type==1:
        if (BisectionMethod.string == ""):
            Title.config(text="Result of Bisection method", bg = "#b9dbfa", font = ('Courier 15 bold'))
            Title.grid(row=1, column=0, columnspan=4, sticky=NS)
            Iteration.config(text="Iteration", bg = "#b9dbfa", font = ("Courier", 12))
            Iteration.grid(row=2, column=0)
            Xi.config(text="Xi", bg = "#b9dbfa", font = ("Courier", 12))
            Xi.grid(row=2, column=1)
            Xii.config(text="Xii", bg = "#b9dbfa", font = ("Courier", 12))
            Xii.grid(row=2, column=2)
            Error.config(text="ERROR", bg = "#b9dbfa", font = ("Courier", 12))
            Error.grid(row=2, column=3)


            error = BisectionMethod.error
            xi = BisectionMethod.xi
            xii = BisectionMethod.xii
            X2 = BisectionMethod.x2


            Root.config(text="The Root", bg = "#b9dbfa", font = ("Courier", 12))
            Root.grid(row=len(xi) + 7, column=0)
            Iteration.config(text="Total Iterations", bg = "#b9dbfa", font = ("Courier", 12))
            Iteration.grid(row=len(xi) + 8, column=0)
            Time.config(text="Time Consumed ", bg = "#b9dbfa", font = ("Courier", 12))
            Time.grid(row=len(xi) + 9, column=0)
            for i in range(1, len(xi)):
                table = Label(Frame3, text=i, bg = "#b9dbfa", font = ("Courier", 12))
                table.grid(row=i + 2, column=0)

            for i in range(1, len(xi)):
                table = Label(Frame3, text=xi[i], bg = "#b9dbfa", font = ("Courier", 12))
                table.grid(row=i + 2, column=1)
            for i in range(1, len(xii)):
                table = Label(Frame3, text=xii[i], bg = "#b9dbfa", font = ("Courier", 12))
                table.grid(row=i + 2, column=2)
            for i in range(1, len(error)):
                table.grid(row=i + 2, column=3)
                table = Label(Frame3, text=error[i], bg = "#b9dbfa", font = ("Courier", 12))

            table = Label(Frame3, text=X2, bg = "#b9dbfa", font = ("Courier", 12))
            table.grid(row=len(xi) + 7, column=1)
            table = Label(Frame3, text=BisectionMethod.it, bg = "#b9dbfa", font = ("Courier", 12))
            table.grid(row=len(xi) + 8, column=1)
            table.grid(row=len(xi) + 9, column=1)
            table = Label(Frame3, text=elapsed_time, bg = "#b9dbfa", font = ("Courier", 12))
        else:
            Answer.config(text=BisectionMethod.string,bg = "#b9dbfa", font = ("Courier", 12))
            Answer.grid(row=1, column=0 , columnspan=4, sticky= NS)

    elif type==3:
        if (falseposition.string == ""):

            Title.config(text="Result of False Position method", font=('Courier 15 bold'), bg="#b9dbfa")
            Title.grid(row=1, column=0, columnspan=4, sticky=NS)
            Iteration.config(text="Iteration", font=("Courier", 12), bg="#b9dbfa")
            Iteration.grid(row=2, column=0)
            Xi.config(text="Xi", font=("Courier", 12), bg="#b9dbfa")
            Xi.grid(row=2, column=1)
            Xii.config(text="Xii", font=("Courier", 12), bg="#b9dbfa")
            Xii.grid(row=2, column=2)
            Error.config(text="ERROR", font=("Courier", 12), bg="#b9dbfa")
            Error.grid(row=2, column=3)

            error = falseposition.error
            xi = falseposition.xi
            xii = falseposition.xii
            x2 = falseposition.x2

            Root.config(text="The Root", font=("Courier", 12), bg="#b9dbfa")
            Root.grid(row=len(xi) + 6, column=0)
            Iteration.config(text="Iterations", font=("Courier", 12), bg="#b9dbfa")
            Iteration.grid(row=len(xi) + 7, column=0)
            Time.config(text="Elapsed_Time", font=("Courier", 12), bg="#b9dbfa")
            Time.grid(row=len(xi) + 8, column=0)
            for i in range(1, len(xi)):
                table = Label(Frame3, text=i, font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=0)

            for i in range(1, len(xi)):
                table = Label(Frame3, text=xi[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=1)
            for i in range(1, len(xii)):
                table = Label(Frame3, text=xii[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=2)
            for i in range(1, len(error)):
                table = Label(Frame3, text=error[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=3)

            table = Label(Frame3, text=x2, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 6, column=1)
            table = Label(Frame3, text=falseposition.it, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 7, column=1)
            table = Label(Frame3, text=elapsed_time, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 8, column=1)
        else:
            Answer.config(text=falseposition.string, font=("Courier", 12), bg="#b9dbfa")
            Answer.grid(row=1, column=0 , columnspan=4, sticky= NS)

    elif type==4:
        if (secant.string == ""):

            Title.config(text="Result of Secant method", font=('Courier 15 bold'), bg="#b9dbfa")
            Title.grid(row=1, column=0, columnspan=4, sticky=NS)
            Iteration.config(text="Iteration", font=("Courier", 12), bg="#b9dbfa")
            Iteration.grid(row=2, column=0)
            Xi.config(text="Xi", font=("Courier", 12), bg="#b9dbfa")
            Xi.grid(row=2, column=1)
            Xii.config(text="Xii", font=("Courier", 12), bg="#b9dbfa")
            Xii.grid(row=2, column=3)
            Error.config(text="ERROR",font=("Courier", 12), bg="#b9dbfa")
            Error.grid(row=2, column=4)

            error = secant.error
            xi = secant.xi
            xii = secant.xii
            X2 = secant.x2

            Root.config(text="The Root",font=("Courier", 12), bg="#b9dbfa")
            Root.grid(row=len(xi) + 6, column=0)
            Iteration.config(text="The Number Of Iteration", font=("Courier", 12), bg="#b9dbfa")
            Iteration.grid(row=len(xi) + 7, column=0)
            Time.config(text="Elapsed_Time", font=("Courier", 12), bg="#b9dbfa")
            Time.grid(row=len(xi) + 8, column=0)
            for i in range(1, len(xi)):
                table = Label(Frame3, text=i, font=("Courier", 12), bg="#b9dbfa").grid(row=i + 2, column=0)

            for i in range(1, len(xi)):
                table = Label(Frame3, text=xi[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=1)

            for i in range(1, len(xii)):
                table = Label(Frame3, text=xii[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=2)

            for i in range(1, len(error)):
                table = Label(Frame3, text=error[i],font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=4)

            table = Label(Frame3, text=X2, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 6, column=1)
            table= Label(Frame3, text=secant.it, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 7, column=1)
            table = Label(Frame3, text=elapsed_time, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 8, column=1)
        else:
            Answer.config(text=secant.string, font=("Courier", 12), bg="#b9dbfa")
            Answer.grid(row=1, column=0, columnspan=4, sticky= NS)

    elif type==2:
        if (NewtonRaphson.string == ""):
            Title.config(text="Result of Newton Raphson Method", font=("Courier", 15), bg="#b9dbfa")
            Title.grid(row=1, column=0, columnspan=4, sticky=NS)
            Iteration.config(text="Iteration", font=("Courier", 12), bg="#b9dbfa")
            Iteration.grid(row=2, column=0)
            Xi.config(text="Xi", font=("Courier", 12), bg="#b9dbfa")
            Xi.grid(row=2, column=1)
            Xii.config(text="Xii", font=("Courier", 12), bg="#b9dbfa")
            Xii.grid(row=2, column=2)
            Error.config(text="ERROR", font=("Courier", 12), bg="#b9dbfa")
            Error.grid(row=2, column=3)

            error = NewtonRaphson.error
            xi = NewtonRaphson.xi
            xii = NewtonRaphson.xii
            X2 = NewtonRaphson.x1

            Root.config(text="The Root", font=("Courier", 12), bg="#b9dbfa")
            Root.grid(row=len(xi) + 6, column=0)
            Iteration.config(text="The Number Of Iteration", font=("Courier", 12), bg="#b9dbfa")
            Iteration.grid(row=len(xi) + 7, column=0)
            Time.config(text="Elapsed_Time", font=("Courier", 12), bg="#b9dbfa")
            Time.grid(row=len(xi) + 8, column=0)
            for i in range(1, len(xi)):
                 table= Label(Frame3, text=i, font=("Courier", 12), bg="#b9dbfa")
                 table.grid(row=i + 2, column=0)

            for i in range(1, len(xi)):
                table = Label(Frame3, text=xi[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=1)

            for i in range(1, len(xii)):
                table = Label(Frame3, text=xii[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=2)

            for i in range(1, len(error)):
                table = Label(Frame3, text=error[i], font=("Courier", 12), bg="#b9dbfa")
                table.grid(row=i + 2, column=3)

            table = Label(Frame3, text=X2, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 6, column=1)
            table = Label(Frame3, text=NewtonRaphson.it, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 7, column=1)
            table = Label(Frame3, text=elapsed_time, font=("Courier", 12), bg="#b9dbfa")
            table.grid(row=len(xi) + 8, column=1)

        else:
            Answer.config(text=NewtonRaphson.string, font=("Courier", 12), bg="#b9dbfa")
            Answer.grid(row=1, column=0, columnspan=4, sticky= NS)

    elif type==5:
        if (fixedpoint.string ==''):
             Title.config(text="Result of Fixed Point method", font=("Courier", 15), bg="#b9dbfa")
             Title.grid(row=1, column=0, columnspan=4, sticky=NS)
             Iteration.config(text="Iteration", font=("Courier", 12), bg="#b9dbfa")
             Iteration.grid(row=2, column=0)
             Xi.config(text="Xi", font=("Courier", 12), bg="#b9dbfa")
             Xi.grid(row=2, column=1)
             Xii.config(text="Xii", font=("Courier", 12), bg="#b9dbfa")
             Xii.grid(row=2, column=2)
             Error.config(text="ERROR", font=("Courier", 12), bg="#b9dbfa")
             Error.grid(row=2, column=3)

             # correct the label
             error = fixedpoint.error
             xi = fixedpoint.xi
             xii = fixedpoint.xii
             X2 = fixedpoint.x1
             total_rows = 4

             Root.config(text="The Root", font=("Courier", 12), bg="#b9dbfa")
             Root.grid(row=len(xi) + 6, column=0)
             Iteration.config(text="The Number Of Iteration", font=("Courier", 12), bg="#b9dbfa")
             Iteration.grid(row=len(xi) + 7, column=0)
             Time.config(text="Elapsed_Time", font=("Courier", 12), bg="#b9dbfa")
             Time.grid(row=len(xi) + 8, column=0)
             for i in range(1, len(xi)):
                 table = Label(Frame3, text=i,  font=("Courier", 12), bg="#b9dbfa")
                 table.grid(row=i + 2, column=0)

             for i in range(1, len(xi)):
                 table = Label(Frame3, text=xi[i], font=("Courier", 12), bg="#b9dbfa")
                 table.grid(row=i + 2, column=1)

             for i in range(1, len(xii)):
                 table = Label(Frame3, text=xii[i], font=("Courier", 12), bg="#b9dbfa")
                 table.grid(row=i + 2, column=2)

             for i in range(1, len(error)):
                 table = Label(Frame3, text=error[i], font=("Courier", 12), bg="#b9dbfa")
                 table.grid(row=i + 2, column=3)

             table = Label(Frame3, text=X2,  font=("Courier", 12), bg="#b9dbfa")
             table.grid(row=len(xi) + 6, column=1)
             table = Label(Frame3, text=fixedpoint.it, font=("Courier", 12), bg="#b9dbfa")
             table.grid(row=len(xi) + 7, column=1)
             table = Label(Frame3, text=elapsed_time,  font=("Courier", 12), bg="#b9dbfa")
             table.grid(row=len(xi) + 8, column=1)
        else:
             Answer=Label(Frame3,text=fixedpoint.string, font=("Courier", 12), bg="#b9dbfa")
             Answer.grid(row=1 , column=0, columnspan=4, sticky= NS)


def destroyer():
    root.destroy()

def restart():
    root.destroy()
    os.startfile("main.py")


#***************  M A I N ******************
control= LabelFrame(root,bg="White")
control.grid(row=0, sticky= N, padx=5, pady=5)

btn_restart = Button(control, text="RESTART", fg="White", bg="Blue", command=restart, font=("courier", 12), padx=50).grid(row=0, column=2,columnspan=2)
btn_exit = Button(control, text="EXIT", fg="White", bg="Blue", command=destroyer, font=("courier", 12), padx=60).grid(row=0, column=0,columnspan=2)
window1()


root.mainloop()
