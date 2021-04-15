from django import forms
from blog.models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(max_length=2)

        # print('1')
        # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
        # print(username)
        # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
