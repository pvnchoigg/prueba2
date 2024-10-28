from django.shortcuts import render,redirect
from app.models import tatuadores
from app.forms import tatuadorForm

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def listaTatuador(request):
    listas=tatuadores.objects.all()
    data={'listas':listas}
    return render(request,'app/listaTatuador.html',data)

def agregarTatuador(request):
    form=tatuadorForm()
    if request.method=='POST':
        form=tatuadorForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'app/agregarTatuador.html',data)

def actualizarTatuador(request,id):
    lista=tatuadores.objects.get(id=id)
    form=tatuadorForm(instance=lista)
    if request.method=='POST':
        form=tatuadorForm(request.POST,instance=lista)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'app/agregarTatuador.html',data)

def eliminarTatuador(reques,id):
    borrar=tatuadores.objects.get(id=id)
    borrar.delete()
    return redirect(index)