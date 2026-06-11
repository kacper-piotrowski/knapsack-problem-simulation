import sys

def load_file(filename):
    try:
        items = []
        with open(filename) as f:
            for line in f:
                current_line = line.strip()
                if len(current_line) == 0:
                    continue
                current_line = current_line.split(";")
                item_name = current_line[0]
                item_weight = float(current_line[1])
                item_value = float(current_line[2])
                items.append([item_name, item_weight, item_value])
            return items
    except FileNotFoundError:
        sys.exit("Nie znaleziono pliku")

def greedy(items, max_capacity):
    items.sort(key=lambda itemlam: itemlam[2]/itemlam[1], reverse=True)
    current_capacity = 0
    current_value = 0
    for item in items:
        if current_capacity + item[1] <= max_capacity:
            current_capacity += item[1]
            current_value += item[2]
            print(f"Włożono {item[0]}, Aktualna waga: {current_capacity}, Aktualna wartość: {current_value}")

def brute_force(items, max_capacity):
    combos=[[]]
    for item in items:
        new_combos = []
        for combo in combos:
            new_combo = combo + [item]
            new_combos.append(new_combo)
        combos.extend(new_combos)

    max_value = 0
    max_val_items = []
    for combo in combos:
        combo_weight = 0
        combo_value = 0

        for item in combo:
            combo_weight += item[1]
            combo_value += item[2]

        if combo_weight <= max_capacity and combo_value > max_value:
            max_value = combo_value
            max_val_items = combo
    print(f"Najlepsze kombo: {max_val_items}, Wartość: {max_value}")
