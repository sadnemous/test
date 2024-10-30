import requests

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    url = 'http://api.icndb.com/jokes/random/3'
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    if response.status_code == 200:
        #print (response.json())
        setup = response.json()['setup']
        punchline = response.json()['punchline']
        joke = f"Setup: {setup}\nAns  : {punchline}"
        #joke = f"{setup}{punchline}"
    else:
        joke ='No jokes'

    return joke

if __name__ == '__main__':
    #main()
    print(get_joke())
