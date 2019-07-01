from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.


class PostModel(models.Model):
    author = models.ForeignKey('auth.User')
# if multiple authors, code would be different.
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)  # tied to line 32

    def get_absolute_url(self):
        # this answers, after a post what page do i show.
        return reverse('blog:postmodel_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    post = models.ForeignKey('AppBlog.PostModel', related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:postmodel_list')

    def __str__(self):
        return self.text
