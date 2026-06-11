import functools
import sys
import time


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

def time_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Wykonano funkcję: {func.__name__} w {end_time - start_time:.6f}")
        return result, (end_time - start_time)
    return wrapper

@time_deco
def greedy(items, max_capacity):
    items.sort(key=lambda itemlam: itemlam[2]/itemlam[1], reverse=True)
    current_capacity = 0
    current_value = 0
    final_items = []
    for item in items:
        if current_capacity + item[1] <= max_capacity:
            current_capacity += item[1]
            current_value += item[2]
            final_items.append([item[0], item[1], item[2]])
            #print(f"Włożono {item[0]}, Aktualna waga: {current_capacity}, Aktualna wartość: {current_value}")
    print(f"Wynik zachłanny: Przedmioty: {final_items}, Łączna wartość: {current_value}")
    return current_value

@time_deco
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
    print(f"Wynik siłowy: Przedmioty:  {max_val_items}, Łączna wartość: {max_value}")
    return max_value

if __name__ == "__main__":
    my_filename = input("Podaj nazwe pliku: ")
    items = load_file(my_filename)
    my_capacity = int(input("Podaj max pojemnosc plecaka: "))
    print("\nWypisywane wyniki- Nazwa, Waga, Wartość\n")
    greedy_result, greedy_time = greedy(items, my_capacity)
    print("\n")
    brute_result, brute_time = brute_force(items, my_capacity)

    print("\n PODSUMOWANIE\nLepszy wynik:", end="")
    if greedy_result > brute_result:
        print("Algorytm zachłanny!")
    elif greedy_result < brute_result:
        print("Algorytm siłowy!")
    else:
        print("Remis!")

    print("Lepszy czas: ", end="")
    if greedy_time < brute_time:
        print("Algorytm zachłanny!")
    elif greedy_time > brute_time:
        print("Algorytm siłowy!")
    else:
        print("Remis!")

