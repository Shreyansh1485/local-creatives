from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Reply
from .forms import TopicForm, ReplyForm
def topic_list(request):
    topics = Topic.objects.order_by('-created_at')[:50]
    return render(request, 'forum/topic_list.html', {'topics': topics})
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    reply_form = ReplyForm()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'reply_form': reply_form})
@login_required
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'forum/topic_form.html', {'form': form})
@login_required
def reply_create(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.topic = topic
            reply.save()
    return redirect('topic_detail', pk=pk)
