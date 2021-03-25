from django.shortcuts import render
from tqdm.auto import tqdm
import os
import pafy
from django.contrib import messages


def yt_download(request):
    if request.method == 'POST':
        a=request.POST.get('link')
        b=request.POST.get('tipo')
        link=str(a)
        type=str(b)
        print("Link: ",link, " tipo: ",type)
        out= pafy.new(link)
        try:
            if type=="mp4":
                messages.info(request, "Espera...")
                down = out.getbestvideo(preftype=type)
                
            else :
                if type=="m4a":
                    messages.info(request, "Espera...")
                    down = out.getbestaudio(preftype=type)
                    
            path=(u"C:\\Users\\Usuario\\Downloads")
            print(path)
            down.download(quiet=True, callback=progreso,  filepath=path)
            messages.success(request, "Listo, revisa tu carpeta de descargas")
        except Exception as e:
            print("Error ", e) 
        return render(request, 'home.html')
    return render(request, 'home.html')

def progreso(total, recvd, ratio, rate, eta):
    print("Total =", total)
    valor=(recvd*100/total)
    porcentaje=int(valor)
    print("Porcentaje despues=",porcentaje)