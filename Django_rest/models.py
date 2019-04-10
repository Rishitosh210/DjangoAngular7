from django.db import models

# Create your models here.


class TestModel(models.Model):
    test_char=models.CharField(max_length=50,db_index=True)
    test_int=models.IntegerField(db_index=True)

    def __str__(self):
        return self.test_char