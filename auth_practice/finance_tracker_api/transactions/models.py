from django.db import models
import uuid
from django.conf import settings
class Transaction(models.Model):
    "a model to handle transactions information"
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    typeChoices=[('INCOME','Income'),
                 ('EXPENSES','Expenses')]

    def __str__(self):
        return f"{self.user.username}'s {self.description} - {self.amount}"