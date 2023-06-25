import random
from choice_loop import choice

choice("to generate random features for you character")

class Human():
    def __init__(self, name, gender, pronoun1, pronoun2):
        self.name = input("\nWhat is the name of your character? ")
        print(f"Great! Your character's name is {self.name}")
        while True:
            print(f"\nWhat is {self.name}'s gender? Please select from the following:")
            genders = ["\n1. Male", "2. Female", "3. Other"]
            for gen in genders:
                print(gen)
            self.gender = input(f"\n")
            self.gender = self.gender.lower()
            if self.gender == "male" or self.gender == "1":
                self.pronoun1 = "he"
                self.pronoun2 = "him"
                print(f"{self.name} is a male, and their pronouns are: {self.pronoun1}/{self.pronoun2}")
                break
            elif self.gender == "female" or self.gender == "2":
                self.pronoun1 = "she"
                self.pronoun2 = "her"
                print(f"{self.name} is a female, and their pronouns are: {self.pronoun1}/{self.pronoun2}")
                break
            elif self.gender == "other" or self.gender == "3":
                self.gender = input("What is your gender? ")
                self.pronoun1 = input("Ok, please enter your first preferred pronoun: ")
                self.pronoun2 = input("Now, enter your second preferred pronoun: ")
                print(f"Ok, your gender is {self.gender}, and your pronouns are {self.pronoun1}/{self.pronoun2}")
                break
            else:
                print("\nYou have made an error. If you would like a male character, ")
                print("please enter the following: male")
                print("Otherwise for a female character, enter female")
                print("And if you wish to have a different gender, then please enter other")
                continue


    def name(self):
        return self.name

    def gender(self):
        return self.gender

    def pronoun1(self):
        return self.pronoun1

    def pronoun2(self):
        return self.pronoun2

    def message(self):
        print("\nNow, let's print out random features for your character: ")

    def facial_hair(self):
        ans = ["\nYes", "No"]
        while True:
            print(f"\nWould you like {self.name} to have facial hair? ")
            for a in ans:
                print(a)
            facial = "\n"
            facial = facial.lower()
            if facial == "yes":
                print(f"{self.name} has facial hair")
                break
            elif facial == "no":
                print(f"{self.name} does not have facial hair")
                break
            else:
                print("you made an error. please enter yes or no")
                continue

    def age(self, age):
        self.age = age
        print(f"\n{self.name}'s age is:")
        print(self.age)

    def hair_type(self, num):
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

    def hair_length(self, length):
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

    def hair_color(self, color):
        self.color = color
        print("\nHair color is:")
        if self.age >= 65:
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
        elif self.color == 8:
            print("White")

    def height(self, height_num):
        self.height_num = height_num
        def height_info(name, height):
            print(f"{name}'s height is {height}")
        print(f"\n{self.name}'s height:")
        if self.height_num == 1:
            height_info(self.name, "short")
        elif self.height_num == 2:
            height_info(self.name, "average")
        elif self.height_num == 3:
            height_info(self.name, "tall")

class Elf(Human):
    def wings(self, wing):
        print("Wings")
        self.wing = wing
        if self.wing == 1:
            print("Your elf has wings")
        elif self.wing == 2:
            print("Your elf does not have wings")

    def ears(self):
        print("All elves are born with pointy ears,")
        print("so your character will have it be default")

    def elf_magic(self, magic):
        self.magic = magic
        print("Elves are proficient at all types of magic")
        print(f"Your character, {name()} will be proficient at:")
        if self.magic == 1:
            print("Ice magic")
        elif self.magic == 2:
            print("Fire Magic")
        elif self.magic == 3:
            print("Nature Magic")
        elif self.magic == 4:
            print("Earth Magic")
        elif self.magic == 5:
            print("Healing Magic")
        elif self.magic == 6:
            print("Light Magic")
        elif self.magic == 7:
            print("Dark Magic")

human_random_age = random.randint(5, 100)
human_random_hair_type = random.randint(1, 8)
human_random_length = random.randint(1, 5)
human_random_hair_color = random.randint(1, 8)
human_random_height = random.randint(1, 3)

elf_random_age = random.randint(5, 100)
elf_random_length = random.randint(1, 5)
elf_random_hair_color = random.randint(1, 8)
elf_random_height = random.randint(1, 3)
elf_random_magic = random.randint(1, 7)



# human1 = Human("\n", "\n", "\n", "\n")
# print(human1)

def action():
    action1 = "To begin please enter the species of your character to be:"
    print(action1)
    species_list = ["\nHuman", "Elf", "Orc", "Merfolk", "Vampires", "Undead"]
    for s in species_list:
        print(s)

    while True:
        print("Please select a species from the list above")
        species = input("\n")
        species = species.lower()
        if species == "human":
            print(f"\nYou've selected you character's species to be {species.lower()}")
            human1 = Human("\n", "\n", "\n", "\n")
            print(human1)
            human1.facial_hair()
            human1.message()
            human1.age(human_random_age)
            human1.hair_type(human_random_hair_type)
            human1.hair_length(human_random_hair_type)
            human1.hair_color(human_random_hair_color)
            human1.height(human_random_height)
            break
        else:
            print("ERROR!")
            print("Please select from the following list")
            for s in species_list:
                print(s)
            continue

action()
