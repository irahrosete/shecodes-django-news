from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    favourites = models.ManyToManyField(USER, related_name="news_stories")

    def total_favourites(self):
        return self.favourites.count()