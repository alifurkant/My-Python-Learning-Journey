

def Finding_Primes(num):

	#Creating empty primes list to append all prime numbers from 0 to  given number "num".
	Primes=[]
	
	for i in range(2,num+1): #i is the number that checked whether it is prime.

		temp=0

		for j in range(2,i+1): #every number until i is being tested.
			
			if i%j==0:
				temp+=1
				
		if temp==1 : Primes.append(i) #it recorded if it is divided at least once.

	return Primes	


	

def Prime_Factors(num):

	primeFactors=[]
	primes=Finding_Primes(num)
	while num > 1 : #the number divided for prime numbers until it reaches 1.
		for prime in primes:

			if num % prime==0:
				primeFactors.append(prime) #if number is divided by prime number, prime number added to list.
				num=num/prime
				break
	return primeFactors			






num=input("please enter the number you want to learn all prime factors.\n")

b=Prime_Factors(int(num))	
print(f"Prime Factors of {num} is : \n{b}")
	
