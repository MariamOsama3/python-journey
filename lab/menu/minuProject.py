import re

class Project:
    def __init__(self, email="m@.nom", password="m", title="title", details="details", totaltarget=111, starttime='10/10/2001', endtime='10/10/2001'):
        self.title = title
        self.details = details
        self.totaltarget = totaltarget
        self.starttime = starttime
        self.endtime = endtime
        self.email = email
        self.password = password

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if valid :
            self.__email=email
        else :
            print("the email is not valid (email should have format using anyexample@anyexample.com)")   
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self,password):
        self.__password=password
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title and not title.isspace():
            self.__title = title
        else:
            print("Title should be a non-empty string.")

    @property
    def details(self):
        return self.__details

    @details.setter
    def details(self, details):
        if details and not details.isspace():
            self.__details = details
        else:
            print("Details should be a non-empty string.")

    @property
    def totaltarget(self):
        return self.__totaltarget

    @totaltarget.setter
    def totaltarget(self, totaltarget):
        if isinstance(totaltarget, int) and totaltarget > 0:
            self.__totaltarget = totaltarget
        else:
            print("Total target should be a positive integer.")

    @property
    def starttime(self):
        return self.__starttime

    @starttime.setter
    def starttime(self, starttime):
        if re.match(r"\d{2}/\d{2}/\d{4}", starttime):
            self.__starttime = starttime
        else:
            print("Start time should be in the format 'DD/MM/YYYY'.")

    @property
    def endtime(self):
        return self.__endtime

    @endtime.setter
    def endtime(self, endtime):
        if re.match(r"\d{2}/\d{2}/\d{4}", endtime):
            self.__endtime = endtime
        else:
            print("End time should be in the format 'DD/MM/YYYY'.")
    
    def saveprojectinfile(self):
        appendto=open("project.txt","a")
        appendto.write(str(self.__dict__)+"\n")
        appendto.close()

    def modify_Project(self):
        print("if you want new modify enter (Enter) if you finish modification enter e  ")   
        while True :
            choice =input("")
            if choice=='e':
                break
            attributeTomodify=input("enter what attripute you wont to modify  ")
                #modify target
                
            if attributeTomodify=="totaltarget":
                while True :
                    newValue=input("enter new value  ")
                    if newValue.isdigit:
                        newValue=int(newValue)
                        setattr(self, attributeTomodify, newValue)
                        print(attributeTomodify ,"have mpdify succesfuly")
                        self.saveprojectinfile()
                        break
                    else:
                        print("target should be degit number")

            # modify details 

            elif attributeTomodify=="details":
                while True :
                    newValue=input("enter new value  ")
                    if attributeTomodify and not attributeTomodify.isspace():
                        setattr(self, attributeTomodify, newValue)
                        print(attributeTomodify ,"have mpdify succesfuly")
                        self.saveprojectinfile()
                        break
                    else:
                        print("details should be string and not null")

            # modify date 

            elif attributeTomodify=="starttime" or attributeTomodify== "endtime" :
                while True :
                    newValue=input("enter new value")
                    if re.match(r"\d{2}/\d{2}/\d{4}", newValue):
                        setattr(self, attributeTomodify, newValue)
                        print(attributeTomodify ,"have mpdify succesfuly")
                        self.saveprojectinfile()
                        break
                    else :
                        print("date should be in format 'DD/MM/YYYY' ")
            else:
                print("there is not attribute in that name try again")
                self.saveprojectinfile()
    def readfromfile(self):
        projects=[]
        projects=open("project.txt","r")
        projects.close()

def searchifuseristheowner(email,password,title):
    try:
        with open("project.txt", "r") as file:
            for line in file:
                if re.search(rf"'_Project__email': '{email}', '_Project__password': '{password}', '_Project__title': '{title}'", line):
                    print("You are the owner")
                    return True
        print(f"Checking line: {line.strip()}")
        print(f"Using regex: {rf"'_Project__email': '{email}', '_Project__password': '{password}', '_Project__title': '{title}'"}")
        return False
    except FileNotFoundError:
        print("Can't open the file.")
        return False
        
pro1 =Project()
pro1.title="mariam"
pro1.details="mmmmm"
pro1.email="m@m.com"
pro1.password="1234"

pro1.saveprojectinfile()

searchifuseristheowner("m@m.com","1234","mariam")