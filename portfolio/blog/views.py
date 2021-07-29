from django.shortcuts import render
from .models import Blog

# Create your views here.
def main(request):
    return render(request, "main.html")


def overseas(request):
    return render(request, "overseas.html")

def activity(request):
    return render(request, "activity.html")

def school(request):
    return render(request, "school.html")

def contest(request):
    return render(request, "contest.html")