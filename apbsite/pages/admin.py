from django.contrib import admin

# Register your models here.

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'full_admin'),
      (2, 'limited_admin'),
      (3, 'editor'),
      
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)