

def Finding_Primes(num):

	#Creating empty primes list to append all prime numbers from 0 to  given number "num".
	Primes=[]
	
	for i in range(2,num+1):

		temp=0

		for j in range(2,num+1):
			
			if i<j: break
			elif i%j==0:
				temp+=1
				
		if temp==1 : Primes.append(i)

	return Primes	


	

def Prime_Factors(num):

	primeFactors=[]
	primes=Finding_Primes(num)
	while num > 1 :
		for prime in primes:

			if num % prime==0:
				primeFactors.append(prime)
				num=num/prime
				break
	return primeFactors			






num=input("please enter the number you want to learn all prime factors.\n")

b=Prime_Factors(int(num))	
print(b)