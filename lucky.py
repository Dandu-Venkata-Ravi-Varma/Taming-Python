def add(number):
	return sum(map(int, str(number)))
	
def sqsum(n):
	return sum(map((lambda m: m*m),map(int, str(n))))

def isprime(n):
    i = 2
    if n < 2:
        return False
    while i < n:        
        if n % i == 0:
            return False
        else:
            i += 1
    return True
T = int(raw_input())
count = 0
for i in xrange(T):
	Num = raw_input().split(" ")
	for j in xrange(int(Num[0]),int(Num[1])):
		S = add(j)
		SQN = sqsum(j)
		if (isprime(S) == True) and (isprime(SQN) == True):
			count = count + 1
	print count
	count = 0





