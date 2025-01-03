import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favourite = row["language"]
        counts[favourite] =  counts.get(favourite, 0) + 1

for favourite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favourite}: {counts[favourite]}")
