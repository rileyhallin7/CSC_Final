import csv
from Class import Fish

fish_list = []

with open("Data_total_pop", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        fish = Fish(
            year = int(row["year"]),
            population = int(row["total_salmon_population"])
        )
        fish_list.append(fish)

fish_list = fish_list