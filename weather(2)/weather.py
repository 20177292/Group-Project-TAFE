series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def medianIndex(in_series):
    if len(in_series) % 2 == 1:
        return([int(len(in_series) / 2 - 0.5)])
    else:
        return([int(len(in_series) / 2), int(len(in_series) / 2 - 1)])


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
    sortedList = sorted(in_series)
    return (sortedList[-1] - sortedList[0])

def iqr_calculation(in_series):
    q1 = []
    q3 = []
    sortedList = sorted(in_series)
    print(sortedList)
    firstHalf = sortedList[0:(int(medianIndex(sortedList)[0])+1)]
    secondHalf = sortedList[int(medianIndex(sortedList)[-1]):]
    q1indecies = medianIndex(firstHalf)
    for value in q1indecies:
        q1.append(firstHalf[value])
    q1 = sum(q1) / len(q1)

    q3indecies = medianIndex(secondHalf)
    for value in q3indecies:
        q3.append(secondHalf[value])
    q3 = sum(q3) / len(q3)

    return(q3 - q1)
    

def filter_series(date_series, data_series, max_date=None, min_date=None):
    # temporary stub matching the menu's call signature — replace with
    # the real implementation once #9 is merged
    result = []
    for date, value in zip(date_series, data_series):
        if min_date and date < min_date:
            continue
        if max_date and date > max_date:
            continue
        result.append(value)
    return result

def read_csv(file, default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    headers = lines[0]
    for i in range(len(headers)):
        if headers[i] == "Date":
            data_table[headers[i]] = [line[i] for line in lines[1:]]
        else:
            data_table[headers[i]] = [default_value if (len(line[i]) == 0) else float(line[i]) for line in lines[1:]]
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



def get_date_range():
    print("Enter a date range in YYYY-MM-DD format (press Enter to skip either):")
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

calc_functions = {
    "Mean": mean,
    "Variance": variance,
    "Standard deviation": standard_deviation,
    "Range": range_calculation,
    "IQR" : iqr_calculation
}

if __name__ == "__main__":
    data = read_csv('weather.csv')
    menu(data)
