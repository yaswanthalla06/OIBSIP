#.................... BMI CALCULATOR .................
def calbmi(w,h):
    bmi = w/(h*h)
    return bmi

# Main program
print("=== BMI CALCULATOR ===")

try:
    w = float(input("Enter your weight in kg: "))
    h = float(input("Enter your height in meters: "))

    if w <= 0 or h<= 0:
        print("Error: Weight and height must be positive numbers.")
    else:
        bmi = calbmi(w,h)
        print("Your BMI is:", round(bmi,2))

        if bmi < 18.5:
            print("Category: Underweight")
            print("Suggestion: Eat nutritious food and maintain a healthy diet.")
        elif bmi < 25:
            print("Category: Normal weight")
            print("Suggestion: Great! Maintain your healthy lifestyle.")
        elif bmi < 30:
            print("Category: Overweight")
            print("Suggestion: Try regular exercise and balanced meals.")
        else:
            print("Category: Obese")
            print("Suggestion: Consult a doctor and follow a fitness plan.")

except ValueError:
    print("Error: Please enter valid numbers only.")