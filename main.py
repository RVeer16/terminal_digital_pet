import json
import random
from datetime import date
import os
import time

pet_happy = r'''
(\___/)
(=^.^=)
(") (")
'''

pet_fine = r'''
(\___/)
(='.'=)
(") (")
'''

pet_sad = r'''
(\___/)
(=╥_╥=)
(") (")
'''

pet_dead = r'''
(\___/)
(=✖_✖=)
~~(") (")
'''

health = 100
pet_said = ""

while True:

    if (health > 100):
        health = 100
        print(pet_happy)

    elif (health >= 75):
        print(pet_happy)

    elif (health >= 50 and health < 75):
        print(pet_fine)

    elif (health <= 0):
        print(pet_dead)
        break

    elif (health < 50):
        print(pet_sad)

    print(pet_said)
    print("""Type A to talk to pet
Type B to enter task management
Type C to check pet health
Type D to see previous conversations
    """)

    operation = input("What do you want to do: ")

    if (operation.lower() != "a" and operation.lower() != "b" and operation.lower() != "c" and operation.lower() != "d"):
        print("Enter valid operation")
        continue
    
    if (operation.lower() == "a"):

        heading = input("Enter heading: ")
        text = input("Enter text: ")

        entry = {

            "date": str(date.today()),
            "heading": heading,
            "text": text            

        }

        if os.path.exists("python_diary.json"):
            with open ("python_diary.json", "r") as f:
                diary = json.load(f)

        else:

            diary = []

        diary.append(entry)

        with open("python_diary.json", "w") as f:
            json.dump(diary, f)

        pet_said = random.choice(["OW", "ow ow", "ni nu", "oni", "nu na na", "nu", "ya"])
        print("\n"*100)

    if (operation.lower() == "b"):

        tasks = []

        while True:
            task = input("Enter task to be completed(or press enter to finish): ")
            
            if (task == ""):
                break
            
            tasks.append(
                {
                    "task": task,
                    "done": False
                }
            )

        print("Tasks added", len(tasks))

        time_limit = float(input("Enter time limit in hours: "))
        start_time = time.time()
            
        completion = input("Enter wheather task is completed(y/n): ")

        if (completion.lower() == "y"):

            end_time = time.time()

            time_taken = (end_time - start_time)/3600

            if (time_taken > time_limit):

                print("You took too much time")
                health = health - 10

            else:
                print("You finished all tasks in time")
                health = health + 5

        else:
            print("You didn't finish your tasks")
            health = health - 20

    if (operation.lower() == "c"):

        print(health)

    if (operation.lower() == "d"):

        if os.path.exists("python_diary.json"):
            with open ("python_diary.json", "r") as f:
                diary = json.load(f)

            for entry in diary:
                print("---")
                print("Date: ", entry["date"])
                print("Heading: ", entry["heading"])
                print("Text: ", entry["text"])

        else:
            print("No entry yet")