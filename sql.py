import mysql.connector
import requests

try:
    mydb = mysql.connector.connect(
        host="localhost",  # Or the IP address of your MySQL server
        user="root",
        password="9977277199aaa",
        database="cricket"  # The name of your existing database
    )
    print("Connection established successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")


mycursor = mydb.cursor()


headers = {
	"x-rapidapi-key": "be716dcb31msh21f3a4208e7d29cp1366b0jsn6a4d2602acd2",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

t = [2, 3, 4, 9, 11, 13]
val = []

tdic = {2 : 'India', 3: 'Pakistan', 4 : 'Australia', 9 : 'England', 11 : 'South Africa', 13 : 'New Zealand'}

for x in t:
    url = f"https://cricbuzz-cricket.p.rapidapi.com/teams/v1/{x}/players"
    response = requests.get(url, headers=headers)
    res = response.json()

    
    for i in range(1, 27):

        try:
            id = res['player'][i]['id']
            name = res['player'][i]['name']
            battingStyle = res['player'][i]['battingStyle']
            intlTeam = tdic[x]
            faceImageId = res['player'][i]['imageId']

            val.append((id, name, battingStyle, intlTeam, faceImageId))
        except(KeyError):
            pass


        #print(id, name, battingStyle)
sql = "INSERT INTO players (id, name, type, intlTeam, faceImageId) VALUES (%s, %s, %s, %s, %s)"



mycursor.executemany(sql, val)

mydb.commit()



mycursor.execute("SELECT * FROM players")
myresult = mycursor.fetchall()



for x in myresult:
    print(x)


