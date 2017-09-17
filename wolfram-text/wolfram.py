import json
import requests
import my_keys

def format_answer(answer):
    if len(answer) == 0: raise Exception('Empty response')
    if len(answer) >= 1600: return answer[0:1600]
    return answer

def get_answer(question):
    print('getting answer...')

    try:
        #replace my_keys.get_key('wolfram') with your wolfram api key
        request = 'http://api.wolframalpha.com/v2/query?appid={}&input={}&format=plaintext&output=JSON'.format(my_keys.get_key('wolfram'), question)
        response = requests.get(request)
        print('status code: {}'.format(response.status_code))
        r = json.loads(response.text)
        return format_answer(r['queryresult']['pods'][1]['subpods'][0]['plaintext'])
    except:
        return 'There was an error in getting the answer - but 42 is a good guess.'
