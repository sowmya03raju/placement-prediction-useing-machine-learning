from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
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
import warnings
warnings.filterwarnings("ignore")
'''
conn = sqlite3.connect('place1.db')
with conn:
    cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS student1 (Username TEXT,Password TEXT,Phoneno TEXT,Address TEXT,SIE TEXT,APT TEXT,GD TEXT,PI TEXT,ten TEXT,puc TEXT,deg TEXT,name TEXT,usn TEXT)')
print("database created")
cursor.execute('INSERT INTO student1 (Username,Password ,Phoneno,Address,SIE,APT,GD,PI,ten,puc,deg,name,usn) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)')
print("database inseted")
conn.commit()
'''

def main():
    R1=Tk()
    R1.geometry('900x600')
    R1.title('Main')
    image=Image.open('placement_img.jpg')
    image=image.resize((900,700))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R1,image=photo_image)
    label.place(x=0,y=0)
    #label.place(x=0,y=0)
  
    
    la=Label(R1,text="Placement Manegment System",font=('algerian',15,'bold'))
    la.place(x=200,y=100)
    
    Registerbt = Button(R1,text = "REGISTER",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=sigup)
    loginbt = Button(R1,text = "LOGIN",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=login)
    Registerbt.place(x =300 ,y=200)
    loginbt.place( x =300,y=300)
    R1.mainloop()
    
def sigup():
    
    
    def Sigups():
        usernames = username.get()
        passwords = password.get()
        phonenos = phoneno.get()
        Address = address.get()
        conn = sqlite3.connect('place1.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student1 (Username TEXT,Password TEXT,Phoneno TEXT,Address TEXT)')
        cursor.execute('INSERT INTO student1 (Username,Password ,Phoneno,Address) VALUES(?,?,?,?)',
                  (usernames,passwords,phonenos,Address,))
        conn.commit()
        if username.get() == "" or password.get() == "":
           messagebox.showinfo("sorry", "Pease fill the required information")
           login()
        else:
           messagebox.showinfo("Welcome to %s" % usernames, "Let Login")
           return
           
    
    R2=Toplevel()
    R2.geometry('900x600')
    R2.title('SigUp Now')
    image=Image.open('images.jpg')
    image=image.resize((900,700))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R2,image=photo_image)
    label.place(x=0,y=0)
   
   
    lblInfo=Label(R2,text="Username",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R2,text="Password",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=190)

    lblInfo=Label(R2,text="phoneno",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=240)

    lblInfo=Label(R2,text="Adress",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=290)

    

    username=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    username.place(x=300,y= 140 )
    
    password=Entry(R2,show="**",width=20,font=("bold",15),highlightthickness=2)
    password.place(x=300,y=190 )
    
    phoneno=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    phoneno.place(x=300,y= 240 )
    
    address=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    address.place(x=300,y= 290 )

    

    signUpbt = Button(R2,text = "SignUp",width=10,height=2,fg="black",font=('algerian',15,'bold'),justify='center',bg="light blue",command=Sigups)
    signUpbt.place( x =350,y=490)
    
      
    R2.mainloop()



def login():

    def login1():
        usernames = e1.get()
        passwords = e2.get()
        conn = sqlite3.connect('place1.db')
        with conn:
          cursor=conn.cursor()
        ('CREATE TABLE IF NOT EXISTS student1 (Username TEXT,Password TEXT,Phoneno TEXT)')
        conn.commit()
        if usernames == "" and passwords == "" :
            messagebox.showinfo("sorry", "Please complete the required field")
        else:
            cursor.execute('SELECT * FROM student1 WHERE Username = "%s" and Password = "%s"'%(usernames,passwords))
            for i in usernames:
                if cursor.fetchall():
                    messagebox.showinfo("Welcome %s" % usernames, "Logged in successfully")
                    job()
                
                else:
                    messagebox.showinfo("Sorry", "Wrong Password")
                    return
  
    
    R3 =Toplevel()
    R3.geometry('900x600')
    R3.title("LOGIN NOW")
    image=Image.open('login.png')
    image=image.resize((900,700))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R3,image=photo_image)
    label.place(x=0,y=0)
    
   
    

    lblInfo=Label(R3,text="username",fg="black",font=("bold",15))
    lblInfo.place(x=230,y=200)
   
    lblInfo=Label(R3,text="Password",fg="black",font=("bold",15))
    lblInfo.place(x=230,y=250)

    e1= Entry(R3,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=330, y=190)

    e2= Entry(R3,width=15,font=("bold",17),show="*",highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=330, y=240)

    btn = Button(R3, text="LOGIN", width=10, height=2,fg="black",font=('algerian',15,'bold'),justify='center',bg="light blue",command=login1)
    btn.place(x=380, y=400)
    
    R3.mainloop()


def job():
    window4 = Toplevel()
    window4.geometry('900x600')
    window4.title("Admin")
    image=Image.open('admin1.jpg')
    image=image.resize((900,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window4,image=photo_image)
    label.place(x=0,y=0)
    
    btn = Button(window4, text="EnterMarks", width=15, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply)
    btn.place(x=400, y=200)
    btn = Button(window4, text="EligebleTest", width=15, height=2,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply1)
    btn.place(x=400, y=280)
    
   
    window4.mainloop()


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

        if int(SIE) <=10 and int(APT) <=10 and int(GD) <=10 and int(PI) <=10 and int(ten) <=10 and int(puc) <=10 and int(deg) <=10:
            print("entering Database")
            conn = sqlite3.connect('place1.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS student1 (SIE TEXT,APT TEXT,GD TEXT,PI TEXT,ten TEXT,puc TEXT,deg TEXT,name TEXT,usn TEXT)')
            cursor.execute('INSERT INTO student1 (SIE,APT ,GD,PI,ten,puc,deg,name,usn) VALUES(?,?,?,?,?,?,?,?,?)',
                      (SIE,APT ,GD,PI,ten,puc,deg,name,usn,))
            conn.commit()
            messagebox.showinfo("Congratulations","record saved successfully")
        else:
            messagebox.showinfo("error","Enter value between 1 to 10")
        
            '''
            aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="el")
            mm = aa.cursor()
            
            mm.execute("""INSERT INTO el1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (SIE,APT,GD,PI,ten,puc,deg,name,usn))
            aa.commit()
            tkinter.messagebox.showinfo("Congratulations","record saved successfully")
        else:
            tkinter.messagebox.showinfo("error","Enter value between 1 to 10")
        #messagebox.showinfo("Record Saved success",icon="info")
            '''
    window9 = Toplevel()
    window9.geometry('900x700')
    image=Image.open('use.jpg')
    window9.title("Enter Marks")
    image=image.resize((900,700))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(window9,image=photo_image)
    label.place(x=0,y=0)
    

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
        #aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="el")
        #mm = aa.cursor()
        name = e11.get()
        usn = e12.get()
        conn = sqlite3.connect('place1.db')
        with conn:
          cursor=conn.cursor()
        ('CREATE TABLE IF NOT EXISTS student1 (name TEXT,usn TEXT)')
        conn.commit()
        if e11.get() == "" or e12.get() == "":
            messagebox.showinfo("sorry", "Please complete the required field")

        else:
            cursor.execute('SELECT * FROM student1 WHERE name = "%s" and usn = "%s"'%(name,usn))    
            result=cursor.fetchone()

            

            SIE=StringVar()
            APT=StringVar()
            GD=StringVar()
            PI=StringVar()
            ten=StringVar()
            puc=StringVar()
            deg=StringVar()
            name=StringVar()
            usn=StringVar()

            

            
            SIE.set(result[4])
            APT.set(result[5])
            GD.set(result[6])
            PI.set(result[7])
            ten.set(result[8])
            puc.set(result[9])
            deg.set(result[10])
            name.set(result[11])
            usn.set(result[12])
            #print(result[1])
            #print(result[9])
            
            window9 = Toplevel()
            window9.geometry('900x700')
            window9.title("Verify")
            image=Image.open('eligible.jpg')
            image=image.resize((900,700))
            photo_image=ImageTk.PhotoImage(image)
            label=Label(window9,image=photo_image)
            label.place(x=0,y=0)
    

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
            btn = Button(window9, text="OK", width=8, height=1,fg="black",font=('algerian',15,'bold'),bg="SKYBLUE",justify='center',command=apply1)
            btn.place(x=600, y=540)
            res=""
            message =Label(window9, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
            message.place(x=100, y=580)
            
           
            data = pd.read_csv("placement_data.csv", sep=",")
            y = data.target
            x = data.drop('target', axis=1)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=2)
            model = tree.DecisionTreeClassifier(max_depth=5, max_leaf_nodes=10, criterion='entropy')
            model.fit(x_train, y_train)

              
            y_predict = model.predict([[int(result[4]),int(result[5]),int(result[6]),int(result[7]),int(result[8]),int(result[9]),int(result[10])]])
            print('Myprediction',y_predict)
            message.configure(text= y_predict)
            
            if y_predict =='yes':
                from tkinter import messagebox
                print(tkinter.messagebox.showinfo("Congratulations","Eligible for placement"))
                temp=data.iloc[0].values.tolist()
                print("TEMP",temp)
                import matplotlib.pyplot as plt
                plt.plot(temp)
                plt.title("Eligible")
                plt.show()
            else:
                print(tkinter.messagebox.showinfo("Sorry","NotEligible for placement"))
                import matplotlib.pyplot as plt
                temp=data.iloc[1].values.tolist()
                print("TEMP",temp)
                plt.plot(temp)
                plt.title("NotEligible")
                plt.show()
            import matplotlib.pyplot as plt; plt.rcdefaults()
            import numpy as np
            import matplotlib.pyplot as plt
            objects=('SIE','APT','GD','PI','ten','puc','deg')
            y_pos = np.arange(len(objects))
            performance=[int(result[4]),int(result[5]),int(result[6]),int(result[7]),int(result[8]),int(result[9]),int(result[10])]
            plt.bar(y_pos,performance,align='center',alpha=1.0)
            plt.xticks(y_pos,objects)
            plt.ylabel(y_predict)
            plt.title('Performace Analysis')
            plt.show()
            predictions=model.predict(x_test)
            result=accuracy_score(y_test,predictions)
            print(result)
            print(confusion_matrix(y_test,predictions))
            import seaborn as sns
            cm= confusion_matrix(y_test, predictions)
            ax = sns.heatmap(cm/np.sum(cm), annot=True, 
                        fmt='.2%', cmap='Blues')

            ax.set_title('Seaborn Confusion Matrix with labels\n\n');
            ax.set_xlabel('\nPredicted Values')
            ax.set_ylabel('Actual Values ');
            plt.show()

           
            
            window9.mainloop()

    window2 = Toplevel()
    window2.geometry('900x600')
    window2.title("Details")
    image=Image.open('entry.jpg')
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
if __name__ == "__main__":
        #print "Hello World"
     #hrportal()
     main()



  

