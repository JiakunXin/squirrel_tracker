from django.db import models
from django.utils.translation import gettext as _

class squirrel(models.Model):
    Longitude = models.FloatField(
            help_text=_('Longitude'),
            )

    Latitude = models.FloatField(
            help_text=_('Latitude'),
            )

    Unique_id = models.CharField(
            max_length=20,
            help_text=_('Unique ID of squirrel'),
            )

    AM='AM'
    PM='PM'

    SHIFT_CHOICE=(
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift = models.CharField(
            max_length=10,
            help_text=_('Time of sighting'),
            choices=SHIFT_CHOICE,
            )

    Date = models.DateField(
            help_text=_('Date of sighting'),
            )

    ADULT='Adult'
    JUVENILE='Juvenile'

    AGE_CHOICE=(
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            )

    Age = models.CharField(
            max_length=16,
            help_text=_('Age of squirrel'),
            choices=AGE_CHOICE,
            blank=True,
            default='',
            )

    GRAY='Gray'
    BLACK='Black'
    CINNAMON='Cinnamon'

    COLOR_CHOICE=(
            (BLACK,'Black'),
            (GRAY,'Gray'),
            (CINNAMON,'Cinnamon'),
            )

    Primary_fur_color=models.CharField(
            max_length=16,
            help_text=_('Color of squirrel'),
            choices=COLOR_CHOICE,
            blank=True,
            default='',
            )

    GROUND_PLANE='Ground Plane'
    OVER_GROUND='Above Ground'

    LOCATION_CHOICE=(
            (GROUND_PLANE,'Ground Plane'),
            (OVER_GROUND,'Above Ground'),
            )

    Location=models.CharField(
            max_length=20,
            help_text=_('Location'),
            choices=LOCATION_CHOICE,
            blank=True,
            default='',
            )

    Specific_location=models.CharField(
            max_length=200,
            help_text=_('Specific location'),
            blank=True,
            default='',
            )

    Running=models.BooleanField(
            help_text=_('Squirrel was seen running'),
            )

    Chasing=models.BooleanField(
            help_text=_('Squirrel was seen chasing'),
            )

    Climbing=models.BooleanField(
            help_text=_('Squirrel was seen climbing'),
            )

    Eating=models.BooleanField(
            help_text=_('Squirrel was seen eating'),
            )

    Foraging=models.BooleanField(
            help_text=_('Squirrel was seen foraging'),
            )

    Other_activities=models.CharField(
            max_length=200,
            help_text=_('Other activities'),
            blank=True,
            default='',
            )

    Kuks=models.BooleanField(
            help_text=_('Squirrel was heard kukking'),
            )

    Quaas=models.BooleanField(
            help_text=_('Squirrel was heard quaaing'),
            )

    Moans=models.BooleanField(
            help_text=_('Squirrel was heard moaning'),
            )

    Tail_flags=models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail'),
            )

    Tail_twitches=models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail'),
            )

    Approaches=models.BooleanField(
            help_text=_('Squirrel was seen approaching human'),
            )

    Indifferent=models.BooleanField(
            help_text=_('Squirrel was seen indifferent to human presence'),
            )

    Runs_from=models.BooleanField(
            help_text=_('Squirrel was seen running from human'),
            )

    def __str__(self):
        return self.Unique_id
