# This function will function as a program that the user can utilize to extract data from the data set
# like a research function or a search function to access data
import Convert
from Class import Fish
from functions import summarize

# returns input as int
def prompt_int(message: str) -> int:
    while True:
        s = input(message).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer.")

#main menu
def menu() -> None:
    print("\nActions:")
    print("  1 = summarize  - summarizes details within the given data range")
    print("  2 = quit  ")

#menu logic
def main() -> None:
    while True:
        menu()
        print("Enter the number corresponding with desired action")
        choice = prompt_int("\nEnter a number")

        if choice == 2:
            print("Goodbye!")
            break

        elif choice == 1:
            print('The data ranges from 1930 to 2024')
            y1 = prompt_int("Enter year 1: ")
            while y1 <= 1930:
                print('The data ranges from 1930 to 2024')
                y1 = prompt_int("Enter a year within the data range")
            y2 = prompt_int("Enter year 2: ")
            while y2 <= 2024 and y2 < y1:
                print('The data ranges from 1930 to 2024')
                y2 = prompt_int("Enter a year within the data range")

            try:
                result = summarize(y1, y2)

                print(
                    "\nThe biggest fish population was {} in {}\n"
                    "The smallest fish population was {} in {}\n"
                    "The total change of Fish during those 2 time periods is {}\n"
                    .format(
                        result["highest_population"], result["highest_year"],
                        result["lowest_population"], result["lowest_year"],
                        result["total_change"],
                        result["percent_change"]
                    )
                )
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()