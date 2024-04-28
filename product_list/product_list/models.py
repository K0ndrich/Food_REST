from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=300)
    info = models.TextField()
    img_link = models.TextField()
    manufacture = models.TextField(null=True, blank=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, blank=True)


class Category(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pk} | {self.name}"
