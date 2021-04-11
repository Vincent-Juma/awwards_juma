from django import forms
from .models import Project,Rating

class ProjectUploadForm(forms.ModelForm):
    '''
    This class will define the form for users to upload their projects for ratings
    '''
    class Meta:
        model = Project
        fields = ["title","description","link","image"]

class RatingUploadForm(forms.ModelForm):
    '''
    This class will define the form for users to rate the project
    '''
    class Meta:
        model = Rating
        fields = ["design","usability","content"]