def tips(bill, servicerating):
    tip_percentages = {
        "terrible" : 0.0,
        "bad" : 0.5,
        "mid" : 0.10,
        "okay": 0.15,
        "good": 0.20,
        "great": 0.25 }

    if servicerating.lower() not in tip_percentages:
        print( "Invalid service rating. Please choose from 'terrible, 'bad', 'mid', 'okay', 'good', or 'great'.")

    tip_percentage = tip_percentages[servicerating.lower()]

    tip = bill * tip_percentage
    return tip

bill_amount = int(input("What was your bill amount?"))
service = input("How was your service?")
tip_amount = tips(bill_amount, service)
print(f"For a ${bill_amount} bill with {service} service, the tip is ${tip_amount:.2f} Thank you for choosing to dine with us. Have a splendid day!")
