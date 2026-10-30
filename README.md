# Monty Hall Simulation

A small Python script that simulates the Monty Hall problem to check whether the theory is true.

**This project was made to practice Python.** I wanted to test the idea with code instead of just reading about it.

## The problem

You are in a game show with 3 doors. Behind one of them there is a prize. You pick a door, then the host, who knows where the prize is, opens another door that has nothing behind it. Now you can stay with your first choice or switch to the last closed door.

Is it better to stay or to switch?

## How it works

For each simulation the script:

1. Puts the prize behind a random door
2. Makes a random first choice for the player
3. Lets the host open a door that has no prize and wasn't chosen
4. Counts a win for the **stay** strategy if the first choice had the prize
5. Counts a win for the **switch** strategy if the remaining closed door has the prize

At the end it prints how many times each strategy won.

## How to run

You need Python 3 installed.

```bash
git clone https://github.com/reisdan7/monty-hall-simulation.git
cd monty-hall-simulation
python monty_hall.py
```

Then type how many simulations you want to run (from 1 to 1000).

## Example output

```
How many simulations do you want to run? (1-1000): 1000

Results:
Stay wins: 331
Switch wins: 669
Switching won more often!
```

Your numbers will be a bit different every time, but switching wins around 2/3 of the time and staying around 1/3.

## What I practiced

- Loops and conditions
- Lists
- The `random` module
- Reading and validating user input

Made by Daniel Reis
