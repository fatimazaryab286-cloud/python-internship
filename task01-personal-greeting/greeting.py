name=input("What's your name?") #asking user for name
age=int(input("What's your age?")) #asking user for age
fav_number=int(input("What's your favourite number?")) #asking user for favourite number

birth_year=2026-age          #calculating the birth year
newfavourite_num=fav_number*2 #doubling the favourite number

print(f"oh, {name} just entered the chat")
print(f"you picked {fav_number}? interesting choice")
print(f"born in {birth_year} and already {age}? time really said speedrun.")
print(f"your favourite number is, {fav_number}, but doubled it's {newfavourite_num}.")
