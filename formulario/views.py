from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import Texto, UploadedFiles
from .models import Uploader, Denuncia

def index(request):
    if request.method == 'POST':
        form = Texto(request.POST)
        uploader = UploadedFiles(request.FILES)
        files = request.FILES.getlist('aqui')
        guardForm = Denuncia()
        den = open('aqui//denuncia.txt', 'w')
        den.write(str(guardForm.__str__(form)))
        den.close()
        if form.is_valid():
            for f in files:
                file_instance = Uploader(aqui=f)
                file_instance.save()
    else:
        form = Texto()
        uploader = UploadedFiles()

    return render(request, 'index.html', {'form' : form, 'uploader' : uploader})