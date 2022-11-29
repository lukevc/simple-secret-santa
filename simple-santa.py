"""
EZ Secret Santa

Algorithm:
 1. list of persons in "hat" ~ ["giver", "reciever"]
 2. shuffle list
 3. take "reciever" and give it to next person
 4. each index of persons output to a seperate text file with the name of the "giver"
"""

import random
from dataclasses import dataclass


@dataclass()
class Person:
    giver: str
    reciever: str


def PopulateList():
    person1 = Person("Ana", "Ana")
    person2 = Person("Jack", "Jack")
    person3 = Person("Vince", "Vince")
    person4 = Person("Zelda", "Zelda")
    person5 = Person("Jane", "Jane")
    person6 = Person("Sally", "Sally")
    person7 = Person("Denis", "Denis")
    
    persons = [person1, person2, person3, person4, person5, person6, person7]
    return persons


def GenerateSantas(persons):
    
    random.shuffle(persons)

    for x in range(len(persons) - 1):
        persons[x].reciever = persons[x + 1].reciever

    persons[len(persons) - 1].reciever = persons[0].giver

    #print(persons)
    return persons


def WritetoFile(persons):
    for person in persons:
        with open(person.giver + ".txt", "w") as file:
            file.write(person.reciever)


def main():
    persons = GenerateSantas(PopulateList())
    WritetoFile(persons)


if __name__ == "__main__":
    main()