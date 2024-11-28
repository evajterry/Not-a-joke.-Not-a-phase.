# Kerrigan Feet Pic Simulator

## Introduction

Welcome to the **Kerrigan Feet Pic Simulator**! This playful Python program simulates a quirky interaction between a character named *Kerrigan* and *Eva*. The goal? To see if Kerrigan will send "foot pics" based on user interactions involving proximity, pickup lines, and the surprising addition of extra feet. 

**Disclaimer**: This project is purely for fun and educational purposes. It does not endorse inappropriate behavior and should be taken lightheartedly as a humorous demonstration of Python programming.

---

## How It Works

### Key Components

- **Kerrigan Class**:
  - `name`: Initialized as `"Kerrigan"`.
  - `number_of_feet`: Starts with 2 feet.
  - `proximity_to_eva`: Begins at a distance of 10 units from Eva.
  - `foot_pick_up_lines`: Stores user-submitted foot-themed pickup lines.

- **`distance_calculator(user_response)`**:
  Adjusts the proximity between Kerrigan and Eva:
  - `"2"` decreases the distance (Eva moves closer).
  - `"3"` increases the distance (Eva moves farther away).

- **`growing_feet(user_response)`**:
  Adds an additional foot to Kerrigan each time it is called.

- **`does_kerrigan_send_feet_pics(kerrigan)`**:
  Determines if Kerrigan sends foot pics based on the following:
  - Checks for pickup lines containing "toe" or "toes."
  - Evaluates Kerrigan's proximity to Eva.
  - Considers the total number of feet Kerrigan has.

### User Interaction Options

1. **Pickup Lines**: Submit a foot-themed pickup line to influence Kerrigan.
2. **Proximity Control**: Move Kerrigan and Eva closer or farther apart.
3. **Feet Growth**: Increase Kerrigan’s number of feet.
4. **Check Status**: Check progress toward receiving a foot pic.

---

## Running the Program

To run the program, execute the script in your terminal or IDE:

```bash
python kerrigan_simulator.py
