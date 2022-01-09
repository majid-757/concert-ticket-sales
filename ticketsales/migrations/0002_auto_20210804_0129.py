# Generated by Django 3.2.6 on 2021-08-03 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='address',
            field=models.CharField(default='تهران شهرک غرب', max_length=500),
        ),
        migrations.CreateModel(
            name='TimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdatetime', models.DateTimeField()),
                ('seats', models.IntegerField()),
                ('status', models.IntegerField(choices=[('start', 'فروش بلیط شروع شده'), ('end', 'قروش بلیط تمام شده'), ('cancel', 'این سانس کنسل شده است'), ('sales', 'در حال فروش بلیط')])),
                ('concertModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketsales.concertmodel')),
                ('locationModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketsales.locationmodel')),
            ],
        ),
    ]