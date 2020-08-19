def dec_to_bin(n):
	if n < 0:
		return bin(n * -1)[2:]
	return bin(n)[2:]


def trim_to(number, length):
    zeroes = ''
    for i in range(int(length) - len(number)):
    	zeroes += '0'
    return zeroes + number


def bit_not(number):
	negated = ''
	for bit in number:
		if bit == '1':
			negated += '0'
		elif bit == '0':
			negated += '1'
	return negated


def add_one(number, length):
	addone = ''
	carryover = ''
	if number[len(number) - 1] == '0':
		addone += number[:-1]
		addone += '1'
		return addone
	else: #Not the best way to do a bitwise addition but it works
		carryover = '1' #Because the number we start with is 1 and 1 + 1 = 0 with carryover 1
		#We iterate through the number but in reversed order sind we start the addition from the end.
		for bit in number[::-1]:
			if bit == '0':
				if carryover == '1':
					addone += '1'
					carryover = '0'
				else:
					addone += '0'
			if bit == '1':
				if carryover == '1':
					addone += '0'
				else:
					addone += '1'
					carryover = '0'
	return trim_to(addone[::-1], length)


if __name__ == '__main__':
	number = input('Enter the (decimal) number you want to convert to the Two\'s Complement: ')
	bitlength = len(dec_to_bin(int(number)))
	
	length = input('Enter the length to which your number should be trimmed to: ')
	if bitlength > int(length):
		print('You should use at least a length equal or greater then the binary number itself!')
	else:
		if int(number) >= 0:
			bit = trim_to(dec_to_bin(int(number)), length)

			print('\nConverting ' + number + ' using the bit length ' + length + ' to -> ' + bit)
			print('Finally we get...')
			print(trim_to(dec_to_bin(int(number)), length))
		else:
			bit = trim_to(dec_to_bin(int(number)), length)
			not_bit = bit_not(bit)

			print('\nConverting the positive number of ' + number + ' using the bit length ' + length + ' to -> ' + bit)
			print('Negating ' + bit + ' to -> ' + not_bit)
			print('Finally add 1 to the negated number and we get...')
			print (add_one(not_bit, length))

	print('\nEnd...')