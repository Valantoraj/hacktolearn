from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='blog\\static\\images\\upload')  # Save images in the 'images/' directory
    uploaded_at = models.DateTimeField(auto_now_add=True)