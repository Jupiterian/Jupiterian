N = float(input("Enter a number. "))
numbers = []
count = 1
while not (N == 1):
    numbers.append(N)
    if N%2 == 0:
        N = N/2
    else: 
        N = 3*N + 1
    count +=1
numbers.append(1.0)
print (f"The sequence is {count} numbers long after it reaches 1 for the first time. This happens after the operation is applied {count - 1} times.")
print(f"The numbers in the sequence are {numbers}.")
