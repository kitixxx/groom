from django.db import models

from reception.validators import validate_week_day, validate_not_past_date


class master(models.Model):
    

    name = models.CharField('Имя (хозяин)', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('кличка, порода', max_length=50)

    class Meta:
        db_table = 'groomer'
        verbose_name = 'грумер'
       

    def __str__(self):
        return '{self.surname} {self.name} {self.patronymic}'.format(self=self)


class Reception(models.Model):
    """Карточка записи на прием."""

    TIME_CHOICES = (
        (0, '10:00'),
        (1, '12:00'),
        (2, '14:00'),
        (3, '16:00'),
        
    )

    master = models.ForeignKey(master, verbose_name='К специалисту')
    date = models.DateField(
        'Дата', validators=[validate_week_day, validate_not_past_date])
    time = models.PositiveSmallIntegerField('Время', choices=TIME_CHOICES)
    fio = models.CharField('ФИО', max_length=150)

    class Meta:
        db_table = 'receptions'
        verbose_name = 'Карточка приема'
        verbose_name_plural = 'Карточки приема'
        unique_together = 'master', 'date', 'time'

    def __str__(self):
        return '{self.master}: {self.date} {self.verbose_time}'.format(
            self=self)

    @property
    def verbose_time(self):
        return dict(self.TIME_CHOICES).get(self.time)
