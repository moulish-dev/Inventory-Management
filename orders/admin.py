from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps

# Get all models from the current app
app = apps.get_app_config('orders')  # Replace 'myapp' with your app's name

# Register all models dynamically
for model in app.get_models():
    admin.site.register(model)
