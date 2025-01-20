from tabulate import tabulate

def get_input(prompt):
    return float(input(prompt).replace(" ", ""))

def get_frequency():
    match input("input the frequency (e.g. w, m, y): ").lower():
        case "w":
            return "week", 52
        case "m":
            return "month", 12
        case "y":
            return "year", 1
        case _:
            print("invalid input")
            quit()

def calculate_compound_interest(money, moneyperyear, percentage, timesperyear):
    rows = []
    year = 1
    for _ in range(20):
        totalamount = money * (pow((1 + percentage / timesperyear), year*timesperyear)) + moneyperyear*((((1+(percentage/timesperyear))**((timesperyear*year)))-1)/(percentage/timesperyear))
        rows.append([year, f"{"{:,}".format(round(totalamount, 3))} $"])
        year += 1
    return rows

def main():
    money = get_input("starting amount: ")
    freq, timesperyear = get_frequency()
    moneyperyear = get_input(f"input the money you put per {freq}: ")
    percentage = get_input("input the percentage you get per year (e.g. 30): ") / 100

    rows = calculate_compound_interest(money, moneyperyear, percentage, timesperyear)
    headers = ["year", "Amount"]
    print(tabulate(rows, headers, tablefmt="fancy_grid"))

    while True:
        this = input("press q to quit, r to rerun: ").lower()
        if this == 'q':
            break
        elif this == 'r':
            main()

main()