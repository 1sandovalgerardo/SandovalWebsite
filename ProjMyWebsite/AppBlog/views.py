from django.shortcuts import render
from django.utils import timezone
from .models import PostModel, CommentModel
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # class based version
from django.contrib.auth.decorators import login_required  # decorator version
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
# imports for comments
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


# Create your views here.
# These views are for the blog posts

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = PostModel

    # this function searches the database
    def get_queryset(self):
        return PostModel.objects.filter(published_date__lte=timezone.now())\
                                        .order_by('-published-date')


class PostDetailView(DetailView):
    model = PostModel


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = PostModel


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = PostModel


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = PostModel
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = PostModel

    def get_queryset(self):
        return PostModel.objects.filter(publised_date__isnull=True).order_by('created_date')


# These views are for the comments section of the page.

@login_required
def post_publish(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


# @login_required  uncomment to use this line
def add_comment_to_post(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, 'Comment can not be blank')
            return render(request, 'blog/comment_form.html', {'form': form})

    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(CommentModel, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(CommentMode, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)







