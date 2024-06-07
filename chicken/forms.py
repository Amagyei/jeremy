from django import forms
from .models import chicken_data_upload

class Upload_data_Form(forms.ModelForm):
    class Meta:
        model = chicken_data_upload
        fields = ['title', 'video_file']
        widgets = {
            'video_file': forms.FileInput(attrs={'accept': 'video/*'}),
        }
        