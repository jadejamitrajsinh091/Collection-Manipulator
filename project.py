student=[{"id":1,"name":"ruchit","Age":20,"Grade":"A","birthdate":"2003-01-15","subject":"social science, Science,zoology,biology"}]



while True:
    print("\nwelcome to the Student Data Organizer!\n")

    print("select an option:")
    print("1. add student")
    print("2. Display All students")
    print("3. Update student Information")
    print("4. Delete student ")
    print("5. Display subjects offered")
    print("6. Exit")

    Choice=input("\nEnter your Choice\n")

    if(Choice == "1"):
        id=len(student)+1
        name= input("enter your name:")
        Age= int(input("enter your age:"))
        Grade=input("Enter your grade:")
        birth_Date=input("Enter your Date of Birth (YYYY-MM-DD):")
        subject=input("Enter your subjects (comma-separated):")

        student.append({"id":id,"name":name,"Age":Age,"Grade":Grade,"birth_date":birth_Date,"subject":subject})

        print("student added successfully!")
    
    elif(Choice == "2"):
        
        if(student == []):
            print("No student data found")
        else:
            for s in student:
                print("id:",s["id"],"name:",s["name"],"Age:",s["Age"],"Grade:",s["Grade"],"Date of Birth:",s["birth_date"],"Subjects:",s["subject"])
  

    elif(Choice == "3"):
        sId = int(input("enter student id to update "))

        for m in student:
            if(m["id"] == sId):
                m["name"] =input("enter new student data to update ")
                m["Age"] =int(input("enter student Age to update "))
                m["Grade"] =input("enter new Grade to update ")
                m["birthdate"] =input("enter new student birth-date to update ")
                m["subject"] =input("enter new subject to update ")
                print("student data updated")
                break
        else:
            print("student not found")             

    elif(Choice == "4"):
        sId = int(input("enter student id to delete "))
        for x in student:
            if(x["id"]==sId):
                student.remove(x)
                print("student data deleted")
                break
        else:
            print("student not found")
    elif(Choice == "5"):
        if not student:
            print("No student data found")
        else:
            subjects_set = set()
            for p in student:
                subjects = p["subject"].split(",")
            for subj in subjects:
                    subjects_set.add(subj.strip())
            print("Subjects offered:")
            for subj in subjects_set:
                print(subj)

    
    elif(Choice == "6"):
        print("good bye")
        break;       

    else:
        print("invalid choice, choose correctly")            





