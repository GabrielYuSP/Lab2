import Lab2

print("Test_Lab2")


def test_find_min_max():
    input_arr = [1, 2, 3, 4, 5]
    test_max = 5
    test_min = 1
    maximum, minimum = Lab2.calc_min_max_temperature(input_arr)

    assert (test_max == maximum and test_min == minimum)


def test_calc_average():
    input_arr = [1, 2, 3, 4, 5]
    test_average = 3
    average = Lab2.calc_average_temperature(input_arr)

    assert (test_average == average)


def test_calc_median_temperature():
    input_arr = [1, 2, 3, 4, 5]
    test_median = 3
    median = Lab2.calc_median_temperature(input_arr)

    assert (test_median == median)
