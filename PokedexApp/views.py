

# Create your views here.

from django.shortcuts import render
import urllib.request
import json
from http import HTTPStatus  #maneja error HTTP
from urllib.error import HTTPError

# Create your views here.
def index(request):

    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ', '%20')
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            
            url_pokeapi.add_header('User-Agent', "pikachu")
            
            source = urllib.request.urlopen(url_pokeapi).read()
            # Convirtiendo el JSON a un diccionario
            # 'list_of_data' guardará todos los datos que estamos solicitando
            list_of_data = json.loads(source)
                
            # La variable 'data' guardará todo lo que vamos a renderizar en HTML
            # Las llaves y valores las provee la API de Pokemon

            # Altura de decímetros a metros
            height_obtained = (float(list_of_data['height']) * 0.1)
            height_rounded = round(height_obtained, 2)

            # Peso de hectogramos a kilogramos
            weight_obtained = (float(list_of_data['weight']) * 0.1)
            weight_rounded = round(weight_obtained, 2)

            data = {
                "number": str(list_of_data['id']),
                "name": str(list_of_data['name']).capitalize(),
                "height": str(height_rounded)+ " m",
                "weight": str(weight_rounded)+ " kg",
                "sprite": str(list_of_data['sprites']['front_default']),
                
            }
            #if request.method == True:
               # url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/type/{pokemon}/')
                #url_pokeapi.add_header('User-Agent', "pikachu")
                #source = urllib.request.urlopen(url_pokeapi).read()
                
                #data = {
                    #"number": str(list_of_data['id']),
                    #"name": str(list_of_data['name']).capitalize(),
                    #"damage relations": str(list_of_data[damage_relations]), 
                    #"past_damage_relations": str(list_of_data [past_damage_relations]), }
                
        
            print(data)
        else:
            data = {}

        return render(request, "main/index.html", data)
    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")



