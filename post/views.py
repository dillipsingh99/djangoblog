from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from . models import Blog
from . models import Comment
from . forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required

def bloglistview(request):
     dataset = Blog.objects.all()
     context = {
          'dataset' : dataset
     }
     return render(request,'home.html', context)


@login_required(login_url='login')
def blogdetailview(request, _id):
     try:
          data = Blog.objects.get(id=_id)
          print(data)
          print(data.author)
          comments = Comment.objects.filter(blog=data)
          username = request.user
          print(type('username'))

          print(username)
     except Blog.DoesNotExist:
          raise Http404("Data does not exit")
     form = CommentForm(request.POST)
     if form.is_valid():
          text = Comment(comment=form.cleaned_data['comment'], author = username,
               blog=data)
          text.save()
          return redirect(f'/blog/{_id}')
     else:
          form = CommentForm()
     context = {
          'data':data,
          'form':form,
          'comments':comments
     }
     return render(request, 'blog_detail.html', context)


class BlogCreateView(LoginRequiredMixin, CreateView):

     model = Blog
     template_name = 'blog_new.html'
     fields = ('title','description', 'body', 'img',)
     LOGIN_URL = 'login'
     success_url = reverse_lazy('home')
     
     def form_valid(self, form): # new
          form.instance.author = self.request.user
          return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
     model = Blog
     template_name = 'blog_edit.html'
     fields = '__all__'
     LOGIN_URL = 'login'
     success_url = reverse_lazy('home')

     def dispatch(self, request, *args, **kwargs):
          obj = self.get_object()
          if obj.author != self.request.user:
               raise PermissionDenied
          return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
     model = Blog
     template_name = 'blog_delete.html'
     success_url = reverse_lazy('home')
     LOGIN_URL = 'login'

     def dispatch(self, request, *args, **kwargs):
          obj = self.get_object()
          if obj.author != self.request.user:
               raise PermissionDenied
          return super().dispatch(request, *args, **kwargs)


