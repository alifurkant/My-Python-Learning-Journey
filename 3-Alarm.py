import winsound
import time


def ask_user():

	#ask user the time they want to set the alarm.

	set_hour=int(input("please enter the desired hours of alarm :"))
	set_minute=int(input("please enter the desired minutes of alarm :"))
	set_seconds=int(input("please enter the desired seconds of alarm :"))

	#convert the input hour and minutes to seconds and return.

	return set_hour*3600+set_minute*60+set_seconds



def main():

	#wait until the time user entered run out.
	time.sleep(ask_user())

	#ring 5 times.

	for i in range(0,5):
		winsound.PlaySound("SystemQuestion",winsound.SND_ALIAS)

main()
