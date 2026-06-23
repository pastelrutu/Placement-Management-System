from database import connect_db

def add_company():
    con=connect_db()
    cur=con.cursor()
    company_name=input("Enter Company name: ")
    package=float(input("Enter Package: "))
    min_cgpa=float(input("Enter Minimum CGPA: "))
    location=input("Enter Location of Company: ")

    query="insert into company(Company_Name,Company_Package,Min_CGPA,Location) values(%s,%s,%s,%s)"
    values=(company_name,package,min_cgpa,location)
    cur.execute(query,values)
    con.commit()
    print("Company Details added successfully!")
    con.close()

def view_company():
    con=connect_db()
    cur=con.cursor()
    cur.execute("select*from company")
    data=cur.fetchall()
    for i in data:
        print("Company ID :", i[0])
        print("Company Name :", i[1])
        print("Company Package :", float(i[2]))
        print("Minimum CGPA :", float(i[3]))
        print("Location :", i[4])
        print("="*30)
    con.close()
def update_company():
    con=connect_db()
    cur=con.cursor()
    c_id=int(input("Enter Company Id: "))
    print("1. Update Name")
    print("2. Update Package")
    print("3. Update minimum CGPA requirement")
    print("4. Update Location ")

    ch=int(input("Enter your choice: "))

    if ch==1:
        new_name=input("Enter Company Name: ")
        query="update company set Company_Name=%s where Company_id=%s"
        cur.execute(query,(new_name, c_id))
    elif ch==2:
        new_package=float(input("Enter Package:"))
        query="update company set Company_Package=%s where Company_id=%s"
        cur.execute(query,(new_package,c_id))
    elif ch==3:
        new_min_cgpa=float(input("Enter the minimum CGPA: "))
        query="update company set Min_CGPA=%s where Company_id=%s"
        cur.execute(query,(new_min_cgpa, c_id))
    elif ch==4:
        new_loc=input("Enter New Location: ")
        query="update company set Location=%s where Company_id=%s"
        cur.execute(query,(new_loc,c_id))
    else:
        print("Invalid Choice!")
        con.close()
        return
    con.commit()
    print("Updated Successfully!")
    con.close()

def delete_company():
    con=connect_db()
    cur=con.cursor()
    c_id=int(input("Enter ID to delete: "))
    query="delete from company where Company_id=%s"
    cur.execute(query,(c_id,))
    con.commit()
    print("Company record has deleted successfully!")
    con.close()
