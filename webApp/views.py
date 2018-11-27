from django.shortcuts import render

# Create your views here.
def formulario(request):
	return render(request, 'webApp/formulario.html')

def resultado(request):
	return render(request, 'webApp/resultado.html')