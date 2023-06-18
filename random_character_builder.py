import random
from choice_loop import choice

# random numbers for the humans
random_2choice = random.randint(1, 2)
random_haircolor = random.randint(1, 6)
random_age = random.randint(5, 100)
random_hairlength = random.randint(1, 5)
random_height = random.randint(1, 3)

# random numbers for the elves
elf_random_2choice = random.randint(1, 2)
elf_random_haircolor = random.randint(1, 6)
elf_random_age = random.randint(5, 100)
elf_random_hairlength = random.randint(1, 5)
elf_random_height = random.randint(1, 3)

choice("generate a random custom character")

class Human():
    def __init__(self, name, gender):
        self.name = input('\nWhat is the name of your character? ')
        print(f"Ok, your character's name is {self.name}")
        while True:
            self.gender = input(f"\nWhat is {self.name}'s gender? ")
            self.gender = self.gender.lower()
            if self.gender == "male" or self.gender == 'boy' or self.gender == 'guy' or self.gender == "man":
                print(f"{self.name} is a male")
                break
            elif self.gender == "female" or self.gender == "girl" or self.gender == "gal" or self.gender == "woman":
                print(f"{self.name} is a female")
                break
            else:
                print("\nYou have made an error. If you would male character, ")
                print("please select the following: male, boy, guy, or man")
                print("otherwise for a female character, please select female, girl, gal, or woman")
                continue

    @property
    def getName(self):
        return self.name

    @property
    def getGender(self):
        return self.gender

    # def hisOrHer(self, his_or_her):
    #     self.his_or_her = his_or_her
    #     if self.gender == "male":
    #         self.his_or_her = "him"
    #     elif self.gender == "female":
    #         self.his_or_her = "her"

    def message(self):
        print("\n-----------Great! now that we have that information-----------")
        print("-----------I will generate random features for you character:------------")

    def age(self, age):
        self.age = age
        print(f"\n{self.name}'s age is:")
        print(self.age)

    def hairType(self, num):
        self.num = num
        print("\nHair type:")
        if self.num == 1:
            print(f"{self.name}'s hair is curly")
        elif self.num == 2:
            print(f"{self.name}'s hair is straight")
        elif self.num == 3:
            print(f"{self.name}'s hair is spiky")
        elif self.num == 4:
            print(f"{self.name}'s hair is frizzy")
        elif self.num == 5:
            print(f"{self.name}'s hair is kinky")
        elif self.num == 6:
            print(f"{self.name}' hair is nappy")
        elif self.num == 7:
            print(f"{self.name}'s hair is wavy")
        elif self.num == 8:
            print(f"{self.name}'s hair is colly")

    def hairLength(self, length):
        self.length = length
        def hairLength2(name, length1):
            msg = f"{name}'s hair is {length1}"
            print(msg)
        print("\nHair length:")
        if self.length == 1:
            hairLength2(self.name, "very short")
        if self.length == 2:
            hairLength2(self.name, "short")
        if self.length == 3:
            hairLength2(self.name, "medium in length")
        if self.length == 4:
            hairLength2(self.name, "long")
        if self.length == 5:
            hairLength2(self.name, "very long")

    def hairFacial(self, facial):
        print(f"\nDoes {self.name} have facial hair?")
        self.facial = facial
        self.gender = self.gender.lower()
        if self.gender == "female":
            print(f"No, {self.name} has no facial hair because she is a female")
        elif self.facial == 1:
            print(f"Yes, {self.name} has facial hair")
        elif self.facial == 2:
            print(f"No, {self.name} has no facial hair")


    def hairColor(self, color):
        self.color = color
        print("\nHair color is:")
        if self.age >= 65 or self.color == 8:
            print(f"White, because {self.name} is {self.age}.")
        elif self.color == 1:
            print("Red")
        elif self.color == 2:
            print('Blue')
        elif self.color == 3:
            print("Yellow")
        elif self.color == 4:
            print("Green")
        elif self.color == 5:
            print("Orange")
        elif self.color == 6:
            print("Purple")
        elif self.color == 7:
            print("Black")

    def height(self, height_num):
        self.height_num = height_num
        def height_info(name, height):
            print(f"{name}'s hieght is {height}")
        print(f"\n{self.name}'s height:")
        if self.height_num == 1:
            height_info(self.name, "short")
        elif self.height_num == 2:
            height_info(self.name, "avergae")
        elif self.height_num == 3:
            height_info(self.name, "tall")


    def __repr__(self):
        return "\n---------This is a randomly generated character of a human----------"


class Elf(Human):
    def specialAttribute(self, attribute):
        self.attribute = attribute
        print(f"\n{self.name}'s attribute:")
        print(self.attribute)

    def ears(self):
        print(f"\nSince {self.name} is an elf, their ears are pointy")

    def __repr__(self):
        elf_repr = super().__repr__()
        return f"{elf_repr}---------This is a randomly generated character of an elf----------"


human1 = Human('\n', "\n")
print(human1)

human1.message()
human1.age(random_age)
human1.hairLength(random_hairlength)
human1.hairType(random_2choice)
human1.hairFacial(random_2choice)
human1.hairColor(random_haircolor)
human1.height(random_height)

elf1 = Elf("\n", "\n")
print(elf1)

elf1.specialAttribute("Great Magical Capabilities")
elf1.message()
elf1.age(elf_random_age)
elf1.hairLength(elf_random_hairlength)
elf1.hairType(elf_random_2choice)
elf1.hairFacial(elf_random_2choice)
elf1.hairColor(elf_random_haircolor)
elf1.height(elf_random_height)
elf1.ears()