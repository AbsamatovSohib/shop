from django.contrib import admin
from django.apps import apps
from .models import Category

post_models = apps.get_app_config('common').get_models()

for model in post_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# admin.site.register(Category)
