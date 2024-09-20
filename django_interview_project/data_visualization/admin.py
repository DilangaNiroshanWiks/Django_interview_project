from django.contrib import admin
from .models import School, Class, Student, AssessmentArea, Summary, Subject, Awards, Answers

# Admin setup for each model
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name')

@admin.register(AssessmentArea)
class AssessmentAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'subject_score')  

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer')

@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = (
        'school', 'sydney_participant', 'sydney_percentile', 'assessment_area', 
        'award', 'class_name', 'correct_answer_percentage_per_class', 'correct_answer', 
        'student', 'participant', 'student_score', 'subject', 'category_id', 
        'year_level_name', 'answer', 'correct_answer_id'
    )
