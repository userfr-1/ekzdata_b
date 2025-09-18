from django.shortcuts import render, redirect
from .models import Profile, Technology, Project, SocialLink
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    profile = Profile.objects.first()
    technologies = Technology.objects.all()
    projects = Project.objects.all()
    socials = SocialLink.objects.all()


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "index.html", {
        "profile": profile,
        "technologies": technologies,
        "projects": projects,
        "socials": socials,
        "form": form,
    })
