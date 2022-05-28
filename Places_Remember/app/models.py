from django.db import models


class Remembers(models.Model):
    header = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    remember_photo = models.ImageField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header




