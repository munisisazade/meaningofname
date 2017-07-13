from django.shortcuts import render
from django.views.generic import TemplateView
import requests as r

class BaseIndexView(TemplateView):
	template_name = 'index.html'


	def post(self,request):
		query = request.POST.get('name')
		result = r.get('http://data.e-gov.az/api/v1/IEGOVService.svc/GetMeaningOfName/'+query)
		data = result.json()
		return render(request, 'index.html', self.get_context_data(query,data))


	def get_context_data(self,query=None,data=None):
		context = {}
		if self.request.method == 'POST':
			context['kes'] = query
			context['data'] = data
		return context
