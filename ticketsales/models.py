from django.db import models
from jalali_date import date2jalali, datetime2jalali

from accounts.models import ProfileModel

class ConcertModel(models.Model):

    class Meta:
        verbose_name = 'کنسرت'
        verbose_name_plural = 'کنسرت'

    name = models.CharField(max_length=100, verbose_name = 'نام کنسرت')
    singername = models.CharField(max_length=100, verbose_name = 'نام خواننده')
    length = models.IntegerField(verbose_name = 'طول کنسرت')
    poster = models.ImageField(upload_to="concertImages/", null=True, verbose_name = 'پوستر')

    def __str__(self):
        return self.singername


class LocationModel(models.Model):

    class Meta:
        verbose_name = 'محل برگزاری'
        verbose_name_plural = 'محل برگزاری'

    name = models.CharField(max_length=100, verbose_name = 'نام محل')
    address = models.CharField(max_length=500, default="تهران شهرک غرب", verbose_name = 'آدرس')
    phone = models.CharField(max_length=11, null=False, verbose_name = 'تلفن')
    capacity = models.IntegerField(verbose_name = 'ظرفیت')

    def  __str__(self):
        return self.name



class TimeModel(models.Model):

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    concertModel = models.ForeignKey(to=ConcertModel, on_delete=models.PROTECT, verbose_name = 'کنسرت')
    locationModel = models.ForeignKey(to=LocationModel, on_delete=models.PROTECT, verbose_name = 'محل برگزاری')
    startdatetime = models.DateTimeField(verbose_name = 'تاریخ و زمان برگزاری')
    seats = models.IntegerField(verbose_name = 'تعداد صندلی ها')

    start = 1
    end = 2
    cancel = 3
    sales = 4
    status_choices = (
        ("start", "فروش بلیط شروع شده"),
        ("end", "فروش بلیط تمام شده"),
        ("cancel", "این سانس کنسل شده است"),
        ("sales", "در حال فروش بلیط"),

    )
    status = models.IntegerField(choices=status_choices, verbose_name = 'وضعیت')


    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.startdatetime, self.concertModel.name, self.locationModel.name)

    def get_jalali_date(self):
        return datetime2jalali(self.startdatetime)


class TicketModel(models.Model):

    class Meta:
        verbose_name = 'بلیط'
        verbose_name_plural = 'بلیط'

    profilemodel = models.ForeignKey(ProfileModel, on_delete=models.PROTECT, verbose_name = 'کاربر')
    timemodel = models.ForeignKey(to=TimeModel, on_delete=models.PROTECT, verbose_name = 'سانس')
    ticketimage = models.ImageField(upload_to="ticketImages/", null=True, verbose_name = 'عکس')

    name = models.CharField(max_length=100, verbose_name = 'عنوان')
    price = models.IntegerField(verbose_name = 'مبلغ')


    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(timeModel.__str__())


