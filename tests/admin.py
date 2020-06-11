from django.contrib import admin

from tests.models import Test, Question 
admin.site.register(Test)
admin.site.register(Question)