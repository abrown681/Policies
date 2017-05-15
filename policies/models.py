from django.db import models
from django.utils import timezone

class Rule(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50, verbose_name='Policy name')
    priority = models.PositiveSmallIntegerField(verbose_name='Priority level')
    day = models.CharField(max_length=10, blank=True, null=True, verbose_name='Day requirement')
    US_Government = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    UNCLASSIFIED = 'UC'
    CONFIDENTIAL = 'CF'
    SECRET = 'S'
    TOP_SECRET = 'TS'
    CLEAR_LEVEL_CHOICES = (
        (UNCLASSIFIED, 'UNCLASSIFIED'),
        (CONFIDENTIAL, 'CONFIDENTIAL'),
        (SECRET, 'SECRET'),
        (TOP_SECRET, 'TOP_SECRET'),
    )
    clear_level = models.CharField(
        max_length=2,
        choices=CLEAR_LEVEL_CHOICES,
        verbose_name = 'Clearance level',
        #default=TOP_SECRET,
    )

    UNITED_STATES = 'USA'
    GREAT_BRITIAN = 'GBR'
    CANADA = 'CAN'
    AUSTRALIA = 'AUS'
    NEW_ZEALAND = 'NZL'
    CITIZENSHIP_CHOICES = (
        (UNITED_STATES, 'United States'),
        (GREAT_BRITIAN, 'Great Britian'),
        (CANADA, 'Canada'),
        (AUSTRALIA, 'Australia'),
        (NEW_ZEALAND, 'New Zealand'),
    )
    citizenship = models.CharField(
        max_length=3,
        choices=CITIZENSHIP_CHOICES,
        #default=UNITED_STATES,
    )

    def publish(self):
        self.published_date=timezone.now()
        self.save

    def __str__(self):
        return self.title
