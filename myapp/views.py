from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def home(req):
    return render(req,'index.html')

def levelFunc(req):
    #nombres de las celdas
    clicked_id = req.GET.get('id',None)
    if clicked_id=='1':
        #action low
        response = {
            'response' : "https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fscipi0n%2FSysmonxMitre%2Fmain%2Flayer_low.json"
        }
    elif clicked_id=='2':
        response = {
            'response': "https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fscipi0n%2FSysmonxMitre%2Fmain%2Flayer_mid.json"
        }
    elif clicked_id=='3':
        response = {
            'response': "https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fscipi0n%2FSysmonxMitre%2Fmain%2Flayer_high.json"
        }

    else:
        response = {
            'response': 'error'
        }
    return JsonResponse(response)