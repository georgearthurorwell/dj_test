from django.http import HttpResponse
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def response(request, *args, **kwargs):                                             
    return HttpResponse('1')
