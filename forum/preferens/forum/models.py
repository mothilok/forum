
from django.db import models

class Posts (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256)
    text_post = models.TextField()
    votes = models.IntegerField(default=0)
    data_published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        if len(self.title) > 20:
            elipsis = '...'
        else:
            elipsis = ''
        return self.title[:20] + elipsis

class Array_Like(models.Model):
    id_post = models.IntegerField()
    id_user = models.IntegerField()
