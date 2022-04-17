from django.db import models
from user.models import User,Role


class SendNotification(models.Model):
    send_notification_by = models.ForeignKey(User,related_name='send_by' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_status=models.BooleanField(default=False)
    role= models.ManyToManyField(Role)
    user= models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Send Notification'
        verbose_name_plural = 'Send Notifications'

    def __str__(self) -> str:
        return self.title