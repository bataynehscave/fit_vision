# Generated by Django 5.0.2 on 2024-05-20 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIModel',
            fields=[
                ('modelID', models.AutoField(primary_key=True, serialize=False)),
                ('modelName', models.CharField(max_length=100, null=True)),
                ('version', models.CharField(max_length=50, null=True)),
                ('accuracy', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exerciseID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(max_length=50, null=True)),
                ('equipment', models.CharField(max_length=50, null=True)),
                ('difficultyLevel', models.CharField(max_length=50, null=True)),
                ('image', models.CharField(max_length=255, null=True)),
                ('video', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedbackID', models.AutoField(primary_key=True, serialize=False)),
                ('sessionID', models.IntegerField(null=True)),
                ('comments', models.TextField(null=True)),
                ('rating', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainerID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('certification', models.TextField(null=True)),
                ('expertise', models.TextField(null=True)),
                ('availability', models.TextField(null=True)),
                ('contactInfo', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSession',
            fields=[
                ('sessionID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(null=True)),
                ('duration', models.FloatField(null=True)),
                ('exercises', models.TextField(null=True)),
                ('feedbackID', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSessionRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authintication.exercise')),
                ('sId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authintication.exercisesession')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('fitnessLevel', models.CharField(max_length=50, null=True)),
                ('goals', models.TextField(null=True)),
                ('preferences', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('progressID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bodyFatPercentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('muscleMass', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('progressPhotos', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('recommendationID', models.AutoField(primary_key=True, serialize=False)),
                ('exercises', models.TextField(null=True)),
                ('dietPlan', models.TextField(null=True)),
                ('tips', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exercisesession',
            name='recommendation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authintication.recommendation'),
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('sensorID', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(null=True)),
                ('data', models.TextField(null=True)),
                ('sessionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authintication.exercisesession')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('consultationID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('notes', models.TextField(null=True)),
                ('recommendations', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authintication.trainer')),
            ],
        ),
    ]