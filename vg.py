def vg():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
    mycursor=mydb.cursor()
    mycursor.execute("select * from staff where name='vivek gandhi'")
    myrecord=mycursor.fetchall()
    for (name,age,workhour,salary,designation) in myrecord:
        print("=====================================")
        print("staff name :",name)
        print("staff age :",age)
        print("staff workhour :",workhour)
        print("staff salary :",salary)
        print("staff designation :",designation)
        
