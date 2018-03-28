from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):

    # message = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'Content'}
    #     ),
    #     max_length=2000,
    #     help_text='The max length of the text is 2000.'
    # )

    class Meta:
        model = Post
        fields = ['title', 'content']
