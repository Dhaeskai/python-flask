"""import requests

url = 'https://rickandmortyapi.com/api/character/1'

response = requests.get(url)
responsejson = response.json()



while i<11:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i)
    res = requests.get(url)
    res = res.json()
    name = res['name']
    stat = res['status']
    print("El personaje {} tiene status: {}".format(name,stat))
    i = i + 1


url = 'https://rickandmortyapi.com/api/episode/1'
response = requests.get(url)
responsejson = response.json()
char = responsejson['characters']

for i in char:
    url = requests.get(i)
    urljson = url.json()
    name = urljson['name']
    status = urljson['status']
    print(name, "---", status)


i = 1
while i <= 5:
    url = 'https://rickandmortyapi.com/api/episode/{}'.format(i)
    response = requests.get(url)
    responsejson = response.json()
    char = responsejson['characters']
    print("Los personajes del capítulo: {} son:".format(i) )
    i = i + 1

    for j in char:
        url = requests.get(j)
        urljson = url.json()
        name = urljson['name']
        status = urljson['status']
        print(name, "---", status)
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    atletas = {
        'peleador' : 'rocky',
        'boxeo' : 'maradona'
    }
   

    url = 'https://rickandmortyapi.com/api/character/1'
    urlreq = requests.get(url)
    urljson = urlreq.json()
    url2 = 'https://rickandmortyapi.com/api/character/2'
    urlreq2 = requests.get(url2)
    urljson2 = urlreq2.json()
    return render_template('index.html', data = urljson, data2 = urljson2 )

    
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)