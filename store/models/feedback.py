from django.db import models
from .orders import Orderbase

class Feedback(models.Model):
    order = models.ForeignKey(Orderbase, on_delete=models.CASCADE)
    feedbackmsg = models.TextField(null=True)
    reply = models.TextField(blank=True, null=True)

