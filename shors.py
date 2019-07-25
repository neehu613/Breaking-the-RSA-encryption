import os, random, time

def gcd(a, b):
	if a==0:
		return b
	return gcd(b%a, a)

def Pick_A(n):
	g = 0
	while g != 1:
		a = random.randrange(1, n)
		g = gcd(a, n)
	return a

#The below function needs to be implemented with Quantum Computing
def Find_Period(a, n):
	k=0
	res=0
	flag=0

	if (pow(a, 1, n) == 1):
		k=1
		flag=1

	while (res!=1):
		k += 1
		res = pow(a,k,n)
	
	if flag==0:
		return k
	return k-1

def Check_R(r, a, n):
	if(r%2==0) and ((pow(a, int(r/2))+1)%n != 0):
		return True
	return False

def shors(n):
	start_time = time.time()
	validity = False
	while validity == False:
		a = Pick_A(n)
		r = Find_Period(a, n)
		if Check_R(r, a, n):
			validity = True
	p = gcd((pow(a, int(r/2))+1), n)
	q = gcd((pow(a, int(r/2))-1), n)
	print("The prime factors are\np = ", p, "q = ", q)
	print("n = ", n)
	print("p*q = ", p*q)
	print("Time consumed : ", time.time()-start_time, "seconds")
	return p, q
