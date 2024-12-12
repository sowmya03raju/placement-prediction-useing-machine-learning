from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import tkinter.messagebox
import tkinter.filedialog
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier 


def hrportal():
    window = Tk()
    window.geometry('900x600')
    image=Image.open('grey.jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window,image=photo_image)
    label.place(x=0,y=0)
    
    btn = Button(window, text="REGISTER", width=8, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=register)
    btn.place(x=400, y=300)

    btn1 = Button(window, text="ADMINLOGIN", width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=Ulogin)
    btn1.place(x=390, y=400)

    '''btn2 = Button(window, text="HRLOGIN", width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=Hlogin)
    btn2.place(x=490, y=330)'''
    
    window.mainloop()

def register():
    def registerinto():
        name = e1.get()
        phone = e2.get()
        emails = e3.get()
        password = e4.get()
        add = e5.get()
        

        aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="el")
        mm = aa.cursor()
        
        mm.execute("""INSERT INTO register VALUES (%s,%s,%s,%s,%s)""", (name, phone, emails, password,add))
        aa.commit()

        if e1.get() == "" or e4.get() == "":
            tkinter.messagebox.showinfo("sorry", "Pease fill the required information")
        else:
            tkinter.messagebox.showinfo("Welcome to %s" % name, "Let Login")
            Ulogin()

    window1 = Toplevel()
    window1.geometry('900x600')
    image=Image.open('grey.jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window1,image=photo_image)
    label.place(x=0,y=0)
    lb5 = Label(window1, text="Name",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=80, y=140)

    lb5 = Label(window1, text="Phone",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=80, y=220)
    lb5 = Label(window1, text="Emails",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=60, y=300)

    lb5 = Label(window1, text="Password",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=10, y=390)
    lb5 = Label(window1, text="Add",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=90, y=490)

    
    e1= Entry(window1,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=200, y=140)

    e2= Entry(window1,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=200, y=220)

    e3= Entry(window1,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e3.place(x=200, y=300)

    e4= Entry(window1,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e4.place(x=200, y=390)

    e5= Entry(window1,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e5.place(x=200, y=490)

    btn = Button(window1, text="REGISTER", width=8, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=registerinto)
    btn.place(x=400, y=550)

    
    window1.mainloop()

def Ulogin():
    def loginto():
        aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="el")
        mm = aa.cursor()
        name = e1.get()
        password = e2.get()
        if e1.get() == "" or e2.get() == "":
            tkinter.messagebox.showinfo("sorry", "Please complete the required field")
        else:
            mm.execute('SELECT * FROM register WHERE name = %s AND password = %s', (name, password))
            for i in name:
                print( 0 )
            if mm.fetchall():
                tkinter.messagebox.showinfo("Welcome to %s" % name, "Logged in successfully")
                job()
            else:
                tkinter.messagebox.showinfo("Sorry", "Wrong Password")  
    window2 = Toplevel()
    window2.geometry('900x600')
    image=Image.open('grey.jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window2,image=photo_image)
    label.place(x=0,y=0)

    lb1 = Label(window2, text="USERNAME",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb1.place(x=300, y=420)
    e1= Entry(window2,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=420, y=420)
    
    lb2 = Label(window2, text="PASSWORD",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb2.place(x=300, y=480)
    e2= Entry(window2,width=15,font=("bold",17),show="*",highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=420, y=480)


    btn = Button(window2, text="LOGIN", width=8, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=loginto)
    btn.place(x=460, y=540)
    
    window2.mainloop()

'''def Hlogin():
    def Hlogin1():
        name = e1.get()
        password = e2.get()
        if e1.get() == "" or e2.get() == "":
            tkinter.messagebox.showinfo("sorry", "Please complete the required field")
        elif e1.get() == "admin" or e2.get() == "admin":
            tkinter.messagebox.showinfo("logged in succeessfully")
            job1()
        else:
             tkinter.messagebox.showinfo("wrong password or username")
    window3 = Toplevel()
    window3.geometry('900x600')
    image=Image.open('download (8).jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window3,image=photo_image)
    label.place(x=0,y=0)
    
    e1= Entry(window3,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=250, y=180)

    e2= Entry(window3,width=15,font=("bold",17),show="*",highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=250, y=280)
    
    btn = Button(window3, text="LOGIN", width=8, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=Hlogin1)
    btn.place(x=420, y=450)
    
    window3.mainloop()'''

def job():
    window4 = Toplevel()
    window4.geometry('900x600')
    image=Image.open('grey.jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window4,image=photo_image)
    label.place(x=0,y=0)
    
    btn = Button(window4, text="EnterMarks", width=15, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply)
    btn.place(x=400, y=200)
    btn = Button(window4, text="EligebleTest", width=15, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply1)
    btn.place(x=400, y=280)
    
    '''btn = Button(window4, text="EXP JOB", width=15, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=uj1)
    btn.place(x=400, y=300)'''
    
    window4.mainloop()

'''def uj():
    
    window7 = Toplevel()
    window7.geometry('900x600')
    image=Image.open('download (5).jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window7,image=photo_image)
    label.place(x=0,y=0)
    aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="job")
    mm = aa.cursor()
    #mm.execute('SELECT * FROM job1 WHERE fjob = %s AND ejob = %s', (fjob, ejob))
    mm.execute('SELECT fjob FROM job1')
    list1 = mm.fetchall()
    menubutton = Menubutton(window7, text = "Jobs",width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center')  
  
    menubutton.place(x=400,y=200)  
  
    menubutton.menu = Menu(menubutton)  
  
    menubutton["menu"]=menubutton.menu  
    a=[]
    for i in range(len(list1)):
        print(list1[i])
        a.append(list1[i])
        menubutton.menu.add_checkbutton(label = list1[i], variable=IntVar())
        #menubutton.pack()

    btn = Button(window7, text="APPLY", width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply)
    btn.place(x=600, y=200)
    window7.mainloop()'''
    
'''def uj1():
    window8 = Toplevel()
    window8.geometry('900x600')
    image=Image.open('download (5).jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window8,image=photo_image)
    label.place(x=0,y=0)
    aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="job")
    mm = aa.cursor()
    #mm.execute('SELECT * FROM job1 WHERE fjob = %s AND ejob = %s', (fjob, ejob))
    mm.execute('SELECT ejob FROM job1')
    list1 = mm.fetchall()
    menubutton = Menubutton(window8, text = "Jobs",width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center')  
  
    menubutton.place(x=400,y=200)  
  
    menubutton.menu = Menu(menubutton)  
  
    menubutton["menu"]=menubutton.menu  
    a=[]
    for i in range(len(list1)):
        print(list1[i])
        a.append(list1[i])
        menubutton.menu.add_checkbutton(label = list1[i], variable=IntVar())
        #menubutton.pack()
        
    btn = Button(window8, text="APPLY", width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply1)
    btn.place(x=600, y=200)
    window8.mainloop()'''
    
'''def job1():
    window4 = Toplevel()
    window4.geometry('900x600')
    image=Image.open('download (5).jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window4,image=photo_image)
    label.place(x=0,y=0)
    
    btn = Button(window4, text="ENTER JOBS", width=15, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=form)
    btn.place(x=400, y=330)
    
    aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="aa")
    mm = aa.cursor()
    #mm.execute('SELECT * FROM job1 WHERE fjob = %s AND ejob = %s', (fjob, ejob))
    mm.execute('SELECT name,phone,ap FROM aa1')
    list1 = mm.fetchall()
    menubutton = Menubutton(window4, text = "freshers",width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center')  
  
    menubutton.place(x=400,y=200)  
  
    menubutton.menu = Menu(menubutton)  
  
    menubutton["menu"]=menubutton.menu  
    a=[]
    for i in range(len(list1)):
        print(list1[i])
        a.append(list1[i])
        menubutton.menu.add_checkbutton(label = list1[i], variable=IntVar())

    
    aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="ab")
    mm = aa.cursor()
    #mm.execute('SELECT * FROM job1 WHERE fjob = %s AND ejob = %s', (fjob, ejob))
    mm.execute('SELECT name,phone,ap FROM ab1')
    list1 = mm.fetchall()
    menubutton = Menubutton(window4, text = "exp",width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center')  
  
    menubutton.place(x=500,y=200)  
  
    menubutton.menu = Menu(menubutton)  
  
    menubutton["menu"]=menubutton.menu  
    a=[]
    for i in range(len(list1)):
        print(list1[i])
        a.append(list1[i])
        menubutton.menu.add_checkbutton(label = list1[i], variable=IntVar())
    

    window4.mainloop()

def form():
    def fo():
        fjob=e1.get()
        ejob=e2.get()
        aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="job")
        mm = aa.cursor()
        mm.execute("""INSERT INTO job1 VALUES (%s,%s)""", (fjob,ejob))
        aa.commit()
    window5 = Toplevel()
    window5.geometry('900x600')
    image=Image.open('download (5).jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window5,image=photo_image)
    label.place(x=0,y=0)

    lb5 = Label(window5, text="ENTER FRESHER JOBS",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=240, y=180)

    lb5 = Label(window5, text="ENTER EXP JOBS",font=('algerian',25,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=260, y=250)
    
    e1= Entry(window5,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=590, y=180)

    e2= Entry(window5,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=550, y=250)

    btn1 = Button(window5, text="SUBMIT", width=10, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=fo)
    btn1.place(x=400, y=330)
    
    window5.mainloop()'''

def apply():
    def a1():
        SIE = e1.get()
        APT = e2.get()
        GD = e3.get()
        PI = e4.get()
        ten = e5.get()
        puc = e6.get()
        deg = e7.get()
        name=e8.get()
        usn=e9.get()
        #ap=e10.get()
        #target = e8.get()
        print(SIE)
        print(APT)
        print(GD)
        print(PI)
        print(ten)
        print(puc)
        print(deg)
        #from sklearn.model_selection import train_test_split
        #import pandas as pd
        #from sklearn.svm import SVC
        #data = pd.read_csv("placement_data.csv",sep=",")
        #y=data.target
        #x=data.drop('target',axis=1)
        #x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.7,random_state=2)
        #svc=SVC()
        #svc.fit(x_train,y_train)
        #y_pred=svc.predict([[SIE,APT,GD,PI,ten,puc,deg]])
        #print(y_pred)

        #if y_pred=='yes':
            #print("am in if")
   
        #if (name_field.get() == "" and course_field.get() == "" and sem_field.get() == "" and form_no_field.get() == "" and contact_no_field.get() == "" and email_id_field.get() == "" and address_field.get() == ""):
        if int(SIE) <=10 and int(APT) <=10 and int(GD) <=10 and int(PI) <=10 and int(ten) <=10 and int(puc) <=10 and int(deg) <=10:
            print("entering Database")
            aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="el")
            mm = aa.cursor()
            
            mm.execute("""INSERT INTO el1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (SIE,APT,GD,PI,ten,puc,deg,name,usn))
            aa.commit()
            tkinter.messagebox.showinfo("Congratulations","record saved successfully")
        else:
            tkinter.messagebox.showinfo("error","Enter value between 1 to 10")
        #messagebox.showinfo("Record Saved success",icon="info")
        
    window9 = Toplevel()
    window9.geometry('900x700')
    '''image=Image.open('grey.jpg')
    image=image.resize((900,700))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window9,image=photo_image)
    label.place(x=0,y=0)'''
    

    lb1 = Label(window9, text="SCI ABILITY",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb1.place(x=50, y=150)
    e1= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=195, y=150)

    
    lb2 = Label(window9, text="APTITUDE",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb2.place(x=50, y=230)
    e2= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=195, y=230)

    lb3 = Label(window9, text="GROUP DISC",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb3.place(x=50, y=300)
    e3= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e3.place(x=195, y=300) 

    lb4 = Label(window9, text="PERS INT",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb4.place(x=50, y=400)
    e4= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e4.place(x=195, y=400)

    lb5 = Label(window9, text="TENTH",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=50, y=500)
    e5= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e5.place(x=195, y=500) 

    lb6 = Label(window9, text="PUC",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb6.place(x=650, y=150) 
    e6= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e6.place(x=750, y=150)

    lb7 = Label(window9, text="DEGREE",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb7.place(x=650, y=230) 
    e7= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e7.place(x=750, y=230)

    lb8 = Label(window9, text="NAME",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb8.place(x=650, y=300)
    e8= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e8.place(x=750, y=300)
    
    lb9 = Label(window9, text="USN",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb9.place(x=650, y=400)
    e9= Entry(window9,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e9.place(x=750, y=400)
    


    btn1 = Button(window9, text="SUBMIT", width=10, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=a1)
    btn1.place(x=400, y=600)

    window9.mainloop()



def apply1():
    def loginto():
        aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="el")
        mm = aa.cursor()
        phone = e11.get()
        usn = e12.get()
        if e11.get() == "" or e12.get() == "":
            tkinter.messagebox.showinfo("sorry", "Please complete the required field")
        else:
            mm.execute('SELECT * FROM el1 WHERE phone = %s AND usn = %s', (phone, usn))
            
            result=mm.fetchone()
            SIE=StringVar()
            APT=StringVar()
            GD=StringVar()
            PI=StringVar()
            ten=StringVar()
            puc=StringVar()
            deg=StringVar()
            name=StringVar()
            usn=StringVar()
            print (result)
            
            window9 = Toplevel()
            window9.geometry('900x700')
            '''image=Image.open('grey.jpg')
            image=image.resize((900,700))
            photo_image=ImageTk.PhotoImage(image)
            label=Label(window9,image=photo_image)
            label.place(x=0,y=0)'''
    

            lb1 = Label(window9, text="SIE",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb1.place(x=50, y=150)
            e1= Entry(window9,width=10,textvariable=SIE,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e1.place(x=200, y=150)

    
            lb2 = Label(window9, text="APT",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb2.place(x=50, y=230)
            e2= Entry(window9,width=10,textvariable=APT,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e2.place(x=200, y=230)

            lb3 = Label(window9, text="GD",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb3.place(x=50, y=300)
            e3= Entry(window9,width=10,textvariable=GD,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e3.place(x=200, y=300) 

            lb4 = Label(window9, text="PI",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb4.place(x=50, y=400)
            e4= Entry(window9,width=10,textvariable=PI,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e4.place(x=200, y=400)

            lb5 = Label(window9, text="ten",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb5.place(x=50, y=500)
            e5= Entry(window9,width=10,textvariable=ten,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e5.place(x=200, y=500) 

            lb6 = Label(window9, text="puc",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb6.place(x=450, y=150) 
            e6= Entry(window9,width=10,textvariable=puc,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e6.place(x=500, y=150)

            lb7 = Label(window9, text="deg",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb7.place(x=450, y=230) 
            e7= Entry(window9,width=10,textvariable=deg,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e7.place(x=500, y=230)

            lb8 = Label(window9, text="Name",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb8.place(x=450, y=300)
            e8= Entry(window9,width=10,textvariable=name,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e8.place(x=530, y=300)
    
            lb9 = Label(window9, text="USN",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
            lb9.place(x=450, y=400)
            e9= Entry(window9,width=10,textvariable=usn,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
            e9.place(x=530, y=400)
            btn = Button(window2, text="OK", width=8, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=loginto)
            btn.place(x=600, y=540)
            print (SIE,APT,GD,PI,ten,puc,deg,name,usn)
            
            SIE.set(result[0])
            APT.set(result[1])
            GD.set(result[2])
            PI.set(result[3])
            ten.set(result[4])
            puc.set(result[5])
            deg.set(result[6])
            name.set(result[7])
            usn.set(result[8])
            print (SIE,APT,GD,PI,ten,puc,deg,name,usn)
            data = pd.read_csv("placement_data.csv", sep=",")
            y = data.target
            x = data.drop('target', axis=1)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=2)
            model = tree.DecisionTreeClassifier(max_depth=5, max_leaf_nodes=10, criterion='entropy')
            model.fit(x_train, y_train)
            predictions=model.predict(x_test)
            print(accuracy_score(y_test,predictions))
            print(confusion_matrix(y_test,predictions))
            
            
            
            y_predict = model.predict([[int(result[0]),int(result[1]),int(result[2]),int(result[3]),int(result[4]),int(result[5]),int(result[6])]])
            print(y_predict)
            if y_predict =='yes':
                from tkinter import messagebox
                print(tkinter.messagebox.showinfo("Congratulations","Eligible for placement"))
                #temp=data.iloc[0].values.tolist()
                #plt.plot(temp)
                #plt.title("Eligible")
                #plt.show()
            else:
                print(tkinter.messagebox.showinfo("Sorry","NotEligible for placement"))
            
                #temp=data.iloc[1].values.tolist()
                #plt.plot(temp)
                #plt.title("NotEligible")
                #plt.show()
            import matplotlib.pyplot as plt; plt.rcdefaults()
            import numpy as np
            import matplotlib.pyplot as plt
            objects=('SIE','APT','GD','PI','ten','puc','deg')
            y_pos = np.arange(len(objects))
            performance=[int(result[0]),int(result[1]),int(result[2]),int(result[3]),int(result[4]),int(result[5]),int(result[6])]
            plt.bar(y_pos,performance,align='center',alpha=1.0)
            plt.xticks(y_pos,objects)
            plt.ylabel(y_predict)
            plt.title('Performace Analysis')
            plt.show()
           
            
            window9.mainloop()

    window2 = Toplevel()
    window2.geometry('900x600')
    image=Image.open('grey.jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window2,image=photo_image)
    label.place(x=0,y=0)

    lb11 = Label(window2, text="Student Name",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb11.place(x=250, y=420)
    e11= Entry(window2,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e11.place(x=420, y=420)

    lb12 = Label(window2, text="USN",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb12.place(x=360, y=480)
    e12= Entry(window2,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e12.place(x=420, y=480)
    
    btn = Button(window2, text="LOGIN", width=8, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=loginto)
    btn.place(x=460, y=540)
    
    window2.mainloop()


'''def apply1():
    def ab1():
        SIE = e1.get()
        APT = e2.get()
        GD = e3.get()
        PI = e4.get()
        ten = e5.get()
        puc = e6.get()
        deg = e7.get()
        proj = e8.get()
        exp = e9.get()
        name= e10.get()
        phone=e11.get()
        ap=e12.get()
        print(SIE)
        print(APT)
        print(GD)
        print(PI)
        print(ten)
        print(puc)
        print(deg)
        from sklearn.model_selection import train_test_split
        from matplotlib import pyplot as plt
        import pandas as pd
        from sklearn.svm import SVC
        data = pd.read_csv("experience_data.csv",sep=",")
        y=data.target
        x=data.drop('target',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.7,random_state=2)
        svc=SVC()
        svc.fit(x_train,y_train) 
        y_pred=svc.predict([[SIE,APT,GD,PI,ten,puc,deg,proj,exp]])  #SIE,APT,GD,PI,ten,puc,deg,proj,exp
        print(y_pred)
        if y_pred=='yes':
            aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="ab")
            mm = aa.cursor()
        
            mm.execute("""INSERT INTO ab1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (SIE,APT,GD,PI,ten,puc,deg,proj,exp,name,phone,ap))
            aa.commit()
            print("Congrats You are Eligeble For Interview U get a call rom HR")
        
    window10 = Toplevel()
    window10.geometry('900x800')
    image=Image.open('download (5).jpg')
    image=image.resize((900,800))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window10,image=photo_image)
    label.place(x=0,y=0)

    lb1 = Label(window10, text="SIE",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb1.place(x=50, y=150)
    e1= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=200, y=150)

    
    lb2 = Label(window10, text="APT",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb2.place(x=50, y=230)
    e2= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=200, y=230)

    lb3 = Label(window10, text="GD",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb3.place(x=50, y=300)
    e3= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e3.place(x=200, y=300) 

    lb4 = Label(window10, text="PI",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb4.place(x=50, y=400)
    e4= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e4.place(x=200, y=400)

    lb5 = Label(window10, text="ten",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb5.place(x=50, y=500)
    e5= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e5.place(x=200, y=500) 

    lb6 = Label(window10, text="puc",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb6.place(x=450, y=150) 
    e6= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e6.place(x=500, y=150)

    lb7 = Label(window10, text="deg",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb7.place(x=450, y=230) 
    e7= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e7.place(x=500, y=230)

    lb8 = Label(window10, text="proj",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb8.place(x=450, y=300) 
    e8= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e8.place(x=530, y=300)

    lb9 = Label(window10, text="exp",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb9.place(x=450, y=370) 
    e9= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e9.place(x=500, y=370)
    
    lb10 = Label(window10, text="Name",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb10.place(x=450, y=450)
    e10= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e10.place(x=530, y=450)
    
    lb11 = Label(window10, text="Phone",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb11.place(x=450, y=530)
    e11= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e11.place(x=530, y=530)
    
    lb12 = Label(window10, text="AppliedPosition",font=('algerian',15,'bold'),fg="BLUE",anchor='w')
    lb12.place(x=450, y=620)
    e12= Entry(window10,width=10,font=("bold",15),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e12.place(x=630, y=620)
    
    btn1 = Button(window10, text="SUBMIT", width=10, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=ab1)
    btn1.place(x=250, y=600)

    window10.mainloop()'''

