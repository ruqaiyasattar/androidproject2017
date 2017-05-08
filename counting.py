

##example 4.3
for count in range(1,21):
    print(str(count)+"\n")

#example 4.4

number=list(range(1,100))
for num in number:
    print(str(num)+"\n")


mylist=list(range(1,100))
print("minimum value in list is: "+str(min(mylist)))
print("maximum value in list is: "+str(max(mylist)))
print("sum of whole list is: "+str(sum(mylist))+"\n")

print("Odd numbers are:")
for val in range(1,21,2):
    print(val)

print("multiplies of 3 from 3 to 30:")
multiple=[val**3 for val in range(3,30)]
print(multiple)

print("cube via for loop")
cube=[]
for val in range(1,11):
    square=val**3
    cube.append(square)
print(str(cube)+"\n")



print("cube from 1 to 10:")
cube=[val**3 for val in range(1,10)]
print(cube)

#4.10 example
print("\nprinting first three elements from cube list")
for newdata in cube[:3]:
    print(newdata)


print("\nprinting three elements from the middle of cube list")
for newdata in cube[int(len(cube)/2-1):int(len(cube)/2+1)]:
    print(newdata)


print("\nprinting last three elements from cube list")
for new in cube[-3:]:
    print(new)
