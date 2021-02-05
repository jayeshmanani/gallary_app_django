from django.db import models

# Create your models here.
class ImageCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200, default='Other')
    def __str__(self):
        return self.category

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category_id = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

