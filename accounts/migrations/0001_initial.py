# Generated by Django 3.2.6 on 2021-08-18 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('profileimage', models.ImageField(null=True, upload_to='profileImages/', verbose_name='عکس')),
                ('gender', models.CharField(choices=[('man', 'مرد'), ('woman', 'زن')], max_length=50, verbose_name='جنسیت')),
                ('credit', models.IntegerField(default=0, verbose_name='اعتبار')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر',
            },
        ),
    ]
