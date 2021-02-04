import math
def distance(x1,y1,x2,y2):
   AB=math.sqrt((x2-x1)**2+(y2-y1)**2)
   return AB
x1=int(input("Enter x value in A point:"))
y1=int(input("Enter y value in A point:"))
x2=int(input("Enter x value in B point:"))
y2=int(input("Enter y value in B point:"))
res=distance(x1,y1,x2,y2)
print("Distance =",res)

