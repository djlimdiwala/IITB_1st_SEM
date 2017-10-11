from django.shortcuts import render


def index(request):
	return render (request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['Mail me if you want to contact: ','dhaval.limdiwala@gmail.com']})

