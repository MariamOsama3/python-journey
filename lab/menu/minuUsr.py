
import re
class usr :
    #constarct to take the value the constract should take self at first
    def __init__(self,firstname="A", lastname="A",password="124@Mm",email="mm@gmail.com",mopilephone="+2123456789"):
        self.firstname=firstname
        self.lastname=lastname
        self.password=password
        self.email=email
        self.mopilephone=mopilephone

    #check if the name is string and not null
    def checkFName(self):
        name =self.firstname
        if name and not name.isspace():
            print("valid first name")
            return True
        else :
            print("invalid first name (the name should contain string only and not be null)")
            return False
        
    def checkLName(self):
        name =self.lastname
        if isinstance(name,str) and name is not None:
            print("valid first name")
            return True
        else :
            print("invalid last name (the name should contain string only and not be null)")
            return False
        
        #check if the email is match the formula
    def checkEmail(self):
        emails = self.email
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', emails)
        if valid :
            print("email is valid")
            return True
        else :
            print("the email is not valid (email should have format using anyexample@anyexample.com)")   
            return False
        #to check if the email used pefor and check first to open the file
    def checkIfEmailIsUse(self):
        emails = self.email
        try:
            with open("user.txt", "r") as file:
                for line in file:
                    # Check if the email is already in the file
                    if f"'email': '{emails}'" in line:
                        print("Invalid email: This email is already in use.")
                        return False
                    return True
        except FileNotFoundError:
            print("can't open the file")
        #check if password is used pefor or not 
    def checkPasswordIsUseTologin(self):
        passWrd = self.password
        try:
            with open("user.txt", "r") as file:
                for line in file:
                    if f"'password': '{passWrd}'" in line:  # Check if the email is already in the file
                        return False
                    return True
        except FileNotFoundError:
            print("can't open the file")

        #check email to login 
    def checkIfEmailIsUseTologin(self):
        newemail = self.email
        try:
            with open("user.txt", "r") as file:
                for line in file:
                    if f"'email': '{newemail}'" in line:  # Check if the email is already in the file
                        return False
                    return True
        except FileNotFoundError:
            print("can't open the file")
        #check if the password is not strong
    def checkifpassisvalid(self):
        password = self.password
        flag = 0
        while True:
            if (len(password)<=8):
                print("invalid password should de more than 8")
                return False
            elif not re.search("[a-z]", password):
                print("invalid password should contain [a-z]")
                return False
            elif not re.search("[A-Z]", password):
                print("invalid password should contain [A-Z]")
                return False
            elif not re.search("[0-9]", password):
                print("invalid password should contain [0-9]")
                return False
            elif not re.search("[_@$]" , password):
                print("invalid password should contain speacial character")
                return False
            elif re.search(r"\s" , password):
                print("invalid password shouldn't contain any spaces")
                return False
            else:
                print("Valid Password")
                return True
            
        # first i install the phonenumber package then check it
    def checkMobileIsValid(self):
        import phonenumbers 
        phone = self.mopilephone
        parsed_number = phonenumbers.parse(phone)
        if phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number):
            print("Valid mobile number.")
            return True
        else:
            print("Invalid mobile number.")
            return False
    def saveinfile(self):
        appendto=open("user.txt","a")
        appendto.write(str(self.__dict__))
        appendto.close()

