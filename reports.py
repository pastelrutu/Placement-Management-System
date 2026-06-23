from database import connect_db

def view_selected_students():
    con=connect_db()
    cur=con.cursor()

    cur.execute("""select a.App_Id, s.Name,c.Company_Name,a.Status from
                application a join student s on a.Student_id=s.Student_id
                join company c on a.Company_id=c.Company_id where
                a.Status='Selected'
                """)
    data=cur.fetchall()
    for i in data:
        print("Application ID :", i[0])
        print("Student ID :", i[1])
        print("Company ID :", i[2])
        print("Status :", i[3])
        print("="*30)
    con.close()
def view_rejected_students():
     con=connect_db()
     cur=con.cursor()

     cur.execute("""select a.App_Id, s.Name,c.Company_Name,a.Status from
                application a join student s on a.Student_id=s.Student_id
                join company c on a.Company_id=c.Company_id where
                a.Status='Rejected'
                """)
     data=cur.fetchall()
     for i in data:

         print("Application ID :", i[0])
         print("Student ID :", i[1])
         print("Company ID :", i[2])
         print("Status :", i[3])
         print("="*30)
     con.close() 

def view_shortlisted_students():
     con=connect_db()
     cur=con.cursor()

     cur.execute("""select a.App_Id, s.Name,c.Company_Name,a.Status from
                application a join student s on a.Student_id=s.Student_id
                join company c on a.Company_id=c.Company_id where
                a.Status='Shortlisted'
                """)
     data=cur.fetchall()
     for i in data:
         print("Application ID :", i[0])
         print("Student ID :", i[1])
         print("Company ID :", i[2])
         print("Status :", i[3])
         print("="*30)
     con.close()

def total_application():
     con=connect_db()
     cur=con.cursor()
     cur.execute("select count(*)from application")
     total=cur.fetchone()
     print("Total Application: ",total[0])
     con.close()

def total_selected_students():
     con=connect_db()
     cur=con.cursor()
     cur.execute("select count(*)from application where status='Selected'")
     total=cur.fetchone()
     print("Total Selected Students: ",total[0])
     con.close()

def select_choice_menu():
    while True:
        print("\n===== Selection Status Module =====")
        
        print("1. View Selected Students list")
        print("2. View Rejected Students list")
        print("3. View Shortlisted Students list")
        print("4. Total Applications")
        print("5. Total Selected Students")
        print("6. Back")

        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
             view_selected_students()
        elif ch==2:
             view_rejected_students()
        elif ch==3:
             view_shortlisted_students()
        elif ch==4:
             total_application()
        elif ch==5:
             total_selected_students()
        elif ch==6:
             return
        else:
             print("Invalid Choice!")
     
   
    
     
