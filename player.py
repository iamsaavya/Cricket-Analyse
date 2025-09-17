import mysql.connector
import pandas as pd

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

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'


while True:

    j = []
    x = str(input("Enter the name of Player whose profile you want to see : "))
    mycursor.execute(f"SELECT ODI_Matches, Runs, 100s, 50s, Average, Highest, SR, NotOut from batting where name = '{x}'")
    r = mycursor.fetchall()
    for i in r[0]:
        j.append(i)

    print(YELLOW  + f"{x}" + MAGENTA + " STATS" + RESET)
    t = pd.Series(j, index = ['ODI Matches', "Runs", "100s", "50s", "Average", "Highest", "S/R", "Not Out"])
    print(t)

    

