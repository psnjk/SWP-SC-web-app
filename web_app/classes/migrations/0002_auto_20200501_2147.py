# Generated by Django 3.0.5 on 2020-05-01 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportgroup',
            name='students',
            field=models.ManyToManyField(to='users.Student', verbose_name='Students enrolled in the group'),
        ),
        migrations.AddField(
            model_name='sportgroup',
            name='trainers',
            field=models.ManyToManyField(to='users.Trainer', verbose_name='Trainers of the group'),
        ),
        migrations.AddField(
            model_name='sportclass',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.SportGroup'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='sport_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.SportClass'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
    ]
