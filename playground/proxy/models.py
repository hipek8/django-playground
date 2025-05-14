from django.db import models

# Create your models here.

class BaseObject(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class DCHost(models.Model):
    objects = models.Manager()
    hostname = models.CharField(max_length=100)


    class Meta:
        abstract = True


class VM(DCHost, BaseObject):
    pass


class DCAsset(DCHost, BaseObject):
    pass


# class DCHost(BaseObject):
# #    hostname = models.CharField(max_length=100)
#
#     class Meta:
#         proxy = True