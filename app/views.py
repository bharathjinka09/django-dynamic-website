from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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


