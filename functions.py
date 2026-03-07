import Convert

# This function when given the input of 2 years will return the summary of data between the 2 time periods

def summarize(year1: int, year2: int):
    # ensure year1 <= year2
    if year1 > year2:
        return "year 1 must be less than year 2"

    # collect Fish in the time period
    period = [f for f in Convert.fish_list if f.year]

    if not period:
        return "no data found between given years"

    # highest / lowest within the period
    high_fish = max(period)
    low_fish  = min(period)

    # total change from year1 to year2:
    # if there are duplicates for a year, take the last one in the list
    year1 = [f for f in Convert.fish_list if f.year == year1]
    year2   = [f for f in Convert.fish_list if f.year == year2]

    if not year1:
        return "no data found at year1"
    if not year2:
        return "no data found at year2"

    start_pop = year1[0].pop
    end_pop   = year2[0].pop
    total_change = end_pop - start_pop

    # return (
    #     "The biggest fish population was {} in {}\n"
    #     "The smallest fish population was {} in {}\n"
    #     "The total change of Fish during those 2 time periods is {}"
    # ).format(
    #     high_fish.pop, high_fish.year,
    #     low_fish.pop, low_fish.year,
    #     total_change
    # )

    return {
        "highest": {"year": high_fish.year, "population": high_fish.pop},
        "lowest": {"year": low_fish.year, "population": low_fish.pop},
        "total_change": total_change
    }

print(summarize(1937,1942)['highest']['population'])