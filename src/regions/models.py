from django.contrib.gis.db import models
from councilmatic.phillyleg.models import LegFile


class Region (models.Model):
    """
    A Region is any shape that can be used as a filter for legislation. Sample
    regions may be neighborhoods, zip codes, council districts, or precincts.
    Regions filter legislation according to whether the legislation mentions a
    place that falls within the bounds of the region.

    To load the Azavea neighborhoods, run:

        python manage.py load_azavea_neighborhoods

    """
    LAYER_CHOICES = (
        ('zipcodes', 'Zip Codes'),
        ('districts', 'Districts'),
        ('neighborhoods', 'Neighborhoods'),
    )

    name = models.CharField(max_length=100)
    layer = models.CharField(max_length=50, choices=LAYER_CHOICES)
    shape = models.GeometryField()

    def legislation(self):
        legislation = LegFile.objects\
            .filter(metadata__locations__valid=True)\
            .filter(metadata__locations__geom__within=self.shape)
        return legislation
