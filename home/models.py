from django.db import models
from django.contrib.auth.models import User


REASONS = (('', 'Choose a reason'), (1, 'Giving feedback'),
           (2, 'Making a complaint'), (3, 'Looking for information'),
           (4, 'Other'),)


class CustomerMessage(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='customer_messages')
    reason = models.IntegerField(choices=REASONS, default=0)
    message = models.TextField(max_length=512, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'The user {self.customer} sent a message ' +
                f'to the staff on {self.created_on} for the following ' +
                f'reason: {self.reason}')
