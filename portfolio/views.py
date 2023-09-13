from django.http import HttpResponse
from django.template import loader

def portfolio(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def about(request):
    # template = loader.get_template('about.html')
    return HttpResponse(loader.get_template('about.html').render())