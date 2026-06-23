from student import*
from company import*
from drive import*
from application import*
from reports import*

def main_menu():
    while True:

        print("="*30)
        print("1. Student Management")
        print("2. Company Management")
        print("3. Application Management")
        print("4. Placement Drive")
        print("5. Selection Status")
        print("6. Exit")

        ch=int(input("Enter Choice: "))

        if ch==1:

            while True:

                print("\n =====Student Management=====")
                print("1. Add Student")
                print("2. View Student")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Back")

                stud_choice=int(input("Enter CHoice: "))
                if stud_choice==1:
                    add_student()
                elif stud_choice==2:
                    view_student()
                elif stud_choice==3:
                    update_student()
                elif stud_choice==4:
                    delete_student()
                elif stud_choice==5:
                    break
                else:
                    print("Invalid Choice!")

        elif ch==2:

            while True:

                print("\n =====Company Management=====")
                print("1. Add Company")
                print("2. View Company")
                print("3. Update Company")
                print("4. Delete Company")
                print("5. Back")

                stud_choice=int(input("Enter CHoice: "))
                if stud_choice==1:
                    add_company()
                elif stud_choice==2:
                    view_company()
                elif stud_choice==3:
                    update_company()
                elif stud_choice==4:
                    delete_company()
                elif stud_choice==5:
                    break
                else:
                    print("Invalid Choice!")

        elif ch==3:

            while True:
                print("\n =====Application Management=====")
                print("1. Apply for Company")
                print("2. View Application")
                print("3. Update Application")
                print("4. Delete Application")
                print("5. Back")

                stud_choice=int(input("Enter Choice: "))

                if stud_choice==1:
                    apply_company()
                elif stud_choice==2:
                    view_application()
                elif stud_choice==3:
                    update_application()
                elif stud_choice==4:
                    delete_application()
                elif stud_choice==5:
                    break
                else:
                    print("Invalid Choice!")

        elif ch==4:

            while True:
                print("\n =====Placement Drive Management=====")
                print("1. Add Drive")
                print("2. View Drive")
                print("3. Update Drive")
                print("4. Delete Drive")
                print("5. Back")

                stud_choice=int(input("Enter Choice: "))
                if stud_choice==1:
                    add_drive()
                elif stud_choice==2:
                    view_drive()
                elif stud_choice==3:
                    update_drive()
                elif stud_choice==4:
                    delete_drive()
                elif stud_choice==5:
                    break
                else:
                    print("Invalid Choice!")

        elif ch==5:
            select_choice_menu()

        elif ch==6:
            print("THANKYOU!")
            return

        else:
            print("Invalid Choice!")

main_menu()