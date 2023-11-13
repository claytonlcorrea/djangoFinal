from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelecope.org / NASA / James Webb",
            "tag": "Estrelas"
        },
            
        2: {"nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble",
            "tag": "Constelação",
        }, 
        
        3: {"nome": "Galáxia Andromeda",
            "legenda": "nasa.org / NASA / Hubble",
            "tag": "Galáxia",
        }   
    }
    return render(request, 'index.html', {"cards": dados})

def imagem(request):
    return render(request, 'imagem.html')


