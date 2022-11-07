from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Problem(models.Model):
    """ User`s question model """

    class Status(models.IntegerChoices):
        unresolved = 1, 'unresolved'
        solved = 2, 'solved'
        frozen = 3, 'frozen'

    objects = models.Manager()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Question author')
    title = models.CharField(max_length=256, unique=True, verbose_name='Question title')
    description = models.TextField(verbose_name='Description of the problem', blank=False)
    date_created = models.DateTimeField(default=timezone.now, verbose_name='Data of creation')
    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.unresolved,
        verbose_name='Problem status')

    def __str__(self):
        return f'{self.title} - Status:{self.status}'

    class Meta:
        ordering = ('date_created',)
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    """ Answer model of discussion """
    objects = models.Manager()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Answer author')
    text = models.TextField(verbose_name='Discussion text')
    date_created = models.DateTimeField(default=timezone.now, verbose_name='Data of creation')
    response_problem = models.ForeignKey('task.Problem', on_delete=models.CASCADE, verbose_name='Discussion')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        ordering = ('date_created',)
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
