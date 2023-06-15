# Generated by Django 4.2.2 on 2023-06-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_name', models.TextField(unique=True)),
                ('street_address', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'tb_housing_complexes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lease_start', models.TextField()),
                ('lease_end', models.TextField()),
                ('created_date', models.TextField()),
            ],
            options={
                'db_table': 'tb_leases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('resident_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.TextField(unique=True)),
                ('phone', models.TextField(unique=True)),
                ('birthdate', models.TextField()),
                ('gender', models.TextField()),
            ],
            options={
                'db_table': 'tb_resident_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.TextField()),
                ('gender', models.TextField()),
                ('room', models.TextField()),
                ('bed', models.TextField()),
                ('room_type', models.TextField()),
                ('rent_price', models.FloatField()),
            ],
            options={
                'db_table': 'tb_student_housing_units',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TbHousingComplexes',
        ),
        migrations.DeleteModel(
            name='TbLeases',
        ),
        migrations.DeleteModel(
            name='TbResidentInfo',
        ),
        migrations.DeleteModel(
            name='TbStudentHousingUnits',
        ),
    ]