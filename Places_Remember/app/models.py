from django.contrib.auth.models import User
from django.db import models


class Impression(models.Model):
    '''Выбор места, для добавления воспоминаний'''

    list_impressions = []

    name_place = models.CharField(max_length=30, verbose_name="Название места")
    comments = models.TextField(max_length=120, verbose_name="Комментарии")
    img_impression = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name_place)

    def add_impression(self, img_impression):
        '''Добавляет в картинки в list_impression'''
        self.list_impressions.append(img_impression)


class AdvUser(Impression):
    '''Проверка на аунтетификацию'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Активировался?')

