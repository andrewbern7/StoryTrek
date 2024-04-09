import random

# WIP NEED TO LEARN JSON filetype for easier more optimized queries.
def getNameGender():
    gender = getGender()
    name = getFirst(gender)
    last = getsurname()
    return name, last, gender

def getsurname():
    filename = "surnames.txt"
    randQuery = random.randint(1, 10000)
    try:
        with open("data/" + filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if line_number == randQuery:
                    randomName = line.strip()
                    return randomName
    except FileNotFoundError:
        print("Error: " + filename + " not found in /data dir...")
    return "ERROR"

def getGender():
    gender = random.choice(["Male", "Female"])
    return gender

def getFirst(gender):
    randQuery = random.randint(1, 5000)
    if gender == "Male":
        filename = "male_names.txt"
    else:
        filename = "female_names.txt"
    try:
        with open("data/" + filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if line_number == randQuery:
                    randomName = line.strip()
                    return randomName
    except FileNotFoundError:
        print("Error: " + filename + " not found in /data dir...")
    return "ERROR"

