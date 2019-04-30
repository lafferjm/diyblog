from django.shortcuts import render
from django.views import generic
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
    ordering = ['-post_date']
    paginate_by = 5
