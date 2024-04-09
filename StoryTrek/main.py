import random
from utils import randomNameGender
from characters import character


def create_character():
    firstname, lastname, gender = randomNameGender.getNameGender()

    person = character.Character(firstname, lastname, gender)
    return person


def main():
    user = create_character()
    print("Character: " + user.getName() + "\n")
    print("Character Attributes:")
    user.display_attributes()


if __name__ == "__main__":
    main()
