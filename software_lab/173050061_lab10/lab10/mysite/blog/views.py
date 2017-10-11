from django.shortcuts import render

# Create your views here.
@login_required
def index(request):
    return HttpResponse('OK, Google!')