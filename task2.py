def calculate_bmi():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            print("Invalid input. Please enter positive numbers.")
            return
        
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 25:
            print("Category: Normal weight")
        elif 25 <= bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculate_bmi()
