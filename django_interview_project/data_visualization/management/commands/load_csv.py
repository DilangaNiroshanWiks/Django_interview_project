import pandas as pd
from django.core.management.base import BaseCommand
from data_visualization.models import School, Class, Student, AssessmentArea, Summary, Subject, Awards, Answers

class Command(BaseCommand):
    help = 'Load CSV data from multiple files into the database'

    def handle(self, *args, **kwargs):
        csv_files = [
            '/home/libert/Downloads/Interview_dataset/Ganison_dataset/Ganison_dataset_2.csv',
        ]

        for csv_file in csv_files:
            self.stdout.write(f"Loading data from {csv_file}")
            df = pd.read_csv(csv_file)

            # Use sets to track unique values
            schools = set()
            classes = set()
            students = set()
            subjects = set()
            assessment_areas = set()
            awards = set()

            summaries = []

            for index, row in df.iterrows():
                schools.add(row['school_name'])
                students.add((row['First Name'], row['Last Name']))
                classes.add(row['Class'])
                subjects.add((row['Subject'], row.get('subject_score', 0)))  # Include default score
                assessment_areas.add(row['Assessment Areas'])
                awards.add(row['award'])

                # Prepare summary data
                summaries.append({
                    'school_name': row['school_name'],
                    'sydney_participant': row['sydney_participants'],
                    'sydney_percentile': row['sydney_percentile'],
                    'assessment_area_name': row['Assessment Areas'],
                    'award_name': row['award'],
                    'class_name': row['Class'],
                    'correct_answer_percentage_per_class': row['correct_answer_percentage_per_class'],
                    'correct_answer': row['Correct Answers'],
                    'full_name': f"{row['First Name']} {row['Last Name']}",
                    'participant': row['participant'],
                    'student_score': row['student_score'],
                    'subject_name': row['Subject'],
                    'year_level_name': row['Year Level'],
                })

            # Bulk create schools
            school_objects = [School(name=name) for name in schools]
            School.objects.bulk_create(school_objects)

            # Bulk create classes
            class_objects = [Class(class_name=name) for name in classes]
            Class.objects.bulk_create(class_objects)

            # Bulk create students
            student_objects = [Student(full_name=name[0] + ' ' + name[1]) for name in students]
            Student.objects.bulk_create(student_objects)

            # Bulk create subjects
            subject_objects = [Subject(subject=name[0], subject_score=name[1]) for name in subjects]
            Subject.objects.bulk_create(subject_objects)

            # Bulk create assessment areas
            assessment_area_objects = [AssessmentArea(name=name) for name in assessment_areas]
            AssessmentArea.objects.bulk_create(assessment_area_objects)

            # Bulk create awards
            award_objects = [Awards(name=name) for name in awards]
            Awards.objects.bulk_create(award_objects)

            # Prepare for summaries
            schools_map = {school.name: school for school in School.objects.all()}
            classes_map = {class_obj.class_name: class_obj for class_obj in Class.objects.all()}
            students_map = {student.full_name: student for student in Student.objects.all()}
            subjects_map = {subject.subject: subject for subject in Subject.objects.all()}
            assessment_areas_map = {area.name: area for area in AssessmentArea.objects.all()}
            awards_map = {award.name: award for award in Awards.objects.all()}

            # Create summary objects
            summary_objects = []
            for summary in summaries:
                summary_objects.append(Summary(
                    school=schools_map[summary['school_name']],
                    sydney_participant=summary['sydney_participant'],
                    sydney_percentile=summary['sydney_percentile'],
                    assessment_area=assessment_areas_map[summary['assessment_area_name']],
                    award=awards_map[summary['award_name']],
                    class_name=classes_map[summary['class_name']],
                    correct_answer_percentage_per_class=summary['correct_answer_percentage_per_class'],
                    correct_answer=None,  # You may need to handle this based on your logic
                    student=students_map[summary['full_name']],
                    participant=summary['participant'],
                    student_score=summary['student_score'],
                    subject=subjects_map[summary['subject_name']],
                    year_level_name=summary['year_level_name'],
                ))

            # Bulk create all summaries at once
            Summary.objects.bulk_create(summary_objects)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully from all CSV files.'))
