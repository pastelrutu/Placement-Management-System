import pymysql

def connect_db():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="placement_db"
    )

    print("Student Added Successfully!")

    
