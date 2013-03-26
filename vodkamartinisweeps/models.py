from django.db import models
from django.utils import timezone

class LiveSweepManager(models.Manager):
    """
    Manager that returns sweeps with status = LIVE_STATUS.
    """
    def get_query_set(self):
        return super(LiveSweepManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


class Sweep(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    objects = models.Manager()
    live = LiveSweepManager()

    title = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=128)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

    #def save(self, *args, **kwargs):
    #    """
    #    Auto created date.
    #    """

    #    #import pdb; pdb.set_trace()
    #    if not self.pk and not self.created:
    #        self.created = timezone.now()

    @models.permalink
    def get_absolute_url(self):
        return ('vodkamartinisweeps_sweep_detail', (), {'slug': self.slug})

#first_name = models.CharField(_('first name'), max_length=30, blank=True)
#last_name = models.CharField(_('last name'), max_length=30, blank=True)
#email = models.EmailField(_('e-mail address'), blank=True)
