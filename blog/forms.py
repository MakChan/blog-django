
from django import forms
from .models import Post, Comment


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class NewCommentForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Enter comment here'}
        ),
        max_length=300,
        help_text='The maximum length of the comment is 300.'
    )

    class Meta:
        model = Comment
        fields = ['content']
