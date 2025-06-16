from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! everything is ok ! Thanks a lot ")

def hello_chadni(request):
    return HttpResponse("Hello, Chadni! everything is ok ! Thanks a lot ")
