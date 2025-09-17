import ascii as a
import mysql.connector



try:
    mydb = mysql.connector.connect(
        host="localhost",  # Or the IP address of your MySQL server
        user="root",
        password="",
        database="cricket"  # The name of your existing database
    )

except mysql.connector.Error as err:
    print(f"Error: {err}")


mycursor = mydb.cursor()


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[97m'
RESET = '\033[0m'

while True:

    t = []
    x = str(input("Enter the teams you want to see : "))

    mycursor.execute(f"SELECT name FROM players WHERE intlTeam = '{x}';")

    result = mycursor.fetchall()

    def flag():
        a.ascii(f'images/{x}.jpg', 40)

    if __name__ == "__main__":
        flag()

    if x == "India" :
        print(BLUE + "INDIAN CRICKET TEAM" + RESET)
    elif x == "Pakistan":
        print(GREEN + "PAKISTAN CRICKET TEAM" + RESET)
    elif x=="Australia":
        print(YELLOW + "AUSTRALIAN CRICKET TEAM" + RESET)
    elif x == "South Africa":
        print(MAGENTA + "SOUTH AFRICAN CRICKET TEAM" + RESET)
    elif x == "New Zealand":
        print(CYAN + "NEW ZEALAND CRICKET TEAM" + RESET)
    elif x=="England":
        print(RED + "ENGLISH CRICKET TEAM" + RESET)
    
    for i in result:
        print(i[0])





