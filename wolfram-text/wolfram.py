import requests

def get_answer(question):
    response = requests.get('https://api.wolframalpha.com/v2/query?input={}&format=plaintext&output=JSON&appid=DEMO'.format(question)).json()
    print(response)
    print(type(response))
    return '42'