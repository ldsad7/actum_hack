from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel


class Purchase(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Название закупки"
    )
    author = models.ForeignKey(
        User, blank=False, null=False, verbose_name="Автор закупки",
        on_delete=models.CASCADE
    )
    participants = models.ManyToManyField(User, blank=True, related_name='purchases')

    def __str__(self):
        return f"purchase: {self.name}, author: {self.author}"

    class Meta:
        verbose_name = "Закупка"
        verbose_name_plural = "Закупки"
