import mysql.connector
import requests

try:
    mydb = mysql.connector.connect(
        host="localhost",  # Or the IP address of your MySQL server
        user="root",
        #password="",
        database="cricket"  # The name of your existing database
    )
    print("Connection established successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")


mycursor = mydb.cursor()


headers = {
	"x-rapidapi-key": "200ca61bb8msh0f7b505d625d0a2p1dd89ejsn5340650fd024",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}


val=[]
name = []

mycursor.execute("select id, name from players")
result = mycursor.fetchall()

for i in result:
    val.append(i[0])
    name.append(i[1])

value0 = []




for i in range(len(val)):

    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{val[i]}/batting"
    response = requests.get(url, headers=headers)
    res = response.json()
    y = res['values']
    
    id = val[i]
    name1 = name[i]
    matches = y[0]['values'][2]
    runs = y[2]['values'][2]
    hundreds = y[12]['values'][2]
    fifties = y[11]['values'][2]
    highest = y[4]['values'][2]
    average = y[5]['values'][2]
    sr = y[6]['values'][2]
    notOut = y[7]['values'][2]

    t = (id, name1, matches, runs, hundreds, fifties, highest, average, sr, notOut)

    value0.append(t)

sql= "INSERT INTO batting (id, name, ODI_Matches, Runs, 100s, 50s, Highest, Average, SR, NotOut) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

mycursor.executemany(sql, value0)
resso = mycursor.fetchall()

mydb.commit()

