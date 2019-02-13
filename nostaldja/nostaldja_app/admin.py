from django.contrib import admin
from .models import Fads
from .models import Decades

admin.site.register(Fads),
admin.site.register(Decades)
