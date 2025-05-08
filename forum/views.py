from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.views.generic import DetailView, UpdateView, DeleteView

@login_required
def forum_view(request):
    messages = Message.objects.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('users:login')

        form = MessageForm(request.POST,  request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect('forum')
    else:
        form = MessageForm()

    return render(request, 'forum/forum.html', {
        'messages': messages,
        'form': form,
    })

class MessageDeleteView(DeleteView):
    model = Message
    success_url = '/forum/'
    template_name = 'news/news_delete.html'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'forum/details_view.html'
    context_object_name = 'message'
