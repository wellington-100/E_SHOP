












from django.template import loader
from django.http import HttpResponse


# PUBLIC VIEWS
def indexPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

