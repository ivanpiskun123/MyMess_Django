from django.db import models

class Cell(models.Model):
    name = models.CharField(max_length=100,unique=True,db_index=True)
    if_checks_cell = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Message(models.Model):
    text = models.CharField(max_length=500)
    date_create = models.DateTimeField(auto_now_add=True)
    cell = models.ForeignKey('Cell', on_delete = models.CASCADE,blank=False,related_name = 'messages')

    def __str__(self):
        return str(self.id)
