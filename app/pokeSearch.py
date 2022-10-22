import requests as r
def catchemall(pokemon):
    
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = r.get(url)
    

    if response.ok:
        data = response.json()
        pokedex = {}
        pokedex= {
            'name': data['name'],
            'ability': data['abilities'][0]['ability']['name'],
            'base_hp': data['stats'][0]['base_stat'],
            'base_att': data['stats'][1]['base_stat'],
            'base_def': data['stats'][2]['base_stat'],
            'sprite': data['sprites']['front_default']
        }
        
        return pokedex
    return f"Please check your spelling, as '{pokemon}' is not found in the Pokedex.\n\nIf you are searching for Pokemon 122 Mr. Mime, please change your input to 'mr-mime', or simply enter [122]."