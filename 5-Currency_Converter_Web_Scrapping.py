
import requests
import bs4
from datetime import datetime

def ask_convertion(): #function to call user conversion currencies.
	answer='6'
	while answer!="0" and answer!="1" and answer!="2"and answer!="3"and answer!="4" and answer!="5":
		print("\n\n\n0: From USD to TRY ")
		print("1: From EURO to TRY ")
		print("2: From TRY to USD ")
		print("3: From TRY to EURO ")
		print("4: From USD to EURO ")
		print("5: From EURO to USD \n")

		answer=input("Please identify your currency covertion with numbers above : ")
	return answer

def comma_to_dot_converter(currency): 

#convertion rates come with comma from the source. it should be changed to dot and string should be changed to float from string.

	currency_num=""

	for char in currency:
		if char == ',':
			char='.'
		currency_num=currency_num+char

	currency_num=float(currency_num)

	return currency_num

def get_Data(conversion_type):

	#function that gets conversion rates from the source according to user's input.
	
	url=requests.get("https://www.bloomberght.com/doviz")

	soup=bs4.BeautifulSoup(url.text,"html.parser")

	if conversion_type== '0' :

		currency=(soup.select("small.value.LastPrice")[1]).getText()
		currency=comma_to_dot_converter(currency)
		

	elif conversion_type== '1' : 

		currency=(soup.select("small.value.LastPrice")[2]).getText()
		currency=comma_to_dot_converter(currency)
		

	elif conversion_type== '2' :

		currency=(soup.select("small.value.LastPrice")[1]).getText()
		currency=comma_to_dot_converter(currency)
		currency=1/currency	
	
	elif conversion_type== '3' :

		currency=(soup.select("small.value.LastPrice")[2]).getText()
		currency=comma_to_dot_converter(currency)
		currency=1/currency	

	elif conversion_type== '4' : 

		currency=(soup.select("small.value.LastPrice")[3]).getText()
		currency=comma_to_dot_converter(currency)
		currency=1/currency	

	elif conversion_type== '5' : 

		currency=(soup.select("small.value.LastPrice")[3]).getText()
		currency=comma_to_dot_converter(currency)

	return currency	

def Last_Print(conversion_type):
	
	#function that helps print the correct currency names at the last print.
	Last_Print=[]

	if conversion_type =='0':

		Last_Print.append("USD")
		Last_Print.append("TRY")

	elif conversion_type =='1':

		Last_Print.append("EURO")	
		Last_Print.append("TRY")	

	elif conversion_type =='2':

		Last_Print.append("TRY")
		Last_Print.append("USD")	

	elif conversion_type =='3':

		Last_Print.append("TRY")	
		Last_Print.append("EURO")		

	elif conversion_type =='4':

		Last_Print.append("USD")
		Last_Print.append("EURO")	

	elif conversion_type =='5':

		Last_Print.append("EURO")	
		Last_Print.append("USD")	

	return Last_Print				

def main():

	conversion_type= ask_convertion()

	currency_multiplier= get_Data(conversion_type)

	now = datetime.now()

	current_time = now.strftime("%Y-%m-%d %H:%M:%S")

	Money = float(input("\nAmount : "))

	Last=Last_Print(conversion_type)

	print(f"\n{Money} {Last[0]} = {Money*currency_multiplier} {Last[1]} at {current_time}")


main()
