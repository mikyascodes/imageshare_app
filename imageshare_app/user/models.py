from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.


class Memeber(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    profile_pic = models.ImageField(
        upload_to="profile_pics/", default="uploads/default.jpg"
    )
    is_staff = models.BooleanField(("staff status"), default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    def save(self, *args, **kwargs):
        super(Memeber, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
