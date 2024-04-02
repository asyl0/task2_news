from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    image = models.CharField("Сссылка на фото", max_length=500)
    description = models.TextField("Описания")
    post_date = models.DateTimeField("Дата публикации", default=datetime.now)


    def __str__(self):
        return self.title