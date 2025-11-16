import requests
import json
import xml.etree.ElementTree as ET

arr_diz_pokemon = []
unique_ability = []

class Pokemone():
  def __init__(self,diz):
      self.nome = diz["nome"]
      self.altezza = diz["altezza"]
      self.peso = diz["peso"]
      self.types = diz["types"]
      self.ability = diz["ability"]


def __dizionarioPokemon__(nome,altezza,peso,types,ability):
    x = len(ability)
    ability_arr_temp = []
    
    i = 0
    while i != x:
        
        diz_temp = {
            "ability_name" : ability[i]["ability"]["name"],
            "ability_is_hidden" : ability[i]["is_hidden"]
        }
        
        if diz_temp["ability_is_hidden"] == True and diz_temp["ability_is_hidden"] not in unique_ability:
            unique_ability.append(diz_temp["ability_is_hidden"]) 
            
        ability_arr_temp.append(diz_temp)
        i+=1
    
    diz = {
        "nome" : nome,
        "altezza" : altezza,
        "peso" : peso,
        "types" : types,
        "ability" : ability_arr_temp
    }
    arr_diz_pokemon.append(diz)
    

def __fileJson__():
    with open("dizionario_json_api.json", "w") as f:
        json.dump(arr_diz_pokemon,f,indent = 4)
        
r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20")
pokemon = r.json()    
for  x in range(0,20) :
   richiestaSpecifica = requests.get(pokemon["results"][x]["url"])
   pokeApi = richiestaSpecifica.json()
   __dizionarioPokemon__(pokeApi["name"],pokeApi["height"],pokeApi["weight"],pokeApi["types"],pokeApi["abilities"])
   
__fileJson__()

arr_oggetti_pokemon = []
arr_oggetti_pokemon.append(Pokemone(arr_diz_pokemon[0]))
maxWeight = arr_oggetti_pokemon[0].peso
maxAlto = arr_oggetti_pokemon[0].altezza
pokemonPesante = arr_oggetti_pokemon[0]
pokemonAltissimo =  arr_oggetti_pokemon[0]
for i in range(1, 19):
    arr_oggetti_pokemon.append(Pokemone(arr_diz_pokemon[i]))
    if maxWeight < arr_oggetti_pokemon[i].peso:
        maxWeight = arr_oggetti_pokemon[i].peso
        pokemonPesante = arr_oggetti_pokemon[i]
    if maxAlto < arr_oggetti_pokemon[i].altezza:
        maxAlto = arr_oggetti_pokemon[i].altezza
        pokemonAltissimo = arr_oggetti_pokemon[i]
   
    
with open("dizionario_json_api.json", "r") as f:
    pokemon_data = json.load(f)
    
# Creiamo il nodo radice
root = ET.Element("pokemon_list")

for poke in pokemon_data:
    # Nodo per ogni Pokémon
    poke_elem = ET.SubElement(root, "pokemon")
    
    # Aggiungi attributi di base
    nome_elem = ET.SubElement(poke_elem, "nome")
    nome_elem.text = str(poke["nome"])
    
    altezza_elem = ET.SubElement(poke_elem, "altezza")
    altezza_elem.text = str(poke["altezza"])
    
    peso_elem = ET.SubElement(poke_elem, "peso")
    peso_elem.text = str(poke["peso"])
    
    # Types (lista)
    types_elem = ET.SubElement(poke_elem, "types")
    for t in poke["types"]:
        type_elem = ET.SubElement(types_elem, "type")
        type_elem.text = t["type"]["name"]
    
    # Abilities (lista di dizionari)
    abilities_elem = ET.SubElement(poke_elem, "abilities")
    for ab in poke["ability"]:
        ab_elem = ET.SubElement(abilities_elem, "ability")
        name_elem = ET.SubElement(ab_elem, "ability_name")
        name_elem.text = ab["ability_name"]
        hidden_elem = ET.SubElement(ab_elem, "ability_is_hidden")
        hidden_elem.text = str(ab["ability_is_hidden"])

tree = ET.ElementTree(root)
tree.write("pokemon_data.xml", encoding="utf-8", xml_declaration=True)

    
with open("dizionario_json_api.json" , "a") as f:
    f.write("WINNER FOR MAXWEIGHT\n{\n\tnome:" + pokemonPesante.nome + "\n\tpeso:" + str(pokemonPesante.peso) + "\n}"  + "\nWINNER FOR MAXHEIGHT\n{\n\tpokemon:" + pokemonAltissimo.nome + "\n\taltezza:" + str(pokemonAltissimo.altezza) + "\nABILITA' UNICHE TROVATE\n" + str(unique_ability))
 