# Write your code here
def months_required():
    months_required = 0
    annual_salary = int(input("What is your salary?"))
    portion_saved = float(input("What would percent you like to save?")) 
    total_cost = int(input("Cost of dream house?"))
    portion_down_payment = 0.25
    down_payment = total_cost*portion_down_payment
    r = float(.04)
    current_savings = 0
    while current_savings < down_payment:
        current_savings += (annual_salary/12*portion_saved) + (current_savings * (r/12))
        print(current_savings)
        months_required += 1
        print("it will take you ", months_required,"months to buy your house.")
months_required()

