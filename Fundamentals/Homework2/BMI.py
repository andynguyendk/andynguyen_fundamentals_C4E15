hicm = int(input("Your height (in cm) = "))
wgt = int(input("Your weight (in kg) = "))
him = hicm/100
BMI = round(wgt/(him**2),2)
print("Your BMI is ", BMI)
if BMI <16:
    print("you're severely underweight")
elif BMI < 18.5:
    print("you're undereight")
elif BMI < 25:
    print("you're normal")
elif BMI <30:
    print("you're overweight")
elif BMI< 40:
    print("you're obese")
else:
    print("which planet are you from?")
# Underweight if BMI is between 16 and 18.5
# Normal if BMI is between 18.5 and 25
# Overweight if BMI is between 25 and 30
# Obese if BMI is more than 30
