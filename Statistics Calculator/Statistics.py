#/bin/python3

import statistics
dataSet = input("Enter data set: ").split(", ")
data = []

for x in dataSet:
    data.append(float(x))

#Quartiles
quartiles = statistics.quantiles(data)
print(f"Q1 is equal to {quartiles[0]}.")
print(f"The median is equal to {quartiles[1]}.")
print(f"Q3 is equal to {quartiles[2]}.")

#IQR
print(f"The IQR is {quartiles[2] - quartiles[0]}. ")

#Range
max = max(data)
min = min(data)
print(f"The range is equal to {max - min}.")

#Mean
mean = statistics.mean(data)
print(f"The mean is {mean}.")

#MAD
MAD = []
for x in data:
    MAD.append(abs(x - mean))
print(f"The MAD is {statistics.mean(MAD)}.")

#Mode
print(f"The mode is {statistics.mode(data)}.")