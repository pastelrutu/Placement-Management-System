import pymysql

def connect_db():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="placementdb"
    )

    return conn


    
