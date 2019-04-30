from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class BlogAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=2000, help_text="Enter your blog text here.")
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class BlogComment(models.Model):
    comment = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        max_title_length = 75
        if len(self.comment) > max_title_length:
            title_string = self.comment[:max_title_length] + '...'
        else:
            title_string = self.comment
        
        return title_string
