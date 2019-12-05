# Generated by Django 3.0 on 2019-12-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Longitude', models.FloatField(help_text='Longitude')),
                ('Latitude', models.FloatField(help_text='Latitude')),
                ('Unique_id', models.CharField(help_text='Unique ID of squirrel', max_length=20)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Time of sighting', max_length=10)),
                ('Date', models.DateField(help_text='Date of sighting')),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='', help_text='Age of squirrel', max_length=16)),
                ('Primary_fur_color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], default='', help_text='Color of squirrel', max_length=16)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default='', help_text='Location', max_length=20)),
                ('Specific_location', models.CharField(blank=True, default='', help_text='Specific location', max_length=200)),
                ('Running', models.BooleanField(help_text='Squirrel was seen running')),
                ('Chasing', models.BooleanField(help_text='Squirrel was seen chasing')),
                ('Climbing', models.BooleanField(help_text='Squirrel was seen climbing')),
                ('Eating', models.BooleanField(help_text='Squirrel was seen eating')),
                ('Foraging', models.BooleanField(help_text='Squirrel was seen foraging')),
                ('Other_activities', models.CharField(blank=True, default='', help_text='Other activities', max_length=200)),
                ('Kuks', models.BooleanField(help_text='Squirrel was heard kukking')),
                ('Quaas', models.BooleanField(help_text='Squirrel was heard quaaing')),
                ('Moans', models.BooleanField(help_text='Squirrel was heard moaning')),
                ('Tail_flags', models.BooleanField(help_text='Squirrel was seen flagging its tail')),
                ('Tail_twitches', models.BooleanField(help_text='Squirrel was seen twitching its tail')),
                ('Approaches', models.BooleanField(help_text='Squirrel was seen approaching human')),
                ('Indifferent', models.BooleanField(help_text='Squirrel was seen indifferent to human presence')),
                ('Runs_from', models.BooleanField(help_text='Squirrel was seen running from human')),
            ],
        ),
    ]
