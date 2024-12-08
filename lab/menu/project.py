import re
class project:
    def __init__(self, email="",title="title", details="details", totaltarget=111, starttime='10/10/2001', endtime='10/10/2001'):
        self.title = title
        self.details = details
        self.totaltarget = totaltarget
        self.starttime = starttime
        self.endtime = endtime
        self.email=email

    def checkTitle(self):
        title = self.title
        if title and not title.isspace():
            print("Valid title")
            return True
        else:
            print("Invalid title (the title should contain string only and not be null)")
            return False

    def checkDetails(self):
        details = self.details
        if details and not details.isspace():
            print("Valid details")
            return True
        else:
            print("Invalid details (the details should contain string only and not be null)")
            return False

    def checkTarget(self):
        target = self.totaltarget
        if target.isdigit:
            print("Valid target")
            return True
        else:
            print("Total target should be a positive integer.")
            return False

    def checkstartdate(self):
        date = self.starttime
        if re.match(r"\d{2}/\d{2}/\d{4}", date):
            print("Valid date")
            return True
        else:
            print("Invalid date (Start time should be in the format 'DD/MM/YYYY').")
            return False

    def checkenddate(self):
        date = self.endtime
        if re.match(r"\d{2}/\d{2}/\d{4}", date):
            print("Valid date")
            return True
        else:
            print("Invalid date (end time should be in the format 'DD/MM/YYYY').")
            return False

    def saveinfile(self):
        with open("newproject.txt", "a") as appendto:
            appendto.write(str(self.__dict__) + "\n")

    def checkIfTitleIsUse(self):
        title =self.title
        try:
            with open("newproject.txt", "r") as file:
                for line in file:
                    # Check if the title is already in the file
                    if f"'title': '{title}'" in line:
                        print("Invalid title: This title is already in use.")
                        return False
            return True
        except FileNotFoundError:
            print("Can't open the file")
            return False

    def modify_Project(self):
        while True:
            choice = input("Enter 'e' to exit or press Enter to continue: ").strip()
            if choice == 'e':
                print("Exiting modification process.")
                break

            attribute_to_modify = input("Enter the attribute you want to modify ('totaltarget', 'details', 'starttime', 'endtime'): ").strip()

            # to Check if the attribute exists in the object
            if attribute_to_modify in self.__dict__:

                # Modify 'totaltarget'
                if attribute_to_modify == "totaltarget":
                    while True:
                        new_value = input("Enter new value for 'totaltarget' (must be a positive integer): ").strip()
                        if new_value.isdigit():
                            new_value = int(new_value)
                            setattr(self, attribute_to_modify, new_value)
                            print(f"'{attribute_to_modify}' has been successfully updated to {new_value}.")
                            self.saveinfile()
                            break
                        else:
                            print("Invalid input. 'totaltarget' must be a positive integer.")

                # Modify 'details'
                elif attribute_to_modify == "details":
                    while True:
                        new_value = input("Enter new value for 'details': ").strip()
                        if new_value and not new_value.isspace():
                            setattr(self, attribute_to_modify, new_value)
                            print(f"'{attribute_to_modify}' has been successfully updated to '{new_value}'.")
                            self.saveinfile()
                            break
                        else:
                            print("Invalid input. 'details' cannot be empty or only spaces.")

                # Modify 'starttime' or 'endtime'
                elif attribute_to_modify in ["starttime", "endtime"]:
                    while True:
                        new_value = input(f"Enter new value for '{attribute_to_modify}' (format: DD/MM/YYYY): ").strip()
                        if re.match(r"\d{2}/\d{2}/\d{4}", new_value):
                            setattr(self, attribute_to_modify, new_value)
                            print(f"'{attribute_to_modify}' has been successfully updated to '{new_value}'.")
                            self.saveinfile()
                            break
                        else:
                            print("Invalid date format. Please use 'DD/MM/YYYY'.")

                else:
                    print(f"'{attribute_to_modify}' is not a recognized modifiable attribute.")

            else:
                print(f"'{attribute_to_modify}' does not exist in the project. Please try again.")

    def showAllProjects(self):
        try:
            with open("newproject.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip()) 
        except FileNotFoundError:
            print("The file 'newproject.txt' does not exist.")

    def deletproject(self):
        try:
            with open("newproject.txt", "r") as file: 
                lines = file.readlines() #first read the file

            selectedopjected = str(self.__dict__) #take the opject need to delete

            theotherlines = [line for line in lines if line.strip() != selectedopjected] #the line is not the line that you need to delete

            with open("newproject.txt", "w") as file:
                file.writelines(theotherlines) #write the hole file
        except FileNotFoundError:
            print("The file 'newproject.txt' does not exist.")
