# Generated by Django 5.0.2 on 2024-05-20 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authintication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercisesessionrelation',
            old_name='eId',
            new_name='exercise',
        ),
        migrations.RenameField(
            model_name='exercisesessionrelation',
            old_name='sId',
            new_name='session',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='mohamed', max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='exercisesession',
            name='exercises',
        ),
        migrations.AlterField(
            model_name='exercisesession',
            name='feedbackID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authintication.feedback'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='sessionID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authintication.exercisesession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercisesession',
            name='exercises',
            field=models.ManyToManyField(through='authintication.ExerciseSessionRelation', to='authintication.exercise'),
        ),
    ]