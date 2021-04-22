from django.db import models


# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", blank=False)
    surname = models.CharField(max_length=100, verbose_name="Фамилия", blank=False)
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    photo = models.ImageField(upload_to='media/', verbose_name="Фото", blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
