class EB:
    def setData(self):
        print(("\nEnter following inputs for develop Electricity bill\n"))
        try:
            self.cid=int(input('Consumer ID: '))
        except  Exception as e:
            print("Err: Invalid Consumer ID")
            exit(0)
        try:
            self.pr = int(input('Previous Reading: '))
        except  Exception as e:
            print("Err: Invalid Previous Reading")
            exit(0)
        try:
            self.cr = int(input('Current Reading: '))
        except  Exception as e:
            print("Err: Invalid Current Reading")
            exit(0)
        try:
            self.cc = input('Consumer Category: ')
        except Exception as e:
            print("Err: Invalid Consumer Category")
            exit(0)
        if self.cid < 1001:
            print("\nErr.: Consumer ID > 1000")
            exit(0)
        if self.cr < 0 or self.pr < 0 or (self.cr < self.pr):
            print("\nErr.: Invalid Current or Previous Reading")
            exit(0)
        if self.cc not in ("Agriculture", "Domestic", "Commercial"):
            print("\nErr.: Invalid Consumer Category")
            exit(0)
        return
    def computeData(self):
        self.nr=self.cr - self.pr
        self.cuu100=self.cuu200=self.cuu400=self.cua400=0
        if self.cc == "Agriculture":
            self.puau100 = 0.50
            self.puau200 = 1.00
            self.puau400 = 1.50
            self.puaa400 = 2.00
            self.mc=25
            self.tip=0.5
        elif self.cc == "Domestic":
            self.puau100 = 1.00
            self.puau200 = 1.50
            self.puau400 = 2.00
            self.puaa400 = 2.50
            self.mc = 25
            self.tip = 1.0
        else:
            self.puau100 = 2.00
            self.puau200 = 3.00
            self.puau400 = 4.00
            self.puaa400 = 5.00
            self.mc = 300
            self.tip = 2.0
        if self.nr > 400:
            self.cuu100 = 100
            self.cuu200 = 100
            self.cuu400 = 200
            self.cua400 = self.nr - 400
        elif self.nr > 200:
            self.cuu100 = 100
            self.cuu200 = 100
            self.cuu400 = self.nr - 200
        elif self.nr > 100:
            self.cuu100 = 100
            self.cuu200 = self.nr - 100
        elif self.nr > 0:
            self.cuu100 = self.nr
        self.cuau100 = self.cuu100 * self.puau100
        self.cuau200 = self.cuu200 * self.puau200
        self.cuau400 = self.cuu400 * self.puau400
        self.cuaa400 = self.cua400 * self.puaa400
        if self.cuaa400 > 0:
            self.tia = self.cuaa400 * self.tip / 100
        else:
            self.tia = 0
        self.np=self.cuau100 + self.cuau200 + self.cuau400 + self.cuaa400 + self.tia + self.mc
        return
    def showData(self):
        self.computeData()
        print("\nConsumer ID:%d" %(self.cid))
        print("\nPrevious Reading:%d" %(self.pr))
        print("\nCurrent Reading:%d" %(self.cr))
        print("\nNet Reading:%d" %(self.nr))
        print("\nConsumer Category:%s" %(self.cc))
        print("\n%d %.2f %.2f" %(self.cuu100, self.puau100, self.cuau100))
        print("\n%.2f %.2f" %(self.tia, self.tip))
        print("\n%.2f" %(self.mc))
        print("\n%.2f" %(self.np))
        return
obj=EB()
obj.setData()
obj.showData()
'''
Agriculture
output 1
Enter following inputs for develop Electricity bill
Consumer ID: 1001
Previous Reading: 0
Current Reading: 550
Consumer Category: Agriculture
Consumer ID:1001
Previous Reading:0
Current Reading:550
Net Reading:550
Consumer Category:Agriculture
100 0.50 50.00
1.50 0.50
25.00
776.50

output 2
Enter following inputs for develop Electricity bill
Consumer ID: 1002
Previous Reading: 0
Current Reading: 350
Consumer Category: Agriculture
Consumer ID:1002
Previous Reading:0
Current Reading:350
Net Reading:350
Consumer Category:Agriculture
100 0.50 50.00
0.00 0.50
25.00
400.00

output 3
Enter following inputs for develop Electricity bill
Consumer ID: 1003
Previous Reading: 0
Current Reading: 150
Consumer Category: Agriculture
Consumer ID:1003
Previous Reading:0
Current Reading:150
Net Reading:150
Consumer Category:Agriculture
100 0.50 50.00
0.00 0.50
25.00
125.00

output 4
Enter following inputs for develop Electricity bill
Consumer ID: 1004
Previous Reading: 0
Current Reading: 50
Consumer Category: Agriculture
Consumer ID:1004
Previous Reading:0
Current Reading:50
Net Reading:50
Consumer Category:Agriculture
50 0.50 25.00
0.00 0.50
25.00
50.00

Domestic
output 1
Enter following inputs for develop Electricity bill
Consumer ID: 1001
Previous Reading: 0
Current Reading: 550
Consumer Category: Domestic
Consumer ID:1001
Previous Reading:0
Current Reading:550
Net Reading:550
Consumer Category:Domestic
100 1.00 100.00
3.75 1.00
25.00
1053.75

output 2
Enter following inputs for develop Electricity bill
Consumer ID: 1002
Previous Reading: 0
Current Reading: 350
Consumer Category: Domestic
Consumer ID:1002
Previous Reading:0
Current Reading:350
Net Reading:350
Consumer Category:Domestic
100 1.00 100.00
0.00 1.00
25.00
575.00

output 3
Enter following inputs for develop Electricity bill
Consumer ID: 1003
Previous Reading: 0
Current Reading: 150
Consumer Category: Domestic
Consumer ID:1003
Previous Reading:0
Current Reading:150
Net Reading:150
Consumer Category:Domestic
100 1.00 100.00
0.00 1.00
25.00
200.00

output 4
Enter following inputs for develop Electricity bill
Consumer ID: 1004
Previous Reading: 0
Current Reading: 50
Consumer Category: Domestic
Consumer ID:1004
Previous Reading:0
Current Reading:50
Net Reading:50
Consumer Category:Domestic
50 1.00 50.00
0.00 1.00
25.00
75.00

Commercial
output 1
Enter following inputs for develop Electricity bill
Consumer ID: 1001
Previous Reading: 0
Current Reading: 550
Consumer Category: Commercial
Consumer ID:1001
Previous Reading:0
Current Reading:550
Net Reading:550
Consumer Category:Commercial
100 2.00 200.00
15.00 2.00
300.00
2365.00

output 2
Enter following inputs for develop Electricity bill
Consumer ID: 1002
Previous Reading: 0
Current Reading: 350
Consumer Category: Commercial
Consumer ID:1002
Previous Reading:0
Current Reading:350
Net Reading:350
Consumer Category:Commercial
100 2.00 200.00
0.00 2.00
300.0
1400.00

output 3
Enter following inputs for develop Electricity bill
Consumer ID: 1003
Previous Reading: 0
Current Reading: 150
Consumer Category: Commercial
Consumer ID:1003
Previous Reading:0
Current Reading:150
Net Reading:150
Consumer Category:Commercial
100 2.00 200.00
0.00 2.00
300.00
650.00

output 4
Enter following inputs for develop Electricity bill
Consumer ID: 1004
Previous Reading: 0
Current Reading: 50
Consumer Category: Commercial
Consumer ID:1004
Previous Reading:0
Current Reading:50
Net Reading:50
Consumer Category:Commercial
50 2.00 100.00
0.00 2.00
300.00
400.00
'''



