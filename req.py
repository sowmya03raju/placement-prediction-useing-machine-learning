data = pd.read_csv("placement_data.csv", sep=",")
            y = data.target
            x = data.drop('target', axis=1)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=2)
            model = tree.DecisionTreeClassifier(max_depth=5, max_leaf_nodes=10, criterion='entropy')
            model.fit(x_train, y_train)
            y_predict = model.predict([[int(result[0]),int(result[1]),int(result[2]),int(result[3]),int(result[4]),int(result[5]),int(result[6])]])
            print(y_predict)
            if y_predict =='yes':
                aa = mysql.connector.connect(host='localhost', port=3306, user="root", passwd="root", db="pla")
                mm = aa.cursor()
                eligeble='1'
                noteligeble='0'
        
                mm.execute("""INSERT INTO eligeble VALUES (%s,%s)""", (eligeble,noteligeble))
                
                #aa.commit()
                print("record saved successfully")
                label = ['Eligeble', 'NotEligeble']
                mm.execute("SELECT eligeble FROM eligeble")
                eligeble=mm.fetchall()
                plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
                plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
                plt.xlabel('Eligeble')
                plt.ylabel('Not Eligeble Students')
                plt.title('No of Eligeble Students')
                plt.show()
                
                from tkinter import messagebox
                print(messagebox.showinfo("Congradulations","Eligeble"))
            else:
                print(messagebox.showinfo("Congradulations","NotEligeble"))
                
            
                window9.mainloop()
