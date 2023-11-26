def main():
    display_main_menu()
    num_list = get_user_input()
    average = calc_average_temperature(num_list)
    print("Average=",average)
    maximum, minimum = calc_min_max_temperature(num_list)
    print("Max= ", maximum)
    print("Min= ", minimum)
    median = calc_median_temperature(num_list)
    print("Median= ", median)

def display_main_menu():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def get_user_input():
    userInput = input("Enter some numbers separated by commas (e.g. 5, 67, 32)"+ "\n")
    list = userInput.split(",")
    float_list = [float(i) for i in list]
    return float_list

def calc_average_temperature(list):
    average = sum(list)/ len(list)
    return average

def calc_min_max_temperature(list):
    maximum = max(list)
    minimum = min(list)
    return maximum, minimum

def calc_median_temperature(list):
    x = sorted(list)
    mid = len(list) // 2
    result = (x[mid] + x[~mid]) / 2
    return result


if __name__ == '__main__':
    main()