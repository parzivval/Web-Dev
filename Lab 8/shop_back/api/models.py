from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name + " " + str(self.price)
    def to_json(self):
        if self is None:
            return {}
        return {
            "id": self.pk,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "count": self.count,
            "is_active": self.is_active,
            "category": self.category.to_json(),
        }
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def to_json(self):
        if self is None:
            return {}
        return {
            "id": self.pk,
            "name": self.name,
        }
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


