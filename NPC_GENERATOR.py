import random
import time

while True:    #<--- makes the loop run endlessly
    user_input = int(input("Enter the amount of NPC's you would like to generate: "))  #Takes the amount of NPC's to print
    if user_input > 20:
        print("\n-:-ERROR-:- A maximum of 20 NPC's can be printed at once, please enter another value\n") #<---- error if 21 or above NPC's are requested
    elif user_input < 1:
        print("\n-:-ERROR-:- Only positive numbers can be printed, please enter another value\n: ")   #<---- error if 0 or any negitive numbers are requested
    else:
        break    #<---- stops the loop
  
Name = ["Alex", "Taylor", "Riley", "Jordan", "Jamie", "Charlie", "Oliver", "sam", "kai", "Rowan", "Morgan", "corrie", "Jasper", "Luca", "Quin", "Jade", "Rune", "Java"] #<--- gender neutral names
gender = ["Male", "Female"]                  
for i in range(user_input): #<--- loops the NPC generator how ever many times user unput is
    random_name = (random.choice(Name))          #Takes a random string from the list in line 13 and prints as NPC's name
    random_gender = (random.choice(gender))
    Attack_power = (random.randint(1, 10))                  #each of these characteristics print strength 1/10 - 10/10
    Health_efficency = (random.randint(1, 10))              #^
    Agility = (random.randint(1, 10))                       #^
    sheilding = (random.randint(1, 10))                     #^
    NPC_stats = (f"-------------\nCharacter stats:\nName: {random_name} \nGender: {random_gender} \nHealth efficency:  {Health_efficency}/10  \nAttack power:  {Attack_power}/10 \nsheilding:  {sheilding}/10  \nAgility:  {Agility}/10")  #This is the format of the final print
    time.sleep(0.000888) #<---- Float
    print(NPC_stats)
    if Attack_power + Health_efficency + Agility + sheilding >= 40:          #adds Attack_power + Health_efficency + Agility + sheilding and determans it's strength   
        print(f"{random_name}" " is a GOLDEN CHARACTER and has top tier skill!")    #10/10
    elif 28 <= Attack_power + Health_efficency + Agility + sheilding <= 36:   
        print(f"{random_name}" " is strong and has above average skill!") #7/10 - 9/10
    elif 16 <= Attack_power + Health_efficency + Agility + sheilding <= 24:
        print(f"{random_name}" " is standard and has average skill!")         #4/10 - 6/10
    else:
        print(f"{random_name}" " is weak and has below average skill!")       #1/10 - 3/10