# 📓 Project Log — Terminal Souls

> *Students:* Luis Gonzales & Carlos Muñoz
> *Course:* Fundamentals of Programming
> *Start date:* 19/03/2026
> *Language:* Python

-----

## 📌 Project Description

Terminal Souls is a turn-based combat simulator that runs in the terminal. The player controls a Hero who must defeat an Enemy by choosing actions each turn: attack, heal, or use a special ability.

-----

## 🎯 Project Goals

- [x] Implement the function generate_damage(minimum, maximum)
- [x] Implement the function show_status()
- [x] Implement the function player_turn()
- [x] Implement the function enemy_turn()
- [x] Implement the function check_winner()
- [x] Main loop with while
- [x] Potion validation
- [x] Console messages for each action

### Extra challenges

- [ ] Critical hit system (10% chance, double damage)
- [x] Basic enemy AI (heals itself if HP drops below 20%)

-----

## 🗂️ File Structure


terminal_souls.py
│
├── generate_damage()     → Generates random damage
├── health_bar()          → Shows a visual health bar
├── show_status()         → Shows HP of both characters
├── player_turn()         → Handles the player's actions
├── enemy_turn()          → Automatic enemy logic
├── check_winner()        → Checks if someone reached 0 HP
└── Main loop             → While cycle that runs the game


-----

## 📋 Game Attributes

| Character | Starting HP | Special                  |
|-----------|-------------|--------------------------|
| Hero      | 100         | 3 healing potions         |
| Enemy     | 120         | Attacks automatically + 1 emergency potion |

### Player actions

| Action           | Effect                                          |
|------------------|-------------------------------------------------|
| Attack           | Random damage between 10 and 25                 |
| Heal             | Recovers 20 HP (requires a potion)              |
| Special Ability  | Damage 30-50, but 50% chance of missing         |

-----

## 📅 Progress Log

### Entry 1 — 19/03/2026

*What was done?*

> Luis Gonzales and Carlos Muñoz defined the conditions for both players and the general logic of the game. They read the project requirements to understand what each function needed to do. They split the functions between the two developers. All the planning and analysis was written on paper before starting to code.

*How was it done?*

> Luis and Carlos read the instructions PDF together. They went through each requirement, talked about how the turns would work, and decided which function each person would build. The first design was done by hand, as a draft on paper.

*What did they learn?*

> The importance of planning before coding. Dividing the work from the start prevents two people from writing duplicate or incompatible code.

-----

### Entry 2 — 19/03/2026

*What was done?*

> **Carlos Muñoz:** Started the Python file. He wrote the `import random`, declared the global variables (`hero_hp`, `enemy_hp`, `potions`, `enemy_potions`), built the `generate_damage()` function, and set up the main `while` loop. He shared his progress with Luis at the end of the day.
>
> **Luis Gonzales:** Received Carlos's work and built the `health_bar()` function to show a visual health bar using `█` and `-` characters, and the `show_status()` function that prints the combat status on screen.

*How was it done?*

> Carlos used `random.randint()` inside `generate_damage()` to generate random damage. The global variables were defined at the top of the file so all functions could use them.
>
> Luis calculated the health bar proportionally to the max HP using integer division and multiplication. The `show_status()` function uses the global variables to print the updated status each turn.

*What did they learn?*

> How to use global variables inside functions. How to use special characters in the terminal to display data visually. The importance of sharing progress between teammates to integrate the code.

-----

### Entry 3 — 20/03/2026

*What was done?*

> **Carlos Muñoz:** Reviewed the changes Luis had added to the main code (`health_bar` and `show_status`) to make sure they matched the flow of the program. Then he built the `player_turn()` function with the three action options for the player.
>
> **Luis Gonzales:** Built the `enemy_turn()` function with the basic enemy AI (heals itself if HP drops below 20%) and the `check_winner()` function that returns `True` when one of the fighters reaches 0 HP.

*How was it done?*

> Carlos used `input()` to read the player's choice and `if/elif/else` conditions to run each action. He added potion validation: if the player tries to heal with no potions left, the program gives a message without wasting the turn. He used recursion (calling `player_turn()` again) to handle invalid inputs.
>
> Luis checked in `enemy_turn()` if `enemy_hp <= 24` (20% of 120) to decide if the enemy heals or attacks. The `check_winner()` function uses a simple `or` condition to detect if either HP reached 0 or below.

*What did they learn?*

> How to build basic AI logic using conditions. How to use the `global` keyword to modify variables from inside a function. How to structure a turn-based game with separate functions.

-----

### Entry 4 — 20/03/2026

*What was done?*

> Once the first full draft of the code was ready, **Luis Gonzales** ran the program and found two bugs: the variable `enemy_potions` was not declared globally, and the enemy's health bar looked the same as the hero's even though the enemy has more HP.
>
> **Carlos Muñoz** fixed the global declaration of `enemy_potions`. **Luis Gonzales** updated `show_status()` so the enemy's bar is calculated using 120 HP instead of 100.

*How was it done?*

> Carlos added `enemy_potions = 1` as a global variable at the top of the file. Luis adjusted the `health_bar()` call inside `show_status()` to pass `max_hp=120` for the enemy and `max_hp=100` for the hero, making each bar proportional to the real HP of each character.

*What did they learn?*

> The importance of testing the code after putting it together. That variables used in multiple functions need to be declared globally to avoid reference errors. That the same helper function (`health_bar`) can be reused with different parameters for each character.

-----

## 🐛 Bug Log

### Bug 1

- *Date:* 20/03/2026
- *Description:* `UnboundLocalError` — the variable `enemy_potions` was not found inside `enemy_turn()`.
- *Cause:* The variable `enemy_potions` was used inside `enemy_turn()` without being declared as global or defined at the top of the file.
- *Solution:* Added `enemy_potions = 1` as a global variable at the top of the file, next to the other attribute variables.

-----

### Bug 2

- *Date:* 20/03/2026
- *Description:* The enemy's health bar was showing incorrectly — it appeared almost full even when the enemy had very little HP.
- *Cause:* The `health_bar()` function was calculating the bar using `max_hp=100` for both characters, but the enemy has 120 HP, so the proportion was wrong.
- *Solution:* Updated the `health_bar()` call in `show_status()` to pass `max_hp=120` for the enemy and `max_hp=100` for the hero.

-----

## ✏️ Changes Log

### Change 1

- *Date:* 20/03/2026
- *What was changed?* Added the global variable `enemy_potions` at the top of the file.
- *Why was it changed?* It was a bug: the variable was not defined and caused the program to crash when the enemy tried to heal.
- *Before:*

```python
hp_heroe = 100
hp_enemigo = 120
pociones = 3
```

- *After:*

```python
hero_hp = 100
enemy_hp = 120
potions = 3
enemy_potions = 1   # Variable added
```

-----

### Change 2

- *Date:* 20/03/2026
- *What was changed?* Fixed the enemy's health bar in `show_status()` to use `max_hp=120`.
- *Why was it changed?* The bar was not showing the enemy's health correctly because it was calculated using 100 instead of 120.
- *Before:*

```python
print(f"ENEMY  {enemy_hp}/120")
print(f"[{health_bar(enemy_hp, 100)}]")   # Wrong
```

- *After:*

```python
print(f"ENEMY   {enemy_hp}/120")
print(f"[{health_bar(enemy_hp, 120)}]")   # Fixed
```

-----

## 💡 Concepts Learned

| Concept             | What is it for?                                               |
|---------------------|---------------------------------------------------------------|
| `def`               | Define a reusable function                                    |
| `random.randint()`  | Generate a random integer within a range                      |
| `while`             | Repeat a block of code while a condition is true              |
| `global`            | Let a function modify a variable that is defined outside of it |
| `input()`           | Read data that the user types in the terminal                 |
| `if / elif / else`  | Make decisions based on the value of a variable               |
| `return`            | Make a function send a value back to the code that called it  |
| Parameters          | Pass values to a function so it can use them in its logic     |
| Simple recursion    | Call a function from inside itself to repeat an action        |

-----

## 🔍 Questions and Doubts

> Questions that came up during the development of the project.

1. Why do we need to use `global` inside a function if the variable already exists outside of it?
2. When is it better to use recursion instead of a `while` loop to repeat an action?
3. How could we add the critical hit system (10% chance of double damage) to the existing code?

-----

## ✅ Final Status

- *Delivery date:* 20/03/2026
- *Does it work correctly?* Yes
- *Final notes:*

> The project was finished successfully in two days of work. The hardest part was putting together the code from both developers, especially dealing with global variables shared between functions. The biggest lesson was learning how to break a big problem into small, separate functions, and how important it is to test the code after each integration. If we did it again, we would add the critical hit system and improve the input validation for the player.

-----

Project log for Terminal Souls — Programming Challenge
