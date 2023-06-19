from django.db import models
from django.utils.text import slugify
from django_comments.moderation import CommentModerator, moderator
import os

class Page(models.Model):

    title_en = models.CharField(max_length = 50)
    title_de = models.CharField(max_length = 50, default='')
    title_fr = models.CharField(max_length = 50, default='')
    text = models.TextField()
    text_de = models.TextField(default='')
    text_fr = models.TextField(default='')
    slug = models.CharField(max_length = 50, editable=False)
  
    @property
    def title(self):
        match os.environ['LOCALIZATION']:
            case 'de':
                if (self.title_de.strip() == ''):
                    return self.title
                return self.title_de
            case 'fr':
                if (self.title_fr.strip() == ''):
                    return self.title
                return self.title_fr
            case _:
                return self.title_en

    def __unicode__ (self):
        return self.title_en

    def save(self):
        self.slug = slugify(self.title_en)
        super(Page, self).save()

    class Meta:
        db_table = "page"

class News(models.Model):

    title_en = models.CharField(max_length = 50)
    title_de = models.CharField(max_length = 50, default='')
    title_fr = models.CharField(max_length = 50, default='')
    text = models.TextField()
    text_de = models.TextField(default='')
    text_fr = models.TextField(default='')
    slug = models.CharField(max_length = 50, editable=False)

    @property
    def title(self):
        match os.environ['LOCALIZATION']:
            case 'de':
                if (self.title_de.strip() == ''):
                    return self.title
                return self.title_de
            case 'fr':
                if (self.title_fr.strip() == ''):
                    return self.title
                return self.title_fr
            case _:
                return self.title_en

    def __unicode__ (self):
        return self.title_en

    def save(self):
        self.slug = slugify(self.title_en)
        super(News, self).save()

    class Meta:
        db_table = "news"
        verbose_name = "news"
        verbose_name_plural = "news"

class NewsModerator(CommentModerator):
    email_notification = True
    auto_close_field   = 'posted_date'
    close_after        = 7

moderator.register(News, NewsModerator)