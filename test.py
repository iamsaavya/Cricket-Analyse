import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/6635"

headers = {
	"x-rapidapi-key": "5e8f37c067mshbe176f742f462bep16e50djsn292e2f836c59",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())