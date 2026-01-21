cunits = 0
cuau50 = 0
cuau150 = 0
cuau250 = 0
cuaa250 = 0
cunits = input("Enter Consume Units:")
try:
    cunits = int(cunits)
except Exception as e:
    print("err...Invalid Consume units")
    exit(1)
if cunits < 0:
    print("err...Invalid Consume units")
    exit(1)
if cunits > 250:
    cuau50 = 50 * 1.50
    cuau150 = 100 * 2
    cuau250 = 100 * 3
    cuaa250 = (cunits - 250) * 4
elif cunits > 150:
    cuau50 = 50 * 1.50
    cuau150 = 100 * 2
    cuau250 = (cunits - 150) * 3
    cuaa250 = 0
elif cunits > 50:
    cuau50 = 50 * 1.50
    cuau150 = (cunits - 50) * 2
    cuau250 = 0
    cuaa250 = 0
else:
    cuau50 = cunits * 1.50
    cuau150 = 0
    cuau250 = 0
    cuaa250 = 0
np = cuau50 + cuau150 + cuau250 + cuaa250
print("Electricity Bill...")
print(f"Consume Units: {cunits}")
print(f"Consume Units amount upto 50: {cuau50}")
print(f"Consume Units amount upto 150: {cuau150}")
print(f"Consume Units amount upto 250: {cuau250}")
print(f"Consume Units amount above 250: {cuaa250}")
'''
output 1
Enter Consume Units:-1
err...Invalid Consume units
output 2
Enter Consume Units:fox
err...Invalid Consume units
output 3
Enter Consume Units:25
Electricity Bill...
Consume Units: 25
Consume Units amount upto 50: 37.5
Consume Units amount upto 150: 0
Consume Units amount upto 250: 0
Consume Units amount above 250: 0
output 4
Enter Consume Units:75
Electricity Bill...
Consume Units: 75
Consume Units amount upto 50: 75.0
Consume Units amount upto 150: 50
Consume Units amount upto 250: 0
Consume Units amount above 250: 0
output 5
Enter Consume Units:200
Electricity Bill...
Consume Units: 200
Consume Units amount upto 50: 75.0
Consume Units amount upto 150: 200
Consume Units amount upto 250: 150
Consume Units amount above 250: 0
output 6
Enter Consume Units:300
Electricity Bill...
Consume Units: 300
Consume Units amount upto 50: 75.0
Consume Units amount upto 150: 200
Consume Units amount upto 250: 300
Consume Units amount above 250: 200
'''