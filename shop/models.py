from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    video = models.FileField(upload_to='product_videos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Highlight(models.Model): # C'est ce modèle qui manque !
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='highlights/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title