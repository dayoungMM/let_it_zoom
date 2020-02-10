from django.db import models


class food_list(models.Model):
    foodName = models.CharField(max_length=50)
    foodImg = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.foodName) + str(self.foodImg)
    class Meta:
        db_table = 'food_list'

class animal_list(models.Model):
    foodName = models.CharField(max_length=50)
    foodImg = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.foodName) + str(self.foodImg)
    class Meta:
        db_table = 'animal_list'



class user(models.Model):
    nickName = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return str(self.nickName) + str(self.score) +str(pub_date)
    class Meta:
        db_table = 'user'