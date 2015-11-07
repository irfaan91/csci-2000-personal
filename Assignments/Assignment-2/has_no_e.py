def has_no_e(string):
	count = 0
	for c in data:
		if c == 'e':
			count += 1
		string = reader.read()
	if count == 0:
		return 'True'
	else:
		return 'False'	

reader = open('gadsby_stripped.txt', 'r')
data = reader.read()
print(has_no_e(data))
reader.close()
## Irfaan Ali
## 100400606

