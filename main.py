from characters import character, physAttributes


# def create_character():
#    firstname, lastname, gender = basicAttr.getNameGender()
#
#    person = character.Character(firstname, lastname, gender)
#    return person


def main():
    person = character.create_character()
    print("Character: " + person.getName())
    person.display_attributes()
    person.physical_Attributes.display_physAttributes()

if __name__ == "__main__":
    main()
