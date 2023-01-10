from django.db import models
class Task(models.Model):
    task=models.CharField(max_length=500)
    def __str__(self):
        return f'TASK IS {self.task}'

class Fileupload(models.Model):
    title=models.CharField(max_length=100)
    detail=models.CharField(max_length=200)
    filepath=models.CharField(max_length=100)
    def __str__(self):
        return F'title is {self.title} detail {self.detail} path {self.filepath}'

class Comment(models.Model):
    comment=models.CharField(max_length=300)
    def __str__(self):
        return f'{self.comment}'