from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract model for the common fields 'created' and 'last_modified'.
    """
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Page(TimeStampedModel):
    """
    Represents page in the diary. There will be only one page
    for a particular user on a particular day.
    """
    day = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    html_content = models.TextField(blank=True)


    def save(self, *args, **kwargs):
        """
        Generate html from the markdown content.
        """
        super(Page, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %s" % (self.title, self.day)
