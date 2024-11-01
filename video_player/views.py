from django.shortcuts import render
from .models import Video


def index(request):
    if request.method == "GET":
        da = Video.objects.all()
    return render(request, 'videos.html', {'da': da})
# Create your views here.
