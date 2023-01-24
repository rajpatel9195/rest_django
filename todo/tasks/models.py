from django.db import models

class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted= False)



class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    
    deletedall = models.Manager()
    objects = NonDeleted()
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
        
    def restore(self):
        self.is_deleted = False
        self.save()
        
    class Meta:
        abstract = True    
            





class Task(SoftDelete):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    