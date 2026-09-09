series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def mean(in_series):
    return(sum(in_series) / len(in_series))

def variance(in_series):
    meanValue = mean(in_series)
    squaredValues = []
    for dataPoint in in_series:
        squaredValues.append((dataPoint - meanValue) ** 2)
    return sum(squaredValues) / len(in_series) - 1

def standard_deviation(in_series):
    return variance(in_series) ** 0.5

def range_calculation(in_series):
    sortedList = in_series.sorted()
    return (sortedList[-1] - sortedList[0])


def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    pass

def read_csv(file,default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(len(lines[0])):
        data_table[lines[0][i]] = [default_value if (len(line[i]) == 0) else float(line[i]) for line in lines[1:]]
    return data_table

def get_user_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Enter the number of your choice: ")
    if choice.lower() == 'exit':
        return None
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        print("Invalid choice. Please try again.")
        return get_user_choice(options)
    choice = int(choice) - 1
    return options[choice]

calc_functions = {
    "Mean": mean,
    "Variance": variance,
    "Standard deviation": standard_deviation,
    "Range": range_calculation,
}

def get_date_range():
    print("Enter a date range (press Enter to skip either):")
    min_date = input("Start date (YYYY-MM-DD): ").strip() or None
    max_date = input("End date (YYYY-MM-DD): ").strip() or None
    return min_date, max_date

def menu(data_table):
    while True:
        print("\nSelect a data series (or type 'exit' to quit):")
        series_choice = get_user_choice(series_titles)
        if series_choice is None:
            break

        min_date, max_date = get_date_range()
        series = filter_series(
            data_table["Date"],
            data_table[series_choice],
            max_date=max_date,
            min_date=min_date,
        )

        print("\nSelect a calculation:")
        calc_choice = get_user_choice(list(calc_functions.keys()))
        if calc_choice is None:
            break

        result = calc_functions[calc_choice](series)
        print(f"\n{calc_choice} of {series_choice}: {result}")

if __name__ == "__main__":
    data = read_csv('weather.csv')
    menu(data)