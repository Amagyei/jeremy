from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Upload_data_Form
from .models import chicken_data_upload,chicken


# Create your views here.


def upload_data(request):
    if request.method == 'POST':
        form = Upload_data_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_uploads')  
    else:
        form = Upload_data_Form()
    return render(request, 'home.html', {'form': form})

def list_uploads(request):
    uploads = chicken_data_upload.objects.all()
    return render(request, 'video_list.html', {'uploads': uploads})