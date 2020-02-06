from django.db import models


class food_list(models.Model):
    foodName = models.CharField(max_length=50)
    foodImg = models.CharField(max_length=1000)
    def __str__(self):
        return self.foodName, self.foodImg
    class Meta:
        db_table = 'food_list'



class user(models.Model):
    nickName = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.nickName, self.score
    class Meta:
        db_table = 'user'