# BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
# Martin Quinn - PTA18070

import sqlite3
import time
import datetime

conn = sqlite3.connect('BMI.db')
c = conn.cursor()

def menu():
	print("\npress 1 : to add your profile.")
	print("press 2 : to check your profile. ")
	print("press 3 : to check all profiles. ")
	print("press q : to quit program. ")
	return input('What would you like to do?\n Enter a valid entry: ')


def createTable():
	c.execute('CREATE TABLE IF NOT EXISTS users(datestamp TEXT, name TEXT, weight FLOAT, height FLOAT, bmi FLOAT, information TEXT)')

createTable()
run = menu()

def search():
	person = input("What is your name?\n")
	c.execute("SELECT * FROM users WHERE name = (?)",(person,))
	data = c.fetchall()
	print(data[0])
#	print("%s You are %.2f cms, and you are %.2f kg\nYour BMI is %f, This means you are %s" % (name, height, weight, BMI, information))

	if data == [(0,)]:
		print("user not in database, please add user")
		create()
		return 0
	else:
		return 0

def create():
	
	name = str(input("\nWhat is your name?\n"))
	
	c.execute("SELECT * FROM users WHERE name = (?)",(name,))
	data = c.fetchall()
	if data != []:
		return print("user already in database.")
		return 0
	else:
		unix = time.time()
		date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H:%M:%S'))
		stone = int(input( "How many stone?\n" ))
		pounds = int(input( "How many pounds?\n" ))
		feet = int(input("How many foot?\n"))
		inches = int(input("How many inches?\n"))
		verdict = ""
	
		weight = (stone * 6.35029318) + (pounds * 0.45359237)

		heightcm = (feet * 30.48) + (inches * 2.54)

		heightm = heightcm * 0.01

		BMI = (weight / (heightm * heightm))
		if BMI <= 18.5:
			verdict = "Underweight, eat something"
		elif BMI > 18.5 and BMI < 25:
			verdict = "A Healthy weight, keep it up"
		elif BMI >= 25 and BMI < 30:
			verdict = "Overweight, although if you are sporty with muscle mass you are healthy. if not, cut down on the food yo." 
		elif BMI >= 30:
			verdict = "Obese, just stop eating."

		print("%s You are %.2f cms, and you are %.2f kg\nYour BMI is %f, This means you are %s" % (name, heightcm, weight, BMI, verdict))

		c.execute("INSERT INTO users (datestamp, name, weight, height, bmi, information) VALUES (?,?,?,?,?,?)",
		  (date, name, weight, heightcm, BMI, verdict))
	
		conn.commit()

def showall():
	try:
		conn = sqlite3.connect('BMI.db')
		c = conn.cursor()
		c.execute("SELECT * FROM users")
		
		row = c.fetchone()
		
		while row is not None:
			print(row)
			row = c.fetchone()
			
	except Error as e:
		print(e)
 
	finally:
		menu()
			

while True:
	# to add user #
		if run == '1':
			create()
			run = menu()
	# to check user #
		elif run == '2':
			search()
			run = menu()
	# to check all users
		elif run == '3':
			showall()
		elif run == 'q':
			break
	# any other input during the menu #
		else:
			print("not a valid selection, please choose again below")
			run = menu()

c.close()
conn.close()
