# Generated by Django 3.1.5 on 2021-05-15 07:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='departmentsEligible',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BT', 'Bio Technology'), ('che', 'Chemical'), ('chem', 'Chemistry'), ('civil', 'Civil'), ('cse', 'Computer Science'), ('elec', 'Electrical'), ('ece', 'Electronics and Communication'), ('ipe', 'Industial and Production'), ('it', 'Information Technology'), ('ice', 'Instrumentation and Control'), ('maths', 'Mathematics'), ('phe', 'Physics'), ('tt', 'Texttile Technology')], default='cse', max_length=54),
        ),
        migrations.AddField(
            model_name='company',
            name='employmentType',
            field=models.CharField(blank=True, choices=[('intern', 'Internship'), ('fte', 'Full Time')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='package',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='programEligible',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BTech', 'Btech'), ('Mtech', 'Mtech')], default='BTech', max_length=11),
        ),
    ]
