print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())
number_of_people = int(input())

tip_total = (tip_percentage / 100) * bill_amount
total = bill_amount + tip_total

total_per_person = total / number_of_people

print(f"Total (including tip): ${total}")
print(f"Each person pays: ${total_per_person}")
