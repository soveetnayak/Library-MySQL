import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age

def enterbookdetails(con,cur):

    try:
        row = {}
        author={}
        genre={}
        print("Enter new Book's details: ")

        row["Book_id"] = int(input("Book_id: "))
        if (row["Book_id"] <= 0):
            print("Book_id cannot be <1/NULL")

        row['Book_Name'] = input("Book_Name: ")
        
        row["Edition"] = input("Edition: ")
       
        row["ISBN_value"] = int(input("ISBN_value: "))
        if(row["ISBN_value"] >= 9999999999999 or row["ISBN_value"] <= 1000000000000):
            print("ISBN_value should be 13 digits")
            return
        
        row["Price"] = float(input("Price: "))
        if (row["Price"] <= 0):
            print("Price should be > 0")
            return
        
        row["Publisher_id"] = int(input("Publisher_id: "))
        
        row["Status"] = (input("Status (Available/Borrowed): "))
        if (row['Status'] != "Available" and row['Status'] != "Borrowed"):
            print("Status should be either Available or Borrowed")
            return
        
        auth = int(input("Number of authors: "))
        for i in range(auth):
            author[i] = int(input("Author_id: "))
        gen = int(input("Number of genres: "))
        for i in range(gen):
            genre[i] = int(input("Genre_id: "))


        query = "INSERT INTO Books VALUES(%d, '%s', '%s', %d, %f, %d, '%s' )" % (row["Book_id"], row["Book_Name"], row["Edition"], row["ISBN_value"], row["Price"], row["Publisher_id"], row["Status"])

        print(query)
        cur.execute(query)
        con.commit()

        for i in range(auth):
            query = "INSERT INTO Multi_Authors VALUES(%d, %d)" % (
                author[i], row["Book_id"])
            print(query)
            cur.execute(query)
            con.commit()

        for i in range(gen):
            query = "INSERT INTO Multi_Genres VALUES(%d, %d)" % (
                 genre[i], row["Book_id"])
            print(query)
            cur.execute(query)
            con.commit()
            
        print("Inserted Into Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database!\n")
        print("> ", e)

    return


def entermagazinedetails(con,cur):
    
    try:
        row = {}
        print("Enter new Magazine's details: ")

        row["Magazine_id"] = int(input("Magazine_id: "))
        if (row["Magazine_id"] <= 0):
            print("Magazine_id cannot be <1/NULL")

        row['Magazine_Name'] = input("Magazine_Name: ")
        row['Volume_no'] = int(input("Volume_no: "))
        row["Issue_no"] = int(input("Issue_no: "))
        row["Publisher_id"] = int(input("Publisher_id: "))

        query = "INSERT INTO Magazine VALUES(%d, '%s', %d, %d, %d)" % (row["Magazine_id"], row["Magazine_Name"], row["Volume_no"], row["Issue_no"], row["Publisher_id"])
        print(query)
        cur.execute(query)
        con.commit()
            
        print("Inserted Into Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database!\n")
        print("> ", e)

    return
    
def entermemberdetails(con,cur):
    """
    Function to implement option 3
    """
    age = 0
    try: 
        row = {}
        print("Enter new member's details: ")
        row["Member_id"] = int(input("Member_id: "))
        if (row["Member_id"] <= 0):
            print("Member_id cannot be <1/NULL")
            return
            

        row["Government_id"] = int(input("Government_id: "))
        if (row["Government_id"] <= 0):
            print("Government_id cannot be <1/NULL")
            return

        row["First_Name"] = (input("First_Name: "))
        if (row['First_Name'] == ""):
            print("First_Name cannot be empty")
            return

        row["Last_Name"] = (input("Last_Name: "))
        if (row['Last_Name'] == ""):
            print("Last_Name cannot be empty")
            return

        row["Date_of_birth"] = (input("Date_of_birth (YYYY-MM-DD)): "))
        if (row['Date_of_birth'] == ""):
            print("Date_of_birth cannot be empty")
            return
        
        else :
            temp_dob = [int(x) for x in row["Date_of_birth"].split('-')]
            if (len(temp_dob) != 3):
                print("Date_of_birth is in wrong format1")
                return
            elif (temp_dob[0] < 1900 or temp_dob[0] > 2021):
                print("Date_of_birth is in wrong format")
                return
            elif (temp_dob[1] < 1 or temp_dob[1] > 12):
                print("Date_of_birth is in wrong format")
                return
            elif (temp_dob[2] <= 0 or temp_dob[2] > 31):
                print("Date_of_birth is in wrong format")
                return
            else:
                row["Age"] = calculateAge(date(temp_dob[0], temp_dob[1], temp_dob[2]))
            
    # Age is a derived attribute so we shouldn't take it as input rather we should derive it
    
        # row["Age"] = int(input("Age: "))
        # if (row['Age'] <= 0):
        #     print("Age cannot be negative")
        #     return

        row["House_no"] = input("House_no: ")

        row["Locality"] = input("Locality: ")
        if (row['Locality'] == ""):
            print("Locality cannot be empty")
            return

        row["City"] = input("City: ")
        if (row['City'] == ""):
            print("City cannot be empty")
            return

        row["Pin_Code"] = int(input("Pin_Code: "))
        if (row['Pin_Code'] < 0):
            print("Pin_Code cannot be negative")
            return
        
        mobile = {}
        num = int(input("Number of contact no.: "))
        for i in range(num):
            mobile[i] = int(input("Contact_no: "))
        
        row["Date_of_joining"] = (input("Date_of_joining: "))
        if (row['Date_of_joining'] == ""):
            print("Date_of_jooining cannot be empty")
            return


        row["Membership_expiration"] = (input("Membership_expiration (YYYY-MM-DD): "))
        if (row['Membership_expiration'] == ""):
            print("Membership_expiration cannot be empty")
            return


        query = "INSERT INTO Members VALUES (%d, %d, '%s', '%s', '%s', %d, '%s' , '%s', '%s', %d, '%s', '%s')" % (row["Member_id"], row["Government_id"], row["First_Name"], row["Last_Name"], row["Date_of_birth"], row["Age"], row["House_no"], row["Locality"], row["City"], row["Pin_Code"], row["Date_of_joining"], row["Membership_expiration"])


        print(query)
        cur.execute(query)
        con.commit()

        for i in range(num):
            query = "INSERT INTO Contact_number_Members VALUES(%d, %d)" % (
            row["Member_id"],mobile[i])
            print(query)
            cur.execute(query)
            con.commit()

        print("Inserted Into Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database!\n")
        print("> ", e)

    

def enterstaffdetails(con,cur):

    try: 
        row = {}
        print("Enter new staff's details: ")
        row["Staff_id"] = int(input("Staff_id: "))
        if (row["Staff_id"] <= 0):
            print("Staff_id cannot be negative/NULL")
            return
            

        row["Government_id"] = int(input("Government_id: "))
        if (row["Government_id"] <= 0):
            print("Government_id cannot be negative/NULL")
            return

        row["First_Name"] = (input("First_Name: "))
        if (row['First_Name'] == ""):
            print("First_Name cannot be empty")
            return

        row["Last_Name"] = (input("Last_Name: "))
        if (row['Last_Name'] == ""):
            print("Last_Name cannot be empty")
            return

        row["Date_of_birth"] = (input("Date_of_birth (YYYY-MM-DD)): "))
        if (row['Date_of_birth'] == ""):
            print("Date_of_birth cannot be empty")
            return
        
        else :
            temp_dob = [int(x) for x in row["Date_of_birth"].split('-')]
            if (len(temp_dob) != 3):
                print("Date_of_birth is in wrong format")
                return
            elif (temp_dob[0] < 1900 or temp_dob[0] > 2021):
                print("Date_of_birth is in wrong format")
                return
            elif (temp_dob[1] < 1 or temp_dob[1] > 12):
                print("Date_of_birth is in wrong format")
                return
            elif (temp_dob[2] <= 0 or temp_dob[2] > 31):
                print("Date_of_birth is in wrong format")
                return
            else:
                row["Age"] = calculateAge(date(temp_dob[0], temp_dob[1], temp_dob[2]))
      
    # Age is a derived attribute so we shouldn't take it as input rather we should derive it

        # row["Age"] = int(input("Age: "))
        # if (row['Age'] < 0):
        #     print("Age cannot be negative")
        #     return

        row["House_no"] = input("House_no: ")


        row["Locality"] = (input("Locality: "))
        if (row['Locality'] == ""):
            print("Locality cannot be empty")
            return

        row["City"] = (input("City: "))
        if (row['City'] == ""):
            print("City cannot be empty")
            return

        row["Pin_Code"] = int(input("Pin_Code: "))
        if (row['Pin_Code'] < 0):
            print("Pin_Code cannot be negative")
            return

        mobile = {}
        num = int(input("Number of contact no.: "))
        for i in range(num):
            mobile[i] = int(input("Contact_no: "))

        row["Designation"] = (input("Designation: "))

        row["Duty"] = (input("Duty: "))

        row["Type"] = (input("Type: "))
        if (row['Type'] == ""):
            print("Type cannot be empty")
            return


        query = "INSERT INTO Staff VALUES (%d, %d, '%s', '%s', '%s', %d, '%s' , '%s', '%s',%d, '%s', '%s', '%s')" % (row["Staff_id"], row["Government_id"], row["First_Name"], row["Last_Name"], row["Date_of_birth"], row["Age"], row["House_no"], row["Locality"], row["City"], row["Pin_Code"], row["Designation"], row["Duty"],row["Type"])


        print(query)
        cur.execute(query)
        con.commit()

        for i in range(num):
            query = "INSERT INTO Contact_number_Staff VALUES(%d, %d)" % (
             row["Staff_id"],mobile[i])
            print(query)
            cur.execute(query)
            con.commit()

        print("Inserted Into Database! ")
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database!\n")
        print("> ", e)
        


    