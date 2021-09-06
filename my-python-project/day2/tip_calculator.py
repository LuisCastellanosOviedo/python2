print(" welcome to the tip calculator !!!!")
bill = float(input("What wasthe total bill ??? $$$ "))
tip = int(input("How much tip do you want to give ? 10 , 12 , 15 ??"))
people = int(input("How many people to split the bill ? "))


tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill/people
final_amout = round(bill_per_person, 2)
final_amout = "{:.2f}".format(final_amout)
print(f" Each person should pay:  ${final_amout} ")




