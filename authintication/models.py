from django.contrib.auth.models import User
from django.db import models

class AIModel(models.Model):
    modelID = models.AutoField(primary_key=True)
    modelName = models.CharField(max_length=100, null=True)
    version = models.CharField(max_length=50, null=True)
    accuracy = models.FloatField(null=True)

    def __str__(self):
        return self.modelName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # This should be a separate field
    age = models.IntegerField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fitnessLevel = models.CharField(max_length=50, null=True)
    goals = models.TextField(null=True)
    preferences = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    trainerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    certification = models.TextField(null=True)
    expertise = models.TextField(null=True)
    availability = models.TextField(null=True)
    contactInfo = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Consultation(models.Model):
    consultationID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    notes = models.TextField(null=True)
    recommendations = models.TextField(null=True)

class Exercise(models.Model):
    exerciseID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.CharField(max_length=50, null=True)
    equipment = models.CharField(max_length=50, null=True)
    difficultyLevel = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=255, null=True)
    video = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    feedbackID = models.AutoField(primary_key=True)
    sessionID = models.ForeignKey('ExerciseSession', on_delete=models.CASCADE)
    comments = models.TextField(null=True)
    rating = models.IntegerField(null=True)

class Recommendation(models.Model):
    recommendationID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.TextField(null=True)
    dietPlan = models.TextField(null=True)
    tips = models.TextField(null=True)

class ExerciseSession(models.Model):
    sessionID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    duration = models.FloatField(null=True)
    exercises = models.ManyToManyField(Exercise, through='ExerciseSessionRelation')
    feedbackID = models.ForeignKey(Feedback, null=True, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, null=True, on_delete=models.CASCADE)

class ExerciseSessionRelation(models.Model):
    session = models.ForeignKey(ExerciseSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class SensorData(models.Model):
    sensorID = models.AutoField(primary_key=True)
    sessionID = models.ForeignKey(ExerciseSession, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(null=True)
    data = models.TextField(null=True)

class Progress(models.Model):
    progressID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bodyFatPercentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    muscleMass = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    progressPhotos = models.CharField(max_length=255, null=True)
