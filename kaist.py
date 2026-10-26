"""kaist portfolio project:coloumb's law calculator"""
""" calculation of electrical force"""
"""defining values"""
k=9*10**9
q1=float(input("enter the first charge:"))
q2=float(input("enter the second charge:"))
r=float(input("enter the distance between two charges:"))
"""defining formula"""
formula=k*abs(q1*q2)/r**2
"""defining result"""
print("\n---results---")
print("the electrical force between the two charges is :",formula,"newton")
"""defining direction"""
if (q1>0 and q2>0)or(q1<0 and q2<0):
    print("the resulting force is repulsive")
else:
    print("the resulting force is attractive")
          
               
