from django.shortcuts import render
from .models import School, Class, AssessmentArea, Awards, Subject, Student, Answers, Summary

def index(request):
    # Fetching data from the database
    schools = School.objects.all()
    classes = Class.objects.all()
    assessment_areas = AssessmentArea.objects.all()
    awards = Awards.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()
    answers = Answers.objects.all()
    summaries = Summary.objects.all()

    # Passing data to the template
    context = {
        'schools': schools,
        'classes': classes,
        'assessment_areas': assessment_areas,
        'awards': awards,
        'subjects': subjects,
        'students': students,
        'answers': answers,
        'summaries': summaries,
    }

    return render(request, 'data_visualization/index.html', context)
