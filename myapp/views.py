from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm, ipsTextForm
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
    return render(req,'index2.html', {'form': form})
def upload_file(req):
    if req.method == "POST":
        form = UploadFileForm(req.POST, req.FILES)
        if form.is_valid():
            f = req.FILES['file'].file
            ips = req.POST['ips']
            ips_parsed = ips.split(',')
            ##HAY QUE COMPROBAR QUE EL FORMATO DE LAS IPS ES CORRECTO
            exclud = form.cleaned_data.get('mult')
            config = f.read()
            layer_reader(config,exclud,ips_parsed)
            response = HttpResponse(open("myapp/Config_final.xml", 'rb').read())
            response['Content-Type'] = 'text/plain'
            response['Content-Disposition'] = 'attachment; filename=config.xml'
            return response
    return render(req, 'index2.html')