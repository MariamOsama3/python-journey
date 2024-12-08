import project
import minuUsr
#import searchingfun
print("\nMain Menu enter 1. to regression 2. to login")
while True:
    print("1. Register")
    print("2. Login")
    print("3. search using date")
    choice =input("enter choice ")
    if choice=='1' :
        user =minuUsr.usr()
        flage1=0
        flage2=0
        flage3=0
        flage4=0
        flage5=0
        while flage1==0:
            user.firstname=input("enter user first name  ")
            if user.checkFName()==False:
                flage1=0
            else:
                flage1=1
        while flage2==0:
            user.lastname=input("enter user last name  ")
            if user.checkLName()==False:
                flage2=0
            else:
                flage2=1

        while flage3==0:
            user.password=input("enter user password  ")
            if user.checkifpassisvalid()==False:
                flage3=0
            else:
                flage3=1

        while flage4==0:
            user.email=input("enter user email  ")
            if user.checkEmail()==False or user.checkIfEmailIsUse()==False:
                flage4=0
            else:
                flage4=1
        while flage5==0:
            user.mopilephone=input("enter user mobile phone  ")
            if user.checkMobileIsValid()==False:
                flage5=0
            else:
                flage5=1
        user.saveinfile()
    elif choice=='2':
        user1=minuUsr.usr()
        flage6 =0
        flage7 =0
        while flage6==0:
            user1.email=input("enter user email  ")
            if  user1.checkIfEmailIsUseTologin()==True:
                print("cant find that email that email try again")
                flage6=0
            else:
                flage6=1 
        while flage7==0:
            user1.password=input("enter user password  ")
            if  user1.checkPasswordIsUseTologin()==True:
                flage7=0
                print("wrong password try again")
            else:
                flage7=1
        proj =project.project()
        proj.email=user1.email
        print("enter project information  ")
        flage8=0
        flage9=0
        flage10=0
        flage11=0
        flage12=0
        while flage8==0:
            proj.title=input("enter project title  ")
            if proj.checkTitle()==True and proj.checkIfTitleIsUse()==True:
                flage8=1
            else:
                flage8=0
        while flage9==0:
            proj.details=input("enter project detail  ")
            if proj.checkDetails()==True:
                flage9=1
            else:
                flage9=0
        while flage10==0:
            proj.starttime=input("enter the project start date  ")
            if proj.checkstartdate()== True:
                flage10=1
            else:
                flage10=0
        while flage11==0:
            proj.endtime=input("enter the project end date  ")
            if proj.checkenddate()==True:
                flage11=1
            else:
                flage11=0
        while flage12==0:
            proj.totaltarget=input("enter total target")
            if proj.checkTarget()==True:
                flage12=1
            else :
                flage12=0
        proj.saveinfile()
        while True:
            choice2=input("1. if you want to modify your project press 1 \n\n2. if you want to shaw all projects press 2 \n\n3. if you want to remove the project press 3\n\n4. if you want to end press e\n")
            if choice2=='1':
                proj.modify_Project()
            if choice2=='2':
                proj.showAllProjects()
            if choice2=='3':
                proj.deletproject()
            if choice2=='e':
                break

    elif choice=='3':
        file_path = 'newproject.txt'
        search_string=input("enter date want to search about \n ")
        with open(file_path, 'r') as file: 
            for line_number, line in enumerate(file, start=1): 
                if search_string in line: 
                    print(f'Found "{search_string}" in line {line_number}: {line.strip()}') 
                else:
                    print(f"cannt found {search_string} in the file" )

