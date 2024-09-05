from django import forms
from product_module import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        """
        This has been overridden to customise the textarea form widget.
        """
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs['class'] = 'no-resize'