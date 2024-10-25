
from django.db import models

class Posts (models.Model):
    title = models.CharField(max_length=256)
    text_post = models.TextField()
    #models.ImageField(blank=True, upload_to='photos_forum') #/%Y/%m
    votes = models.IntegerField(default=0)
    data_published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        if len(self.title) > 20:
            elipsis = '...'
        else:
            elipsis = ''
        return self.title[:20] + elipsis

class Whitelist(models.Model):
    files_format = models.CharField(max_length=10)

    def __str__(self):
        return self.files_format

class Pars_files(models.Model):
    key_posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    file = models.FileField(blank=True, upload_to='photos_forum')
    format = models.CharField(max_length=10)
    hash_name = models.TextField()

    def __str__(self):
        return str(self.file)

class Array_Like(models.Model):
    id_post = models.IntegerField()
    id_user = models.IntegerField()
