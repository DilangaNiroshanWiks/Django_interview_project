from django.db import models

# School Table
class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Class Table
class Class(models.Model):
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.class_name

# Assessment Areas Table
class AssessmentArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Awards Table
class Awards(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Subject Table
class Subject(models.Model):
    subject = models.CharField(max_length=255)
    subject_score = models.FloatField()

    def __str__(self):
        return self.subject

# Student Table
class Student(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name  # Corrected from fullname to full_name

# Answers Table
class Answers(models.Model):
    answer = models.TextField()

    def __str__(self):
        return self.answer

# Summary Table
class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2)
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.IntegerField()
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=255)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    correct_answer_id = models.IntegerField()

    def __str__(self):
        return f"Summary for {self.school.name}, Student: {self.student.full_name}"  # Corrected from fullname to full_name
