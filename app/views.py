from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, About, Contact

# Create your views here.

def index(request):
	username = request.user
	email = "bha@gma.com"
	posts = Post.objects.all()

	notes = [
			"Read books",
			"Send email",
			"Practice Coding"
	]

	context = {
		"username":username,
		"email":email,
		"notes":notes,
		"posts":posts,
	}
	return render(request,"index.html",context)


def about(request):
	about = About.objects.all()
	context = {'about':about}
	return render(request,"about.html",context)

def contact(request):
	contact = Contact.objects.all()
	context = {'contact':contact}
	return render(request,"contact.html",context)

