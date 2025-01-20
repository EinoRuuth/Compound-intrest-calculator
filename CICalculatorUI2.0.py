import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Compound intrest calculator")
root.geometry("500x550")

root.configure(bg="grey")

main_frame = tk.Frame(root, bg="grey")
main_frame.pack(fill="both", expand=True)

input_frame = tk.Frame(main_frame, bg="grey")
input_frame.pack(side="left", fill="y", padx=10, pady=10)

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="grey", background="grey", foreground="white")

label_dropdown = tk.Label(input_frame, text="Currency:", bg="grey", fg="white")
label_dropdown.pack(anchor="w", padx=2)
dropdown_values = ["Dollar", "Pounds", "DKK"]
dropdown_mapping = {"Dollar": "$", "Pounds": "£",  "DKK": "KR"}
def getCurrency():
    return dropdown_mapping[dropdown.get()]
dropdown = ttk.Combobox(input_frame, values=dropdown_values, style="TCombobox")
dropdown.pack(fill="x", padx=2)
dropdown.current(0)

label1 = tk.Label(input_frame, text="Starting amount:", bg="grey", fg="white")
label1.pack(anchor="w", padx=2)
entry1 = tk.Entry(input_frame, bg="grey", fg="white")
entry1.pack(fill="x", padx=2)

label_dropdown_freq = tk.Label(input_frame, text="Frequency:", bg="grey", fg="white")
label_dropdown_freq.pack(anchor="w", padx=2)
freq_dropdown_values = ["Weekly", "Monthly", "Yearly"]
freq_dropdown_mapping = {"Weekly": 52, "Monthly": 12, "Yearly": 1}
def getFrequency():
    return freq_dropdown_mapping[freq_dropdown.get()]
freq_dropdown = ttk.Combobox(input_frame, values=freq_dropdown_values, style="TCombobox")
freq_dropdown.pack(fill="x", padx=2)
freq_dropdown.current(0)

label2 = tk.Label(input_frame, text="Money per deposit:", bg="grey", fg="white")
label2.pack(anchor="w", padx=2)
entry2 = tk.Entry(input_frame, bg="grey", fg="white")
entry2.pack(fill="x", padx=2)

label32 = tk.Label(input_frame, text="Percentage:", bg="grey", fg="white")
label32.pack(anchor="w", padx=2)
entry3 = tk.Entry(input_frame, bg="grey", fg="white")
entry3.pack(fill="x", padx=2)
entry3.insert(0, "12.481")

def calculate_compound_interest(money, moneyperyear, percentage, timesperyear):
    currency = getCurrency()
    print(money)
    rows = []
    year = 1
    for _ in range(20):
        firstCalc = moneyperyear*((((1+(percentage/timesperyear))**((timesperyear*year)))-1)/(percentage/timesperyear))
        secondCalc = money * (pow((1 + percentage / timesperyear), year*timesperyear))
        moneyinputted = timesperyear * moneyperyear * year
        totalamount = secondCalc + firstCalc
        rows.append([year, f"{"{:,}".format(round(totalamount, 3))} {currency}", f"{"{:,}".format(round(moneyinputted, 3))} {currency}"])
        year += 1
    return rows

def calculatorMain(money, timesperyear, moneyperyear, percentage):
    rows = calculate_compound_interest(money, moneyperyear, percentage/100, timesperyear)
    return rows

def on_start_button_click():
    print("Start button clicked!")
    for item in table.get_children():
        table.delete(item)
    values = calculatorMain(float(entry1.get()), getFrequency(), float(entry2.get()), float(entry3.get()))
    for x in range(len(values)):
        if x % 2 == 0:
            table.insert("", "end", values=values[x], tags=('evenrow',))
        else:
            table.insert("", "end", values=values[x], tags=('oddrow',))

start_button = tk.Button(input_frame, text="Start", command=on_start_button_click, bg="grey", fg="white")
start_button.pack(anchor="w", padx=2, pady=10)

table_frame = tk.Frame(main_frame, bg="grey")
table_frame.pack(side="top", anchor="center")

style = ttk.Style()

style.theme_use("clam")
style.configure("Treeview", rowheight=25, background="grey", foreground="white", fieldbackground="grey", borderwidth=1, relief="ridge")
style.map("Treeview", background=[("selected", "black")], foreground=[("selected", "white")])
style.configure("Treeview.Heading", background="grey", foreground="white")
style.map("Treeview.Heading", background=[("selected", "grey")], foreground=[("selected", "white")])

table = ttk.Treeview(table_frame, columns=("Year", "Money", "Added"), show="headings", height=20)
table.heading("Year", text="Year")
table.heading("Money", text="Money")
table.heading("Added", text="Added")

table.column("Year", width=100, anchor="center")
table.column("Money", width=100, anchor="center")
table.column("Added", width=100, anchor="center")

table.tag_configure('evenrow', background='grey', foreground='white')
table.tag_configure('oddrow', background='darkgrey', foreground='white')

table.pack(fill="both", expand=True)

for i in range(20):
    if i % 2 == 0:
        table.insert("", "end", values=("", "", ""), tags=('evenrow',))
    else:
        table.insert("", "end", values=("", "", ""), tags=('oddrow',))


root.mainloop()
