from django.db import models


class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200,
                             help_text='the title of the blog post')
    content = models.TextField()
    status = models.CharField(choices=STATUS, default='draft', max_length=20)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + " - " + str(self.date_created)


