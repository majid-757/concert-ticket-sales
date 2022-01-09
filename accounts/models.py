from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'

    user = models.OneToOneField(User, verbose_name= 'کاربری', on_delete=models.CASCADE, related_name='profile')
    # name = models.CharField(max_length=50, verbose_name = 'نام')
    # family = models.CharField(max_length=100, verbose_name = 'نام خانوادگی')
    profileimage = models.ImageField(upload_to="profileImages/", null=True, verbose_name = 'عکس')

    status_choices = (
        ("man", "مرد"),
        ("woman", "زن"),
    )

    gender = models.CharField(max_length=50 ,choices=status_choices, verbose_name = 'جنسیت')
    credit = models.IntegerField(default=0, verbose_name = 'اعتبار')

    # def __str__(self):
    #     return "Fullname: {} {}".format(self.name, self.family)


