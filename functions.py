import Convert

# This function when given the input of 2 years will return the summary of data between the 2 time periods

def summarize(year1: int, year2: int):
    # ensure year1 <= year2
    if year1 > year2:
        return "year 1 must be less than year 2"

    # collect Fish in the time period
    period = [f for f in Convert.fish_list if year1 <= f.year <= year2]

    if not period:
        return "no data found between given years"

    # highest / lowest within the period
    high_fish = max(period)
    low_fish  = min(period)

    # total change from year1 to year2:
    start = [f for f in Convert.fish_list if f.year == year1]
    end   = [f for f in Convert.fish_list if f.year == year2]

    if not start:
        return "no data found at year1"
    if not end:
        return "no data found at year2"

    start_pop = start[0].pop
    end_pop   = end[0].pop
    total_change = end_pop - start_pop
    percent_change=(end_pop - start_pop)/start_pop*100

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
        "highest": {"year": f"Largest Population Year: {high_fish.year}", "population": f"Largest Population: {high_fish.pop}"},
        "lowest": {"year": f"Smallest Population Year: {low_fish.year}", "population": f"Smallest Population: {low_fish.pop}"},
        "total_change": f"Total Change: {total_change}",
        "percent_change": f"Percent Change: {percent_change}"
    }

if __name__ == "__main__":
    print(summarize(1960,1962))
    print(summarize(1937,1942))
    print(summarize(1937,1942)['percent_change'])