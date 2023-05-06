neg = []
zero= []
pos = []

print("Enter an integer (blank to quit):" , end=" ")
value = input()
while value!="" :
    value = int(value);
    if value<0:
        neg.append(value)
    elif value == 0:
        zero.append(value)
    elif value>0:
        pos.append(value)
print("Enter an integer (blank to quit):" , end=" ")
value = input()
print("The numbers were:")
for i in range(len(neg)):
    print(neg[i])
for i in range(len(zero)):
    print(zero[i])
for i in range(len(pos)):
    print(pos[i])