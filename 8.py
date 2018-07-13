import random
#Thanks to great success in Monte-Carlo now we have 1000000$!

def compute(n, ca):
  cash = ca
	for i in range(n):
  cash = cash - 1
		a = random.randint(1, 6)
		b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    sum = a + b + c + d
		if (sum<9):
			cash= cash + 10
	return cash
	
n = int(input())
Kenterberry = compute(n, 1000000)

print(n)
print(Kenterberry)
