import random
import time

def main():
	print("WELCOME THE PICK ORDER RANDOMIZER PROGRAM\n\n\n")

	n = int(input("please enter the number of teams in your league : "))

	teams=Take_Team_Names(n)

	random.shuffle(teams)

	print("\n\n")
	print_orders(teams,n)

def Take_Team_Names(n): #the function that takes names of teams from the user.

	Team_Names=[]

	for team in range(0,n):

		name=input(f"Name of Team {team+1}   : ")
		Team_Names.append(name)

	return Team_Names	


def print_orders(Team_Names,n): #the function to print shuffled order.

		for order in range(0,n):

			if order < 7:
				time.sleep(7-order)
			print(f"Pick {order+1}  :  {Team_Names[order]}\n")



main()	
