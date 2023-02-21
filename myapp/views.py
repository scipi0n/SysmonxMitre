from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .layer_read import layer_reader

def home(req):
    form = UploadFileForm()
    req.session['test'] = "0"
    if req.method == "POST":
        form = UploadFileForm(req.POST, req.FILES)
        f = req.FILES['file'].file
        config = f.read()
        layer_reader(config)
        response = HttpResponse(open("myapp/Config_final.xml", 'rb').read())
        response['Content-Type'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename=config.xml'
        return response
        #return render(req, 'index.html', {'response': "ÉXITO, SE HA DESCARGADO EL ARCHIVO DE CONFIGURACIÓN"})
    return render(req,'index2.html', {'form': form})
def upload_file(req):
    if req.method == "POST":
        form = UploadFileForm(req.POST, req.FILES)
        f = req.FILES['file'].file
        config = f.read()
        layer_reader(config)
        response = HttpResponse(open("myapp/Config_final.xml", 'rb').read())
        response['Content-Type'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename=config.xml'
        return response
    return render(req, 'index2.html')