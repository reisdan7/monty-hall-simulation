import random

doors = [1, 2, 3]

counter_stay = 0
counter_switch = 0

simulations = int(input("How many simulations do you want to run? (1-1000): "))

while simulations < 1 or simulations > 1000:
    simulations = int(input("Please enter a number between 1 and 1000: "))

for i in range(simulations):
    prize_door = random.choice(doors)
    player_choice = random.choice(doors)

    # Host opens a door that has no prize and wasn't chosen
    host_doors = []

    for door in doors:
        if door != prize_door and door != player_choice:
            host_doors.append(door)

    host_door = random.choice(host_doors)

    # Stay strategy
    if player_choice == prize_door:
        counter_stay += 1

    # Switch strategy
    remaining_doors = []

    for door in doors:
        if door != player_choice and door != host_door:
            remaining_doors.append(door)

    if remaining_doors[0] == prize_door:
        counter_switch += 1

print("\nResults:")
print("Stay wins:", counter_stay)
print("Switch wins:", counter_switch)

if counter_stay > counter_switch:
    print("Staying won more often!")
elif counter_switch > counter_stay:
    print("Switching won more often!")
else:
    print("Both strategies won the same number of times:", counter_stay)
