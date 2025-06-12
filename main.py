import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import os

# Load and clean the menu data
MENU_FILE = "menu-prices.csv"
if not os.path.exists(MENU_FILE):
    MENU_FILE = filedialog.askopenfilename(title="Select Menu CSV File")
menu_df = pd.read_csv(MENU_FILE)
menu_df['expected price'] = menu_df['expected price'].str.replace(',', '.').astype(float)

class MealBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cubanita AYCE | Meal Designer Deluxe")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f5f5")

        self.selected_items = []

        self.setup_styles()
        self.create_widgets()
        self.update_total_price()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, relief="flat", background="#007acc", foreground="white", font=('Helvetica', 10, 'bold'))
        style.configure("TLabel", background="#f5f5f5", font=('Helvetica', 12))
        style.configure("TListbox", font=('Helvetica', 10))

    def create_widgets(self):
        # Title
        ttk.Label(self.root, text="All You Can Eat Menu", font=("Helvetica", 16, "bold"), background="#f5f5f5").pack(pady=10)

        # Main frame
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left - Menu List
        left_frame = tk.Frame(main_frame, bg="#f5f5f5")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(left_frame, text="Menu Items:").pack(anchor='w')
        self.menu_listbox = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, width=40, height=20, font=('Helvetica', 10))
        for item in menu_df['name']:
            self.menu_listbox.insert(tk.END, item)
        self.menu_listbox.pack(pady=5)

        self.add_button = ttk.Button(left_frame, text="➕ Add to Meal", command=self.add_to_meal)
        self.add_button.pack(fill=tk.X, pady=(5, 2))

        self.clear_button = ttk.Button(left_frame, text="🗑️ Clear Meal", command=self.clear_meal)
        self.clear_button.pack(fill=tk.X, pady=(2, 10))

        # Center - Meal Cart
        center_frame = tk.Frame(main_frame, bg="#f5f5f5")
        center_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(center_frame, text="Your Meal:").pack(anchor='w')
        self.selected_listbox = tk.Listbox(center_frame, width=40, height=12, font=('Helvetica', 10))
        self.selected_listbox.pack(pady=5)

        self.total_label = ttk.Label(center_frame, text="Total: €0.00", font=("Helvetica", 14, "bold"))
        self.total_label.pack(pady=5)

        # Right - Graphs
        self.figure, self.axs = plt.subplots(1, 2, figsize=(6, 4))
        self.figure.subplots_adjust(wspace=0.5)
        self.canvas = FigureCanvasTkAgg(self.figure, master=main_frame)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def add_to_meal(self):
        selections = self.menu_listbox.curselection()
        for index in selections:
            name = menu_df.iloc[index]['name']
            if name not in self.selected_items:
                self.selected_items.append(name)
                self.selected_listbox.insert(tk.END, name)
        self.update_total_price()
        self.draw_graphs()

    def clear_meal(self):
        self.selected_items.clear()
        self.selected_listbox.delete(0, tk.END)
        self.update_total_price()
        self.draw_graphs()

    def update_total_price(self):
        total = sum(menu_df[menu_df['name'].isin(self.selected_items)]['expected price'])
        self.total_label.config(text=f"Total: €{total:.2f}")

    def draw_graphs(self):
        self.axs[0].clear()
        self.axs[1].clear()

        if not self.selected_items:
            self.canvas.draw()
            return

        prices = menu_df[menu_df['name'].isin(self.selected_items)]
        names = prices['name']
        values = prices['expected price']

        # Pie Chart
        self.axs[0].pie(values, labels=names, autopct='%1.1f%%', textprops={'fontsize': 8})
        self.axs[0].set_title("Cost Distribution", fontsize=10)

        # Bar Chart
        self.axs[1].barh(names, values, color="#007acc")
        self.axs[1].set_title("Cost per Dish", fontsize=10)
        self.axs[1].set_xlabel("Price (€)", fontsize=9)
        self.axs[1].tick_params(axis='y', labelsize=8)
        self.axs[1].tick_params(axis='x', labelsize=8)

        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = MealBuilderApp(root)
    root.mainloop()
