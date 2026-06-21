from database import connect_db

def add_student():
    con=connect_db()
    cur=con.cursor()
    name=input("Enter your name: ")
    branch=input("Enter your branch: ")
    cgpa=float(input("Enter your CGPA:"))
    email=input("Enter your Email Id:")
    query="insert into student values(%s,%s,%s,%s)"
    values=(name,branch,cgpa,email)
    cur.execute(query,values)
    con.commit()
    print("Student Added successfully!")
    con.close()
    
def view_student():
    con=connect_db()
    cur=con.cursor()
    cur.execute("select*from student")
    data=cur.fetchall()
    for i in data:
       print(i)

def update_student():
    con=connect_db()
    cur=con.cursor()
    s_id=int(input("Enter your ID: "))
    print("1. Update Name")
    print("2. Update Branch")
    print("3. Update CGPA")
    print("4. Update Email Id")

    ch=int(input("Enter Your Choice: "))

    if ch==1:
        new_name= input("Enter Your Name: ")
        query="update student set Name=%s where Student_id=%s"
        cur.execute(query,(new_name,s_id))
    elif ch==2:
        new_branch=input("Enter Your Branch: ")
        query="update student set Branch=%s where Student_id=%s"
        cur.execute(query,(new_branch,s_id))
    elif ch==3:
        new_cgpa=float(input("Enter Your CGPA: "))
        query="update student set CGPA=%s where Student_id=%s"
        cur.execute(query,(new_cgpa,s_id))
    elif ch==4:
        new_emailID=input("Enter your Email Id: ")
        query="update student set Email_id=%s where Student_id=%s"
        cur.execute(query,(new_emailID,s_id))
    else:
        print("Invalid choice!")
        con.close()
        return
    con.commit()
    print("updated successfully1")
    con.close()

def delete_student():
    con=connect_db()
    cur=con.cursor()
    s_id=int(input("Enter Id to delete: "))
    query="delete from student where Student_id=%s"
    cur.execute(query,(s_id,))
    con.commit()
    print("Student record has Deleted successfully!")

    con.close()
    
