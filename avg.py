print("Please enter 5 numbers")
total = 0
inputs = ""
minmax = []
for i in range(5):
	inputs= int(input(": "))
	total += inputs
	minmax.append(inputs)
print("average =" , (total/5))
print("min =", min(minmax))
print("max =", max(minmax))

