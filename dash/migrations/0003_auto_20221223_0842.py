# Generated by Django 3.2.5 on 2022-12-23 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20221223_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b1_visited_dist', models.CharField(blank=True, max_length=30, verbose_name='District')),
                ('b21_2_spot', models.CharField(blank=True, max_length=30, verbose_name='Spot')),
                ('b2_cbt_known', models.BooleanField(verbose_name='b2_cbt_known')),
                ('b3_cbt_need', models.BooleanField(verbose_name='b3_cbt_need')),
                ('b4_cbt_visit', models.BooleanField(verbose_name='b4_cbt_visit')),
                ('b5_cbt_attraction', models.CharField(blank=True, max_length=30, verbose_name='Your CBT Attractions')),
                ('b6_cbt_facility', models.CharField(blank=True, max_length=30, verbose_name='b6_cbt_facility')),
                ('b7_vacation_package', models.CharField(blank=True, max_length=30, verbose_name='b7_vacation_package')),
                ('b8_tour_operator', models.BooleanField(verbose_name='b8_tour_operator')),
                ('b9_tour_operator_ev', models.IntegerField(verbose_name='b9_tour_operator_ev')),
            ],
        ),
        migrations.AddField(
            model_name='tourist',
            name='a10_travel_interest',
            field=models.CharField(blank=True, max_length=30, verbose_name='Travel interest'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a11_season_choices',
            field=models.CharField(blank=True, max_length=30, verbose_name='Season prefer'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a12_yearly_travel',
            field=models.IntegerField(blank=True, null=True, verbose_name='Average travel day in a year'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a4_occupation',
            field=models.CharField(blank=True, max_length=30, verbose_name='Occupation'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a5_education',
            field=models.CharField(blank=True, max_length=30, verbose_name='Education'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a6_mobile',
            field=models.CharField(blank=True, max_length=15, verbose_name='Mobile'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a7_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email address'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a8_home_dist',
            field=models.CharField(blank=True, max_length=30, verbose_name='District'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='a9_tour_type',
            field=models.CharField(blank=True, max_length=30, verbose_name='Tour type'),
        ),
        migrations.AlterField(
            model_name='cbt_attraction',
            name='cbt_attraction',
            field=models.CharField(max_length=15, verbose_name='CBT attraction'),
        ),
        migrations.AlterField(
            model_name='tour_type',
            name='tour_type',
            field=models.CharField(max_length=30, verbose_name='Tour type'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='a2_age',
            field=models.IntegerField(blank=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='a3_gender',
            field=models.CharField(blank=True, max_length=30, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='travel_interest',
            name='travel_interest',
            field=models.CharField(max_length=30, verbose_name='Travel interest'),
        ),
        migrations.AlterField(
            model_name='travel_season',
            name='travel_season',
            field=models.CharField(max_length=15, verbose_name='Travel season'),
        ),
    ]
