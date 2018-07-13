import random

def compute(n):
	sixes = 0
	for i in range(n):
		a = random.randint(1, 6)
		b = random.randint(1, 6)
		if (a == 6 or b == 6):
			sixes += 1
	return sixes / n
	
n = int(input())
sol = 0.3055555
MonteCarlo = compute(n)
while abs(MonteCarlo - sol) >= 0.0001:
	n = n * 2
	MonteCarlo = compute(n)

print(n)
print(MonteCarlo)
