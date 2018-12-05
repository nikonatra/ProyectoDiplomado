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
from bokeh.models import LinearAxis, Range1d 



# Create your views here.
def login(request):
	return render(request, 'webApp/login.html')

def index(request):
	return render(request, 'webApp/index.html')

def fanalistas(request):

	x = [2013,2014,2015,2015,2016,2017]
	
	y0 = [12.07,11.79,10.21,10.17,9.42,9.24,9.88,9.27,8.98,7.79,8.48,8.44,11.1,10.68,9.73,8.97,8.8,	9.19,9.29,8.9,8.35,7.86,7.71,8.72,
	10.79,9.86,8.86,9.5,8.93,8.25,8.84,9.09,8.98,8.19,7.27,8.59,11.91,10,10.14,9.02,8.85,8.88,9.85,8.99,8.51,8.29,7.51,8.74,11.73,10.5,
	9.7,8.91,9.42,8.72,9.68,9.1,9.22,8.56,8.37,8.63]

	y1 = [2131367,2034579,2190844,2184329,2346644,2351796,2463234,2372257,2375481,2354589,2456844,3120568,2267723,2186724,2553342,
	2414367,2558135,2516423,2645617,2517749,2729554,2520881,2676284,3539703,2489289,2438910,2914437,2614598,2748008,2996526,2938535,
	2915096,2965183,2879323,3274805,3824719,2809585,3029092,3083398,3007722,3315780,3422792,3115245,3390656,3209154,3299334,3730568,
	4104828,3298849,3039975,3592843,3061390,3587096,3555136,3581943,3510051,3376478,3565983,4031612,4203373]

	y2 = [374324,288371,341090,366135,386171,408929,471752,410753,410925,470336,417885,466017,486508,377445,428447,478639,482132,
	499785,581328,495173,548721,584363,548706,612896,533847,426566,501652,495787,526466,639209,673945,525293,492382,541691,579412,
	577851,531181,496031,579340,530663,642650,699016,697802,672735,626969,704244,711803,641404,697882,569497,614508,673891,746115,
	775875,792714,703444,655691,770021,788790,692694]


	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"


	p1 = figure(title="GASTOS TARJETA DE CREDITO RESPECTO A LA TASA DE DESEMPLEO", tools=TOOLS, y_range=(0, 4500000))



	p1.extra_y_ranges = {"tasa": Range1d(start=4, end=13)}
	p1.add_layout(LinearAxis(y_range_name="tasa"), 'right') 

	p1.line(x,   y0, legend="Tasa de Desempleo", color="blue", y_range_name="tasa")
	p1.line(x,   y1, legend="Compras Nacionales", color="red", )
	p1.line(x,   y2, legend="Compras Internacionales", color="green")
	


	script_1, div_1 = components(p1)
	

	return render(request, 'webApp/fanalistas.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fentidades(request):

	x = [2013,2014,2015,2015,2016,2017]
	
	y0 = [12.07,11.79,10.21,10.17,9.42,9.24,9.88,9.27,8.98,7.79,8.48,8.44,11.1,10.68,9.73,8.97,8.8,	9.19,9.29,8.9,8.35,7.86,7.71,8.72,
	10.79,9.86,8.86,9.5,8.93,8.25,8.84,9.09,8.98,8.19,7.27,8.59,11.91,10,10.14,9.02,8.85,8.88,9.85,8.99,8.51,8.29,7.51,8.74,11.73,10.5,
	9.7,8.91,9.42,8.72,9.68,9.1,9.22,8.56,8.37,8.63]

	y1 = [106202,111249,100792,107981,115534,107981,121988,122533,117837,136559,122175,129870,130812,110020,119586,126681,130368,104981,
	125264,136889,131282,136107,136107,218702,124359,117645,130302,59285,129375,128997,155089,145190,158096,144681,142526,175350,150570,
	159463,149738,163617,174057,156655,182359,188390,197272,155425,172818,221666,215107,174256,193408,192844,230329,184478,213883,200343,
	216996,200350,187177,183631]

	
	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"


	p1 = figure(title="TARJETAS DE CREDITO CANCELADAS RESPECTO A TASA DE DESEMPLEO", tools=TOOLS, y_range=(10000, 250000))

	p1.extra_y_ranges = {"tasa": Range1d(start=4, end=13)}
	p1.add_layout(LinearAxis(y_range_name="tasa"), 'right')
	 


	p1.line(x,   y0, legend="Tasa de Desempleo", color="blue", y_range_name="tasa")
	p1.line(x,   y1, legend="Tarjetas de Credito Canceladas", color="red", )

	script_1, div_1 = components(p1)


	return render(request, 'webApp/fentidades.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fcomercializadoras(request):

	x = [2013,2014,2015,2015,2016,2017]
	
	y0 = [12.07,11.79,10.21,10.17,9.42,9.24,9.88,9.27,8.98,7.79,8.48,8.44,11.1,10.68,9.73,8.97,8.8,	9.19,9.29,8.9,8.35,7.86,7.71,8.72,
	10.79,9.86,8.86,9.5,8.93,8.25,8.84,9.09,8.98,8.19,7.27,8.59,11.91,10,10.14,9.02,8.85,8.88,9.85,8.99,8.51,8.29,7.51,8.74,11.73,10.5,
	9.7,8.91,9.42,8.72,9.68,9.1,9.22,8.56,8.37,8.63]

	y1 = [23834,24210,23928,22985,22698,22985,22913,22990,23079,24056,68674,10513,24322,24371,21135,23466,22360,23171,23288,26068,26562,26935,
	26935,27006,16861,16788,27470,27658,27983,28319,28508,28439,28674,29067,29119,29314,29102,29527,29868,29900,30205,31016,31168,31341,31211,
	31296,31262,32314,31573,31894,32553,32596,32805,33168,33812,34427,34777,35138,35459,35824]

	
	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"      


	p1 = figure(title="CUPO DISPONIBLE RESPECTO A TASA DE DESEMPLEO", tools=TOOLS, y_range=(20000, 36000))

	p1.extra_y_ranges = {"tasa": Range1d(start=4, end=13)}
	p1.add_layout(LinearAxis(y_range_name="tasa"), 'right')
	 


	p1.line(x,   y0, legend="Tasa de Desempleo", color="blue", y_range_name="tasa")
	p1.line(x,   y1, legend="Cupo Disponible", color="red", )

	script_1, div_1 = components(p1)

	return render(request, 'webApp/fcomercializadoras.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})

def fprovedores(request):

	x = [2013,2014,2015,2015,2016,2017]
	
	y0 = [56.16,56.2,56.47,57,58.73,57.84,57.81,58.59,58.01,60.92,58.84,59.06,56.56,56.29,56.72,58.12,58.32,58.35,57.64,58.97,59.16,61.27,
	60.33,58.88,56.94,57.39,58.23,59.27,58.81,59.1,58.35,58.86,58.71,61.41,60.88,59.52,56.86,57.93,56.88,58.76,58.22,58.82,57.3,58.79,58.71,
	60.77,60.35,58.98,56.34,57.25,57.4,59.26,58.14,59.48,57.52,58.61,58.24,59.95,59.35,58.7]

	y1 = [23834,24210,23928,22985,22698,22985,22913,22990,23079,24056,68674,10513,24322,24371,21135,23466,22360,23171,23288,26068,26562,26935,
	26935,27006,16861,16788,27470,27658,27983,28319,28508,28439,28674,29067,29119,29314,29102,29527,29868,29900,30205,31016,31168,31341,31211,
	31296,31262,32314,31573,31894,32553,32596,32805,33168,33812,34427,34777,35138,35459,35824]

	
	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"      


	p1 = figure(title="CUPO DISPONOBLE RESPECTO A TASA DE EMPLEO", tools=TOOLS, y_range=(20000, 36000))

	p1.extra_y_ranges = {"tasa": Range1d(start=40, end=70)}
	p1.add_layout(LinearAxis(y_range_name="tasa"), 'right')
	 


	p1.line(x,   y0, legend="Tasa de Empleo", color="blue", y_range_name="tasa")
	p1.line(x,   y1, legend="Cupo Disponible", color="red", )

	script_1, div_1 = components(p1)


	return render(request, 'webApp/fprovedores.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1})	

def fmodelo(request):
	return render(request, 'webApp/fmodelo.html')

def facerca(request):
	return render(request, 'webApp/facerca.html')
