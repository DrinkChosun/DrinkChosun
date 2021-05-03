from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the Title',
                'maxlength': 20,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the Content',
                'rows': 10,
                'cols': 30,
            }
        ),
        error_messages={
            'required': '내용을 입력해주세요.',
        }
    )

    class Meta:
        model = Article
        exclude= ['user',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude= ['user',]