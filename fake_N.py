import random

subjects =[
    "Sourav Mondal",
    "Shahrukh Khan",
    "Khan sir",
    "A group of Monkeys",
    "Prime Minister Modi",
    "Auto Driver from  kolkata",
    "Ranu Mondal",
]

actions =[
    "launches",
    "is looking Trump",
    "Dances",
    "eats",
    "decleared war on",
    "orders",
    "clebrates",
]

places_or_things =[
    "at Red Fort",
    "In Mumbai Local Train",
    "a late of Samosa",
    "inside parlament",
    "at Ganga Ghat",
    "During ipl match",
    "at India Gate",
]


while True:
    Subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)


    headline = f"BREAKING NEWS: {Subject} {action} {places_or_thing}"

    print("\n"+ headline)


    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
print("\nThanks for generating and using the Fake News Headline Generator. Have a fun Day!")