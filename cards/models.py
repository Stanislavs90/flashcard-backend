from django.db import models


class flash_card(models.Model):
    question = models.CharField(max_length=3000)
    answer = models.CharField(max_length=3000)

    def __str__(self):
        return self.question

   