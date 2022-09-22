import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="freshking08",
  database="usersdb"
)

mycursor = mydb.cursor()

print('Hello Genius.\nHow do you want to search for this name?')

while True:
    try:
        def answer():
            print('Press 1 to use ID \nPress 2 to use First Name \nPress 3 to use Last Name')
            global choice
            choice = int(input('Answer:'))
        answer()
        if choice ==1:
            id = str(input('What is the ID of the person?:'))
            mycursor.execute("SELECT * FROM info WHERE id ='"+id+"'")
            result = mycursor.fetchall()
            print(result)

        elif choice == 2:
            first = str(input('Enter the correct letters in the first name:'))
            mycursor.execute("SELECT * FROM info WHERE firstname REGEXP '"+first+"'")
            result = mycursor.fetchall()
            print(result)
        
        elif choice == 3:
            last = str(input('Enter the correct letters in the last name:'))
            mycursor.execute("SELECT * FROM info WHERE lastname REGEXP '"+last+"'")
            result = mycursor.fetchall()
            print(result)

    except ValueError:
        print('You didn\'t use the right value')
        pass

    redo=int(input('Do you want to do something else?\nIf yes, type 1\nIf no, type 2\n'))
    if redo == 1:
        print('Alright. Search again')
    else:
        print('Goodbye!')
        break


