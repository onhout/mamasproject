from django.db import models

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class MenuPicURL(models.Model):
    itemurl = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)