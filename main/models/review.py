from ckeditor.fields import RichTextField
from django.db import models

class Review(models.Model):
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    merchant = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.consumer}的评论"
