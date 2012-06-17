from django.contrib import admin
from servicewatch.models import Grower

class SkillInline(admin.TabularInline):
	verbose_name = 'Skill'
	model = Grower.skills.through
	extra = 0

class InterestInline(admin.TabularInline):
	verbose_name = 'Interest'
	model = Grower.interests.through
	extra = 0

class GrowerAdmin(admin.ModelAdmin):
	inlines = [ SkillInline, InterestInline ]
	exclude = [ 'skills', 'interests' ]

admin.site.register(Grower, GrowerAdmin)
