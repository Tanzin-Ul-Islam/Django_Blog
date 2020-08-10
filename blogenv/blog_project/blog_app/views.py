from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, View, DetailView, TemplateView, DeleteView
from blog_app.models import *
from blog_app.forms import *
import uuid

# Create your views here.
class myblogs(LoginRequiredMixin, TemplateView):
    model=blog
    template_name = 'blog_app/my_blog.html'

class editblog(LoginRequiredMixin,UpdateView):
    model = blog
    template_name = 'blog_app/edit_blog.html'
    fields = ['blog_title', 'blog_content', 'blog_image']
    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_app:blog_details', kwargs={'slug':self.object.slug})


class createblog(LoginRequiredMixin, CreateView):
    model=blog
    template_name = 'blog_app/create_blog.html'
    fields = ['blog_title','blog_content','blog_image']


    def form_valid(self, form, ):
        blog_obj=form.save(commit=False)
        blog_obj.author=self.request.user
        title=blog_obj.blog_title
        blog_obj.slug=title.replace(" ", "-")+" "+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class bloglist(ListView):
    context_object_name = 'blogs'
    model = blog
    template_name = 'blog_app/blog_list.html'

@login_required
def blog_details(request, slug):
    diction={}
    blogs=blog.objects.get(slug=slug)
    form=commentform()
    users=request.user
    already_liked = like.objects.filter(user=users, blog=blogs)

    if already_liked:
        liked=True
    else:
        liked=False

    diction.update({'liked':liked})

    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.blog=blogs
            comment.save()
            return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':slug}))
    diction.update({'blog':blogs})
    diction.update({'form':form})
    return render(request, 'blog_app/blog_details.html', context=diction)

@login_required
def liked(request, pk):
    blogs = blog.objects.get(pk=pk)
    user = request.user
    alredy_liked = like.objects.filter(user=user, blog=blogs)
    if not alredy_liked:
        like_post = like(user=user, blog=blogs)
        like_post.save()
    return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':blogs.slug}))

@login_required
def disliked(request, pk):
    blogs = blog.objects.get(pk=pk)
    users = request.user
    alredy_liked = like.objects.filter(user=users, blog=blogs)
    alredy_liked.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':blogs.slug}))

