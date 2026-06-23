from database import connect_db

def add_drive():
    con=connect_db()
    cur=con.cursor()
    c_id= int(input("Enter Company ID: "))
    date=input("Enter the Drive Date (YYYY-MM-DD): ")
    venue=input("Enter the Venue: ")
    query="insert into placement_drive(Company_id,Drive_Date,Venue) values(%s,%s,%s)"
    values=(c_id,date,venue)
    cur.execute(query,values)
    con.commit()
    print("Drive Added Successfully!")
    con.close()
def view_drive():
    con=connect_db()
    cur=con.cursor()
    cur.execute("select*from placement_drive")
    data=cur.fetchall()
    for i in data:
        print("Drive ID :", i[0])
        print("Company ID :", i[1])
        print("Date :", i[2])
        print("Venue :", i[3])
        print("="*30)
    con.close()
def update_drive():
    con=connect_db()
    cur=con.cursor()
    d_id=int(input("Enter drive ID: "))
    print("1. Update Venue")
    print("2. Update Date")

    ch=int(input("Enter Your Choice: "))

    if ch==1:
        new_venue=input("Enter Venue: ")
        query="update placement_drive set Venue=%s where Drive_id=%s"
        cur.execute(query,(new_venue,d_id))
    elif ch==2:
        new_date=input("Enter Date(YYYY-MM-DD): ")
        query="update placement_drive set Drive_Date=%s where Drive_id=%s"
        cur.execute(query,(new_date,d_id))
    else:
        print("Invalid Choice!")
        con.close()
        return
    con.commit()
    print("Updated Successfully!")
    con.close()
def delete_drive():
    con=connect_db()
    cur=con.cursor()
    d_id=int(input("Enter ID: "))
    query="delete from placement_drive where Drive_id=%s"
    cur.execute(query,(d_id,))
    con.commit()
    print("Deleted Successfully!")
    con.close()
