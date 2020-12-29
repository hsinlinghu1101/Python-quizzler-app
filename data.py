import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)

question_data = [question for question in response.json()["results"]]

