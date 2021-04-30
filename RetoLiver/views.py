from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proceso(request):
    telefono = request.POST['phone']
    correo = request.POST['email']
    card = request.POST['si']
    card2 = request.POST['no']
    return render(request, 'proceso.html', {'Phone': telefono, 'Email': correo, 'Check': card, 'Check2': card2})