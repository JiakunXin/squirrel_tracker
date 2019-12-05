'''
Export data from database to .csv file
'''
import csv
from django.core.management.base import BaseCommand
from sightings.models import squirrel
from datetime import datetime

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('File path',type=str)

    def handle(self,*args,**kwargs):
        file_path = kwargs['File path']
        all_objects = squirrel.objects.all()
        with open(file_path,'w') as csvfile:
            writer=csv.writer(csvfile)
            #write the header
            writer.writerow(['X',
                             'Y',
                             'Unique Squirrel ID',
                             'Shift',
                             'Date',
                             'Age',
                             'Primary Fur Color',
                             'Location',
                             'Specific Location',
                             'Running',
                             'Chasing',
                             'Climbing',
                             'Eating',
                             'Foraging',
                             'Other Activities',
                             'Kuks',
                             'Quaas',
                             'Moans',
                             'Tail flags',
                             'Tail twitches',
                             'Approaches',
                             'Indifferent',
                             'Runs from',
                             ])

            for obj in all_objects:
                #convert the date to the same format as the date in source data
                date = datetime.strftime(obj.Date,'%m%d%Y')
                writer.writerow([obj.Longitude,
                                 obj.Latitude,
                                 obj.Unique_id,
                                 obj.Shift,
                                 date,
                                 obj.Age,
                                 obj.Primary_fur_color,
                                 obj.Location,
                                 obj.Specific_location,
                                 #convert False and True to 'false' and 'true' 
                                 str(obj.Running).lower(),
                                 str(obj.Chasing).lower(),
                                 str(obj.Climbing).lower(),
                                 str(obj.Eating).lower(),
                                 str(obj.Foraging).lower(),
                                 obj.Other_activities,
                                 str(obj.Kuks).lower(),
                                 str(obj.Quaas).lower(),
                                 str(obj.Moans).lower(),
                                 str(obj.Tail_flags).lower(),
                                 str(obj.Tail_twitches).lower(),
                                 str(obj.Approaches).lower(),
                                 str(obj.Indifferent).lower(),
                                 str(obj.Runs_from).lower(),
                                 ])
