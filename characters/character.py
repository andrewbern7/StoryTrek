class Character:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender

    def getName(self):
        return f"{self.firstname} {self.lastname}"

    def getFirst(self):
        return f"{self.firstname} {self.lastname}"

    def getLast(self):
        return f"{self.firstname} {self.lastname}"

    def display_attributes(self):
        print(f"Gender: {self.gender}")