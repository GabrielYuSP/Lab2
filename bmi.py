def calculate_bmi(height, weight):
    print("Height = " + str(height) + "m")
    print("Weight = " + str(weight) + "kg")
    bmi = weight/(height*height)
    roundedBMI = round(bmi,2)
    print ("BMI = " + str(bmi))
    print ("BMI (2dp) = " + str(roundedBMI))

    if (bmi <= 18.5):
        print ("Underweight")

    if (bmi >= 18.5 and bmi <= 25.0):
        print ("Normal Weight")

    else:
        print ("Overweight")

calculate_bmi(weight=57, height=1.43)
