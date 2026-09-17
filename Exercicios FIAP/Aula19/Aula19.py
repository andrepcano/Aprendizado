import requests

def tipo_poke(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url)
    info = r.json()
    id = info['id']
    tipo = []
    for i in range(len(info['types'])):
        tipo.append(info['types'][i]['type']['name'])
    return id, tipo

print(tipo_poke('charizard'))

