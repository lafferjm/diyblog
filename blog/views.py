from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from blog.models import BlogAuthor, BlogComment, BlogPost


def index(request):
    num_authors = BlogAuthor.objects.all().count()
    num_comments = BlogComment.objects.all().count()
    num_posts = BlogPost.objects.all().count()

    context = {
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_posts': num_posts
    }

    return render(request, 'blog/index.html', context=context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5


class BlogPostDetailView(generic.DetailView):
    model = BlogPost


class BlogAuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5


class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['comment',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(BlogPost, pk=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk']})
