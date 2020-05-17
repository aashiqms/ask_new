from django import forms


from post_questions.models import Post, Comment, Answer
from django.forms import ModelForm


class QuestionForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'questions']


# widget = {
#    'title': forms.TextInput(attrs={'class': 'textinputclass'}),
# }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


#        widget = {
#           'title': forms.TextInput(attrs={'class': 'textinputclass'}),
#      }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['author', 'text']


#        widget = {
#           'title': forms.TextInput(attrs={'class': 'textinputclass'}),
#      }


form = QuestionForm()
