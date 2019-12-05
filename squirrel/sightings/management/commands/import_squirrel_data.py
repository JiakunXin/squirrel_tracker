'''
Import squirrel data from .csv file to database
'''
import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import squirrel

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('File path',type=str)
    
    def handle(self,*args,**kwargs):
        file_path = kwargs['File path']
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            squirrel_data = list(reader)

        #remove the duplicate sightings with the same unique squirrel ID
        unique_id_list = list()
        final_data = list()
        for item in squirrel_data:
            if item['Unique Squirrel ID'] not in unique_id_list:
                unique_id_list.append(item['Unique Squirrel ID'])
                final_data.append(item)

        #save the data into database
        for item in final_data:        
            date = datetime.datetime.strptime(item['Date'],'%m%d%Y')
            string_date = datetime.datetime.strftime(date,'%Y-%m-%d')

            sighting = squirrel(Longitude=float(item['X']),
                                Latitude=float(item['Y']),
                                Unique_id=item['Unique Squirrel ID'],
                                Shift=item['Shift'],
                                Date=string_date,
                                Age=item['Age'],
                                Primary_fur_color=item['Primary Fur Color'],
                                Location=item['Location'],
                                Specific_location=item['Specific Location'],
                                Running=(item['Running']=='true'),
                                Chasing=(item['Chasing']=='true'),
                                Climbing=(item['Climbing']=='true'),
                                Eating=(item['Eating']=='true'),
                                Foraging=(item['Foraging']=='true'),
                                Other_activities=item['Other Activities'],
                                Kuks=(item['Kuks']=='true'),
                                Quaas=(item['Quaas']=='true'),
                                Moans=(item['Moans']=='true'),
                                Tail_flags=(item['Tail flags']=='true'),
                                Tail_twitches=(item['Tail twitches']=='true'),
                                Approaches=(item['Approaches']=='true'),
                                Indifferent=(item['Indifferent']=='true'),
                                Runs_from=(item['Runs from']=='true'),
                                )
            sighting.save()
