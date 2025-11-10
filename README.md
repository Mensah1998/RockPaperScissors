# Rock Paper Scissors

A simple and fun **Rock–Paper–Scissors** game built in **Python**. Play against the computer in your terminal!

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## ✨ Features

✅ Play Rock, Paper, Scissors against the computer
✅ Randomized computer choice
✅ Emoji visualisation
✅ Input validation
✅ Continuous play option

---

## 📂 Project Structure

```
main.py        # Game logic and entry point
```

---

## ▶️ Getting Started

### **Prerequisites**

* Python 3.x

### **Run the Game**

```bash
python main.py
```

---

## 🕹️ How to Play

1. Run the program
2. Choose:

   * `r` → Rock
   * `p` → Paper
   * `s` → Scissors
3. The computer makes a random selection
4. Results are displayed
5. Continue or quit

---

## 📘 Game Rules

| Choice   | Beats    |
| -------- | -------- |
| Rock     | Scissors |
| Scissors | Paper    |
| Paper    | Rock     |

A tie occurs if both choose the same option.

---

## 📦 Code Breakdown

* `get_user_choice()` → Handles user input
* `display_choices()` → Shows selection with emojis
* `determine_winner()` → Calculates game result
* `play_game()` → Gameplay loop

---

## 🔧 Technologies Used

* Python Standard Library (`random`)

---

## 📷 Demo

```
Rock, paper, or scissors? (r/p/s): r
You chose 🪨
Computer chose ✂️
You Win!
Continue? (y/n): n
```

---

## 👤 Author

**Mensah Koranteng-Apeagyei**

---

Enjoy playing! 🎉
