def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    calc_median_temperature(num_list)

def display_main_menu():
    print("display_main_menu")

def get_user_input():
    userInput = input("Enter some numbers separated by commas (e.g. 5, 67, 32)"+ "\n")
    list = userInput.split(",")
    float_list = [float(i) for i in list]
    print (float_list)
    return float_list

def calc_average_temperature(list):
    average = sum(list)/ len(list)
    print("Average= ",average)
    return average

def calc_min_max_temperature(list):
    maximum = max(list)
    minimum = min(list)
    print("Max= " ,maximum)
    print("Min= " ,minimum)

def calc_median_temperature(list):
    x = sorted(list)
    print("Sorted list is " , x)
    mid = len(list) // 2
    result = (list[mid] + list[~mid]) / 2
    print("Median= ", result)

main()