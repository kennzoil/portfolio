from django.http import HttpResponse
from django.template import loader

def portfolio(request):
    template = loader.get_template('homepage2.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def music(request):
    template = loader.get_template('music.html')
    return HttpResponse(template.render())