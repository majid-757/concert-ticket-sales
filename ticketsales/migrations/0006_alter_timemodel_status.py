# Generated by Django 3.2.6 on 2021-08-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0005_alter_profilemodel_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط شروع شده'), (2, 'قروش بلیط تمام شده'), (3, 'این سانس کنسل شده است'), (4, 'در حال فروش بلیط')], verbose_name='وضعیت'),
        ),
    ]
