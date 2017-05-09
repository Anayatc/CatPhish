from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    template = loader.get_template('CyberPhish/URL_Expander/templates/index.html')
    return HttpResponse(template.render())
