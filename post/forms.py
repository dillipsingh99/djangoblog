from django import forms
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommentForm(forms.Form):
    comment = forms.CharField(widget=CKEditorUploadingWidget())
    

    
    def __str__(self):
        return {self.comment[:50]}



        