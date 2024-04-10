from characters import basicAttr, physAttributes
from utils import InchtoFt
import random


class Character:
    def __init__(self, firstname, lastname, gender, age, bday, height, weight, physical_attributes):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.birthday = bday
        self.height = height
        self.weight = weight
        self.physical_Attributes = physical_attributes

    def getName(self):
        return f"{self.firstname} {self.lastname}"

    def getFirst(self):
        return f"{self.firstname}"

    def getLast(self):
        return f"{self.lastname}"

    def getBday(self):
        return self.birthday
    
    def getAge(self):
        return self.age
    def display_attributes(self):
        print(f"Character Attributes: ")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Birthday: {self.birthday}")
        print()


def generateRandomBirthday(age):
    current_year = 2500
    year_of_birth = current_year - age

    months = list(range(1, 13))
    days_in_month = {
        1: 31,  # January
        2: 28,  # February (assuming non-leap year)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31   # December
    }

    # Randomly select a month
    birth_month = random.choice(months)

    # Randomly select a day within the valid range for the selected month
    birth_day = random.randint(1, days_in_month[birth_month])
    bday = str(birth_month) + "/" + str(birth_day) + "/" + str(year_of_birth)
    return bday


def generateAge():
    age = random.randint(18, 90)
    return age


def create_character():
    firstname, lastname, gender = basicAttr.setNameGender()
    age = generateAge()
    bday = generateRandomBirthday(age)
    height, weight = physAttributes.setHeightWeight(gender)
    race = random.choice(["African", "European", "Asian", "Latino"])
    eye_color, hair_color, hair_style, skin_tone = physAttributes.randGenAttributes(gender, race)
    physical_attributes = physAttributes.PhysicalAttributes(race, height, weight, eye_color, hair_color, hair_style, skin_tone)
    person = Character(firstname, lastname, gender, age, bday, height, weight, physical_attributes)
    return person
