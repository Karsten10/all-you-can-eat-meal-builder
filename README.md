# Cubanita AYCE | Meal Designer Deluxe

## Overview
This project is a stylish GUI application for building an extravagant all-you-can-eat meal based on the Cubanita AYCE menu. It allows users to:

- Browse the entire menu.
- Select multiple dishes.
- View a live update of the total cost.
- Visualize their selections using a pie chart (cost distribution) and bar chart (cost per dish).

Built with `tkinter` for the GUI and `matplotlib` for the graphs, this project is designed for intuitive use and visual appeal.

---

## Features
- 💡 Intuitive, modern GUI with themed widgets.
- 🛒 Dynamic meal builder cart.
- 📊 Dual-graph display: pie chart and bar chart.
- 📁 Fallback file dialog in case the menu file isn't found.

---

## Setup

### 1. Clone or download this repository
```bash
cd ~/Desktop
mkdir all-you-can-eat-prep && cd all-you-can-eat-prep
```

### 2. Add your CSV menu file
Make sure the file `Cubanita AYCE - prices_cubanita.csv` is in the same folder. If it’s not, the app will ask you to locate it.

### 3. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install pandas matplotlib
```

---

## Run the Application
```bash
python main.py
```

---

## File Format
The CSV file must have the following columns:
```
id,name,expected price
```
Where `expected price` uses commas for decimals (e.g., `3,5` for €3.50).

---

## Example
A selection might show:
- `Brood met alioli en tapenade`
- `Carpaccio met pestodressing`
- `Crostini met tomatensalsa`

Resulting in:
- A total cost of €11.00
- A pie chart showing the percentage cost per dish
- A bar chart comparing the individual dish prices

---

## Improvements & Ideas
- Dark mode toggle 🌙
- Export meal to PDF 🧾
- Nutritional insights (protein, carbs, fats) 🥩
- Random meal generator 🎲
- User login to save favorite combos 💾

---

## License
MIT License. Free to use and modify.

---

## Author
Built with appetite by Karsten Stolk.

---

Enjoy your feast! 🍽️

