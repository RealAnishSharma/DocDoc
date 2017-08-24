from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = [
            "name",
            "image",
            "Specialization",
            "Degree",
            "University",
            "D_O_B",
            "Experience",
            "Hospital",
            "No_of_Clinics",
            "remarks",
            "draft",
            "publish",
            ]
