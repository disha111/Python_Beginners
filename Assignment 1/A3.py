def factorial(number): 
	if(number == 0 or number == 1): 
		fact = 1
	else: 
		fact = number * factorial(number - 1) 
	return fact 

def strong_number(list): 
	new_list =[] 

	for x in list: 
		temp = x 
		sum = 0
		while(temp): 
			rem = temp % 10
			sum += factorial(rem) 
			temp = temp // 10
		if(sum != x or x == 0 != 1): 
			pass
		else: 
			new_list.append(x) 
			
	return new_list 
list = [145,375,0,100,2] 
strong_list = strong_number(list) 
print(strong_list) 

