import sqlite3
try:
	db = sqlite3.connect('db.sqlite3')

	cursor = db.cursor()
	
	print "Sign Up now !"
	name = raw_input("Your Name: ")
	email = raw_input("Your Email: ")
	password = raw_input("Your Password: ")

	cursor.execute('''INSERT INTO users(name, email, password) VALUES(:name, :email, :password)''', {'name': name, 'email': email, 'password': password})
	db.commit()

	print "You have been registered !"

	cursor.execute('''SELECT * FROM users WHERE email=?''', (email,))
	user = cursor.fetchone()

	print "Your name is: ", user[1]
	print "Your email is: ", user[2]
	print "Your password is: ", user[3]
	
	'''fh = open('script.txt', 'r')
	script = fh.read()
	cursor.executescript(script)
	print "Executed"'''
except Exception as e:
	db.rollback()
	raise e
finally:
	db.close()