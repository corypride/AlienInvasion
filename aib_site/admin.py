from django.contrib import admin
from .models import Ship
from .models import Battlesite
from .models import Bullet
from .models import Invader
from .models import Score

# Register your models here.
admin.site.register(Ship)
admin.site.register(Battlesite)
admin.site.register(Bullet)
admin.site.register(Invader)
admin.site.register(Score)
