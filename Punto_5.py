myArray = [1,2,1,3,3,1,2,1,5,1]
my_array = {}

for i in myArray:
	if i in my_array:
		my_array[i] += 1
	else:
		my_array[i] = 1

for valor in sorted(my_array):
  print(f'{valor}: {"*" * my_array[valor]}')