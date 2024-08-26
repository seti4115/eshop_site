from django import forms
from user_module import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ['comment']