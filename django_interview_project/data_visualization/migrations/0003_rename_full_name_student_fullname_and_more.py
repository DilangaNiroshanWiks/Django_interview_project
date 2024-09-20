# Generated by Django 5.1.1 on 2024-09-20 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_visualization', '0002_auto_20240920_0531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='full_name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='subject_name',
        ),
        migrations.RenameField(
            model_name='summary',
            old_name='answer_id',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='summary',
            old_name='class_id',
            new_name='class_name',
        ),
        migrations.AddField(
            model_name='summary',
            name='award',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data_visualization.awards'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summary',
            name='category_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summary',
            name='correct_answer_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summary',
            name='participant',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summary',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data_visualization.subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='summary',
            name='correct_answer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='correct_answer_percentage_per_class',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='summary',
            name='student_score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='summary',
            name='sydney_percentile',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
