'''create pythn proram that ask the user how far they want to travel .
if they want to travel for <3 miles tell them to ride a bicycle 
if they want to travel >3 and <100 tell them to use a motorcycle 
if they want to travel >300 tell them to use a super car'''
distance=int(input("how far you want to travel in miles "))
if distance<3:
    print("Ride bicycle")
    
elif distance>=3 and distance<100:
    print("Ride motorcycle")
    
else:
    print("Drive super-car")