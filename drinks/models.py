
from django.db import models


class Drink(models.Model):
    name = models.CharField((""), max_length=200)
    description = models.CharField((""), max_length=500)
    def __str__(self):
        return self.name
    
 
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)  

#     def __str__(self):
#         return self.name




    # class Meta: = ("")
    #     verbose_name_plural = ("s")
        # verbose_name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
# ):
    
    # def __init__(self, *args):
        # super(ClassName, self).__init__(*args))

# from django.db import models


# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
