from django.contrib import admin
from .models import Module, ModulePart, QuizQuestion, QuizResult, Update


class ModulePartInline(admin.TabularInline):
    model  = ModulePart
    extra  = 3
    fields = ['order', 'title', 'content']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['order', 'title']
    ordering     = ['order']
    inlines      = [ModulePartInline]


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'module', 'correct_option']
    list_filter  = ['module']


admin.site.register(QuizResult)
admin.site.register(Update)