from .models import LostAndFound, Comment
from django import forms

class CommentForm(forms.ModelForm):
    #text = forms.TextInput(label = '댓글')

    class Meta:
        model = Comment
        fields = ['comment_writer', 'comment_text']