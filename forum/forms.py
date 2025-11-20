from django import forms
from .models import Topic, Reply
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title','body']
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
