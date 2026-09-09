
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

def menu(data_table):
    print("Select a data series:")

    choice = get_user_choice(series_titles)
    series = data_table[choice]
    print(f"Mean: {mean(data_table[choice])}")

#if __name__ == "__main__":
#    data = read_csv('weather.csv')
#    menu(data)
