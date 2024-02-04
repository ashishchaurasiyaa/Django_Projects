from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT,primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff': True})
    page_name = models.CharField(max_length=100)
    page_cat = models.CharField(max_length=100)
    page_publish_date = models.DateField()

class Like(Page):
    panna = models.OneToOneField(Page, on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()

class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(max_length=100)
    post_cat = models.CharField(max_length=100)
    post_publish_date = models.DateField()


class Song(models.Model):
    user= models.ManyToManyField(User)
    song_name = models.CharField(max_length=100)
    song_duration = models.FloatField()

    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])