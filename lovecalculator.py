import random

def love_calculator(name1, name2):
    print(f"\n Love Calculator ")
    print(f"Calculating love between {name1} and {name2}...\n")
    
    love_score = random.randint(50, 100)

    print(f"{name1}{name2}")
    print(f"Love Percentage: {love_score}%")

person1 = input("Enter the first name: ")
person2 = input("Enter the second name: ")

love_calculator(person1.strip(), person2.strip())
