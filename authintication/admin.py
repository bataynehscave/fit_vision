

from django.contrib import admin
from .models import Profile, AIModel, Trainer, Consultation, Exercise, Feedback, Recommendation, ExerciseSession, ExerciseSessionRelation, SensorData, Progress

admin.site.register(Profile)
admin.site.register(AIModel)
admin.site.register(Trainer)
admin.site.register(Consultation)
admin.site.register(Exercise)
admin.site.register(Feedback)
admin.site.register(Recommendation)
admin.site.register(ExerciseSession)
admin.site.register(ExerciseSessionRelation)
admin.site.register(SensorData)
admin.site.register(Progress)
