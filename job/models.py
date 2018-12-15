from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Work(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250,default='')
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',default='')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='job_works',default='')
    image = models.ImageField(upload_to='images/',default='')
    website= models.URLField(max_length=250, default='')
    gitlink= models.URLField(max_length=250, default='')
    body = models.TextField(default='')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title



                    # class Job(models.Model):
                    #     jobtitle = models.CharField(max_length=250, default='')
                    #     image = models.ImageField(upload_to='images/',default='')
                    #     summary = models.CharField(max_length=200,default='')
                    #     website= models.URLField(max_length=250, default='')
                    #     objects = models.Manager() # The default manager.
                    #
                    #
                    #
                    #     def __str__(self):
                    #         return self.jobtitle
