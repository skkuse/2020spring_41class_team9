from django.db import models

# Create your models here.

class Message(models.Model):
    m_id = models.AutoField(
        verbose_name = 'message ID',
        name = 'mID',
        primary_key = True,
        unique = True,
        null = False)

    is_read = models.BooleanField(
        verbose_name = 'is read by a receiver',
        name = 'is read')

    sent_time = models.DateTimeField(
        verbose_name = 'sent time',
        name = 'sent time')

    text = models.TextField(
        verbose_name = 'message text',
        name = 'text')

    sender = models.ForeignKey(         # - if not null then user message else system notification
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'messages',
        related_query_name = 'message'
        )
    
    receiver = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'messages',
        related_query_name = 'message'
        )

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return self.text
