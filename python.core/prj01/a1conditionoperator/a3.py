cc = input("Consumer Category for electricity bill:")
if cc == "Agriculture":
    print("per unit amount 0.25 for", cc)
else:
    if cc == "Domestic":
        print(("per unit amount 0.50 for", cc))
    else:
        if cc == "Commercial":
            print("per unit amount 2.00 for", cc)
        else:
            print("Invalid Consumer Category")
'''
output 1
Consumer Category for electricity bill:Domestic
('per unit amount 0.50 for', 'Domestic')
output 2
Consumer Category for electricity bill:DOMESTIC
Invalid Consumer Category
'''