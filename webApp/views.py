from django.shortcuts import render

from bokeh.plotting import figure
from bokeh.embed import components


# Create your views here.
def login(request):
	return render(request, 'webApp/login.html')

def index(request):
	return render(request, 'webApp/index.html')

def fanalistas(request):
	x=[i for i in range(2016,2020)]
	y=[6,10,17,21]

	title_plot_1 = "Miembros del Semillero"
	x_axis_1 = "Años"
	y_axis_1 = "Miembros"
	plot_1_width = 500
	plot_1_height = 350

	plot_1 = figure(title= title_plot_1, x_axis_label= x_axis_1, y_axis_label= y_axis_1, plot_width= plot_1_width, plot_height= plot_1_height)
	
	plot_1.circle(x, y)
	plot_1.line(x, y, legend='', line_width = 2)

	script_1, div_1 = components(plot_1)

	return render(request, 'webApp/fanalistas.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fentidades(request):
	return render(request, 'webApp/fentidades.html')

def fcomercializadoras(request):
	return render(request, 'webApp/fcomercializadoras.html')

def fprovedores(request):
	return render(request, 'webApp/fprovedores.html')		

def resultado(request):
	return render(request, 'webApp/resultado.html')
