from django.contrib import admin
from . import models
from django import forms



admin.site.register(models.Anime)
admin.site.register(models.Ganres)
admin.site.register(models.Studios)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
admin.site.register(models.Post)
admin.site.register(models.AnimeShots)
admin.site.register(models.Rating)
admin.site.register(models.RatingStar)
admin.site.register(models.CheckOngiing)