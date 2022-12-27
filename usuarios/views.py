from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'El usuario ya existe')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'El email ya existe')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				print('usuario creado')

				return redirect('login')

		else:
			messages.info(request, 'Las contraseñas no coinciden')
			return redirect('register')

		return redirect('/')

	else:
		return render(request, 'usuarios/register_form.htm')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'El usuario o la contraseña no son válidos')
			return redirect('login')

	else:
		return render(request, 'usuarios/login_form.htm')

def logout(request):
	auth.logout(request)
	return redirect('/')

def delete(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(User, id=ch)
			obj.delete()
	user=User.objects.all()
	context={
		'usuarios':user,
		}
	return render(request,'usuarios/del_form.html',context)

def change_password(request):
	if request.method == 'POST':
		opassword = request.POST['opassword']
		npassword = request.POST['npassword']
		npassword2 = request.POST['npassword2']
		if (opassword=="" or npassword=="" or npassword2==""):
			messages.info(request,'Password are empty')
			return redirect('change_password')
		u = User.objects.get(id=request.user.id)
		if u.check_password(opassword):
			if npassword==npassword2:
				u.set_password(npassword)
				u.save()
				return redirect('/')
			else:
				messages.info(request,'Password are different...')
				return redirect('change_password')
		else:
			messages.info(request,'Old password are not the same...')
			return redirect('change_password')
		return redirect('/')
	else:
		return render(request,'usuarios/change_password.htm',{})