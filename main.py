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
        sys.exit("File not found")
