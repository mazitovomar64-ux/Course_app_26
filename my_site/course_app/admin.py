from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin,TranslationInlineModelAdmin

class SubcategoryInline(admin.TabularInline,TranslationInlineModelAdmin):
    model = Subcategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [SubcategoryInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    inlines = [OptionInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Language,Course,Chapter,Lesson,
                Assignment,Exam)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class NetworkTeachersInline(admin.TabularInline,TranslationInlineModelAdmin):
    model = NetworkTeachers
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    inlines = [NetworkTeachersInline]


class NetworkStudentInline(admin.TabularInline,TranslationInlineModelAdmin):
    model = NetworkStudent
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [NetworkStudentInline]


admin.site.register(UserProfile)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(ReviewLike)

