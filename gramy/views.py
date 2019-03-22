from django.shortcuts import render
from django.http  import HttpResponse,HttpResponse
from .forms import ProfileForm
from .models import Image,Profile,User

def home(request):
    
    return render(request,'index.html')

def myProfile(request):
    profiles = Profile.objects.all()
    return render(request,'my_profile.html',{"profiles":profiles})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

    else:
        form = CommentsForm()
    return render(request, 'comments.html', {"form": form})


