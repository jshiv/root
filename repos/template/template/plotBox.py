import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def scatter_plot(x, y, data = None, hue = None, title = 'Scatter Plot'
				 ,xlabel = 'X-Values', ylabel = 'Y-Values', alpha=0.3, figsize=(9.5*1.5,6*1.5), saveAs = None
				 ,vlines = None, hlines = None
				 ,xlim = (None,None), ylim = (None,None), legend = True,
				 model = None,
				 plotly = False):
	'''
	scatter_plot uses matplotlib.pyplot.scatter in a seaborn like functional paridigm

	Parameters
	----------
	x, y : strings
		Column names in ``data``.
	data : DataFrame
		Long-form (tidy) dataframe with variables in columns and observations
		in rows.
	hue, col, row : strings, optional
		Variable names to facet on the hue, col, or row dimensions (see
		:class:`FacetGrid` docs for more information).
	title, xlabel, ylabel : strings
		labels of scatter plot.
	alpha : float
		opacity of scatter points.
	figsize : touple, (width, height)
	saveAs : optional
		filename to save figure as
	vlines : list
		list of x points to make vertical lines in the plot
	xlim : touple (xmin, xmax)
		horizontal boundries of the figure
	ylim : tuple (ymin, ymax)
		vertical boundries of the plot
	legend : boolean, optional
		Draw a legend for the data when using a `hue` variable.


	Examples
	--------

	.. plot:: 
		>>>import plotBox
		>>>f = 1000
		>>>hue = ['one' for i in range(50*f)] + ['two' for i in range(30*f)] + ['three' for i in range(20*f)]
		>>>plotBox.scatter_plot(x = np.random.randn(100*f), y = np.random.randn(100*f), hue = hue, vlines = 0, alpha= .1, hlines = 0)
	
	.. todo::

		Add arguments:

		* dropna : boolean, optional
		Drop missing values from the data before plotting.

		* add regression : 
		f, popt, pcov = rp.statBox.regression_model(x,y, model)
		plt.plot(np.linspace(0,max(x)+100,50), f(np.linspace(0,max(x)+100,50), *popt), 'r-', label="Fitted Curve")


	Notes
	-----
	This function can be used in 2 different ways:

		* Using the arguments to generate titles, legends, etc... and then save/display the plot 

		* Incorporate the plot in a script and overriding the plotting features this way:

			>>> import matplotlib.pyplot as plt 
			>>>
			>>> f = 1000
			>>> hue = ['one' for i in range(50*f)] + ['two' for i in range(30*f)] + ['three' for i in range(20*f)]
			>>> plotBox.scatter_plot(x = np.random.randn(100*f), y = np.random.randn(100*f), hue = hue, vlines = 0, alpha= .1, hlines = 0)
			>>> plt.title('My title')
			>>> plt.xlabel('X label I want')
			>>>
			>>> # To change the figure size :
			>>> fig = plt.gcf()	# get the figure object
			>>> fig.set_size_inches(5,10)
			>>>
			>>> plt.show()

	'''

	if isinstance(x, basestring):
		if xlabel == 'X-Values':
			xlabel = x
		x = list(data[x])
	else:
		x = list(x)

	if isinstance(y, basestring):
		if ylabel == 'Y-Values':
			ylabel = y
		y = list(data[y])
	else:
		y = list(y)


	if hue is None:
		hue = ['Data' for i in range(len(x))]
	else:
		if isinstance(hue, basestring):
			hue = list(data[hue])
		else:
			hue = list(hue)   

	hue_count_set = []
	for h in set(hue):
		hue_count_set.append((hue.count(h),h))

	hue_labels = [t[1] for t in sorted(hue_count_set, reverse = True)]


	if len(hue_labels) > 7:
		color_list = list(np.random.rand(len(hue_labels)))
	else:
		color_list = ['c','r','g','b','m','y','k'] 
	inc = 0
	fig = plt.figure(figsize = figsize)
	for h in hue_labels:
		idx = list(np.where(np.array(hue) == h)[0])
		x_idx = [x[i] for i in idx]
		y_idx = [y[i] for i in idx]
		plt.scatter(x_idx, y_idx, c = color_list[inc], alpha=alpha)
		inc += 1

	if legend:
		plt.legend(hue_labels) 
	plt.title(title, size = 16)
	plt.xlabel(xlabel, fontsize = 14)
	plt.ylabel(ylabel, fontsize = 14)

	if ylim[0] is None:
		y_min = plt.ylim()[0]
	else:
		y_min = ylim[0]

	if ylim[1] is None:
		y_max = plt.ylim()[1]
	else:
		y_max = ylim[1]
	plt.ylim(y_min, y_max)


	if xlim[0] is None:
		x_min = plt.xlim()[0]
	else:
		x_min = xlim[0]

	if xlim[1] is None:
		x_max = plt.xlim()[1]
	else:
		x_max = xlim[1]
	plt.xlim(x_min, x_max)


	if vlines is not None:
		plt.vlines(vlines, y_min, y_max)
	if hlines is not None:
		plt.hlines(hlines, x_min, x_max)

	# if plotly:
	# 	plot_url = py.iplot_mpl(fig, filename=title, fileopt='overwrite')

	if saveAs is not None:
		plt.savefig(saveAs)
		