from database import connect_db

def apply_company():
    con=connect_db()
    cur=con.cursor()
    s_id=int(input("Enter Student ID: "))
    c_id=int(input("Enter Company ID: "))

    cur.execute("select CGPA from student where Student_id=%s",(s_id,))
    student=cur.fetchone()
    if student is None:
        print("Student ID not found!")
        con.close()
        return

    cur.execute("select Min_CGPA from company where Company_id=%s",(c_id,))
    company=cur.fetchone()
    if company is None:
        print("Company ID not found!")
        con.close()
        return

    student_cgpa=student[0]
    min_cgpa=company[0]

    if student_cgpa<min_cgpa:
        print("Student is not eligible for this company!")
        con.close()
        return
    
    query="insert into application(Student_id,Company_id)values(%s,%s)"
    values=(s_id,c_id)
    try:
       cur.execute(query,values)
       con.commit()
       print("Application Submitted Successfully!")

    except:   
        print("Student has already applied to this company!")
        con.commit()
        print("Application Submitted Successfully!")
        con.close()

def view_application():
    con=connect_db()
    cur=con.cursor()
    cur.execute("select*from application")
    data=cur.fetchall()
    for i in data:
        print("Application ID :", i[0])
        print("Student ID :", i[1])
        print("Company ID :", i[2])
        print("Status :", i[3])
        print("="*30)
    con.close()

def update_application():
    con=connect_db()
    cur=con.cursor()
    a_id=int(input("Enter Your Application ID: "))
    print("1. Applied")
    print("2. Shortlisted")
    print("3. Selected")
    print("4. Rejected")

    ch=int(input("Enter Choice: "))
    if ch==1:
       status="Applied"
    elif ch==2:
       status="Shortlisted"
    elif ch==3:
       status="Selected"
    elif ch==4:
       status="Rejected"
    else:
       print("Invalid Choice!")
       con.close()
       return
    query="update application set Status=%s where App_Id=%s"
    cur.execute(query,(status,a_id))
    con.commit()
    print("Application Updated Successfully!")
    con.close()
    
def delete_application():
    con=connect_db()
    cur=con.cursor()
    a_id=int(input("Enter Your Application ID: "))
    query="delete from application where App_Id=%s "
    cur.execute(query,(a_id,))
    con.commit()
    print("Application Deleted Successfully!")
    con.close()
    
