# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,


	)
from . forms import UserLoginForm
# Create your views here.




# def login_view(request):
# 	template = 'pos/login.html'
# 	form = LoginForm
# 	if request.method == 'POST':
# 		username = request.POST.get('username', '')
# 		password = request.POST.get('password', '')
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				messages.success(request, "You have logged in!")
# 				return redirect('home')
# 			else:
# 				messages.warning(request, "Your account is disabled!")
# 				return redirect('/login')
# 		else:
# 			messages.warning(request, "The username or password are not valid!")
# 			return redirect('/login')
# 	context = {'form': form}
# 	return render(request, template, context)

# @login_required(redirect_field_name='next', login_url='/login')
# def bar(request):
# 	template = 'pos/bar.html'
# 	drink = OrderItem.objects.filter(product__catgory__gt=1).order_by('-created')
# 	context = {'drink': drink}
# 	return render(request, template, context)







def login_view(request):
	title= "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		if not is_safe_url(url=redirect_to, host=request.get_host()):
			redirect_to = settings.LOGIN_REDIRECT_URL
		# user = authenticate(username=username, password=password)
  #       if user is not None:
  #           if user.is_active:
  #               login(request, user)
  #               state = "You're successfully logged in!"
  #               # return HttpResponseRedirect('/issueapp/1628/')
  #           else:
  #               state = "Your account is not active, please contact the site admin."
  #       else:
  #           state = "Your username and/or password were incorrect."

	# return redirect(self.request.GET.get('next'))
	return render(request,"form.html",{"form":form , "title":title})
	# return render(request,"blog/templates/blog.html")


def register_view(request):
	return render(request,"form.html",{})

def logout_view(request):
	return render(request,"form.html",{})