#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

max_n = 0
while max_n == 0:
	n = input('Введите целое положительное число ')
	if n.isdigit() and int(n) > 0:
		number = int(n)
		while number != 0:
			if number % 10 > max_n:
				max_n = number % 10
				number = number // 10
			else:
			    number = number // 10
	else:
	    print('Требуется ввести целое положительное число')
print(max_n)
