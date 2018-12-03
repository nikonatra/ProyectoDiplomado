from django.shortcuts import render
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
from collections import OrderedDict
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.layouts import gridplot
from bokeh.models import FactorRange
from bokeh.models import BoxAnnotation
from bokeh.layouts import column
from bokeh.models import RangeTool
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import Slider, TextInput



# Create your views here.
def login(request):
	return render(request, 'webApp/login.html')

def index(request):
	return render(request, 'webApp/index.html')

def fanalistas(request):
	
	x = np.linspace(0, 4*np.pi, 100)
	y = np.sin(x)

	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

	p1 = figure(title="Legend Example", tools=TOOLS)

	p1.circle(x,   y, legend="sin(x)")
	p1.circle(x, 2*y, legend="2*sin(x)", color="red")
	p1.circle(x, 3*y, legend="3*sin(x)", color="blue")

	p2 = figure(title="Another Legend Example", tools=TOOLS)

	p2.circle(x, y, legend="sin(x)")
	p2.line(x, y, legend="sin(x)")

	p2.line(x, 2*y, legend="2*sin(x)", line_dash=(4, 4), line_color="red", line_width=2)

	p2.square(x, 3*y, legend="3*sin(x)", fill_color=None, line_color="blue")
	p2.line(x, 3*y, legend="3*sin(x)", line_color="blue")

	script_1, div_1 = components(p1)
	script_2, div_2 = components(p2)
	

	return render(request, 'webApp/fanalistas.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fentidades(request):

	fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
	years = ['2015', '2016', '2017']

	data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

	palette = ["#c9d9d3", "#718dbf", "#e84d60"]

	# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
	x = [ (fruit, year) for fruit in fruits for year in years ]
	counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack

	source = ColumnDataSource(data=dict(x=x, counts=counts))

	p = figure(x_range=FactorRange(*x), plot_height=350, title="Fruit Counts by Year",
           toolbar_location=None, tools="")

	p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2))

	p.y_range.start = 0
	p.x_range.range_padding = 0.1
	p.xaxis.major_label_orientation = 1
	p.xgrid.grid_line_color = None

	script_1, div_1 = components(p)

	return render(request, 'webApp/fentidades.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fcomercializadoras(request):

	factors = [
    ("Q1", "jan"), ("Q1", "feb"), ("Q1", "mar"),
    ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
    ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
    ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),

	]	

	p = figure(x_range=FactorRange(*factors), plot_height=350,
           toolbar_location=None, tools="")

	x = [ 10, 12, 16, 9, 10, 8, 12, 13, 14, 14, 12, 16 ]
	p.vbar(x=factors, top=x, width=0.9, alpha=0.5)

	p.line(x=["Q1", "Q2", "Q3", "Q4"], y=[12, 9, 13, 14], color="red", line_width=2)

	p.y_range.start = 0
	p.x_range.range_padding = 0.1
	p.xaxis.major_label_orientation = 1
	p.xgrid.grid_line_color = None

	script_1, div_1 = components(p)

	return render(request, 'webApp/fcomercializadoras.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fprovedores(request):

	x = np.linspace(0, 4*np.pi, 100)
	y = np.sin(x)

	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

	p1 = figure(title="Legend Example", tools=TOOLS)

	p1.circle(x,   y, legend="sin(x)")
	p1.circle(x, 2*y, legend="2*sin(x)", color="orange")
	p1.circle(x, 3*y, legend="3*sin(x)", color="green")

	script_1, div_1 = components(p1)

	return render(request, 'webApp/fprovedores.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})		

def fmodelo(request):
	return render(request, 'webApp/fmodelo.html')

def facerca(request):
	return render(request, 'webApp/facerca.html')
