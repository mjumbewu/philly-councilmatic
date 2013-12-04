from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis import gdal
from os.path import dirname, pardir, join as pathjoin
from regions.models import Region


class Command(BaseCommand):
    help = "Load neighborhood shapes from Azavea's repository."

    def handle(self, *args, **options):
        path = pathjoin(
            dirname(__file__),
            pardir, pardir,
            'azavea-geo-data',
            'Neighborhoods_Philadelphia',
            'Neighborhoods_Philadelphia.shp')

        shapefile = gdal.DataSource(path)
        for layer in shapefile:
            for feature in layer:
                try:
                    region = Region.objects.get(
                        layer='neighborhoods',
                        name=feature.get('listname'))
                    print 'Updating "%s"' % region.name
                except Region.DoesNotExist:
                    region = Region(
                        layer='neighborhoods',
                        name=feature.get('listname'))
                    print 'Loading "%s"' % region.name

        # Transform the projection from 102729 (NAD 1983 StatePlane
        # Pennsylvania South FIPS 3702 Feet) to 4326 (WSG 1984).
        #
        # Source: http://svn.osgeo.org/postgis/tags/0.7.4/spatial_ref_sys.sql
                region.shape = feature.geom.geos
                region.shape.srid = 102729
                region.shape.transform(4326)

                region.save()
