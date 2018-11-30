from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, 'webApp/login.html')

def index(request):
	return render(request, 'webApp/index.html')

def fanalistas(request):
	return render(request, 'webApp/fanalistas.html')

def fentidades(request):
	return render(request, 'webApp/fentidades.html')	

def resultado(request):
	return render(request, 'webApp/resultado.html')
