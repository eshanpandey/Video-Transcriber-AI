from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ArticlePost(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)#user who created the article
    video_title=models.CharField(max_length=300)
    youtube_link = models.URLField(max_length=300)
    generated_content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title