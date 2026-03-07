import csv
from Class import Fish

fish_list = []

with open("Data_total_pop", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        fish = Fish(
            year = int(row["year"]),  # convert to int (better than str here)
            population = int(row["total_salmon_population"])
        )
        fish_list.append(fish)