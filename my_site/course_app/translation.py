from  modeltranslation.translator import register,TranslationOptions
from .models import (NetworkTeachers,NetworkStudent,Category,
                     Subcategory,Language,Course,Chapter,Lesson,
                     Assignment,Exam,Question,Option)

@register(NetworkTeachers)
class NetworkTeachersTranslationOptions(TranslationOptions):
    fields = ('network_name',)


@register(NetworkStudent)
class NetworkStudentTranslationOptions(TranslationOptions):
    fields = ('network_name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Subcategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name',)


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('language_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name','description')


@register(Chapter)
class ChapterTranslationOptions(TranslationOptions):
    fields = ('chapter_name',)


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson_name','content')



@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('assignment_name','description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('exam_name',)


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question_name',)


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option_name',)
