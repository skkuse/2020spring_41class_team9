from django.db import models

# Create your models here.

class Comment(models.Model):

    cID = models.CharField(
        primary_key=True,
        max_length=20,
    )

    comment_text = models.TextField(
        verbose_name='comment text',
        max_length=500
    )

    sent_time = models.DateTimeField(auto_now_add=True)

    pID = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment'
    )

    writer = models.ForeignKey(
        'Developer',
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment'
    )

class Meta:
    verbose_name = 'comment'
    ordering = ['sent_time']

def __str__(self):
    return "".format(
        self.comment_text,
        self.writer,
        self.sent_time
    )

