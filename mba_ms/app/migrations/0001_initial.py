# Generated by Django 3.0.6 on 2020-07-16 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MBABlogSubcriberList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(editable=False, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MBASchoolList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MSSchoolList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField(default='Add a 2 line summary of the blog here!')),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='blogimages/')),
                ('publish_date', models.DateField()),
                ('high_priority', models.BooleanField(default=False)),
                ('has_a_form', models.BooleanField(default=False)),
                ('form_subject', models.CharField(default='', max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MSMajorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(default='', max_length=255)),
                ('FK_school_name', models.ManyToManyField(to='app.MSSchoolList')),
            ],
        ),
        migrations.CreateModel(
            name='MSAlumniDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('school_batch', models.CharField(default='', max_length=255)),
                ('pre_ms_education', models.CharField(default='', max_length=255)),
                ('pre_ms_job_role', models.CharField(default='', max_length=255)),
                ('pre_ms_job_experience', models.CharField(default='', max_length=2)),
                ('post_ms_job_role', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=50)),
                ('linkedin', models.CharField(default='', max_length=255)),
                ('long_description', models.TextField(default='')),
                ('FK_major_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MSMajorList')),
                ('FK_school_name', models.ManyToManyField(to='app.MSSchoolList')),
            ],
        ),
        migrations.CreateModel(
            name='MBAIndustryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_name', models.CharField(default='', max_length=255)),
                ('FK_school_name', models.ManyToManyField(to='app.MBASchoolList')),
            ],
        ),
        migrations.CreateModel(
            name='MBAAlumniDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('school_batch', models.CharField(default='', max_length=255)),
                ('pre_mba_education', models.CharField(default='', max_length=255)),
                ('pre_mba_job_role', models.CharField(default='', max_length=255)),
                ('pre_mba_job_experience', models.CharField(default='', max_length=2)),
                ('post_mba_job_role', models.CharField(default='', max_length=255)),
                ('linkedin', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=50)),
                ('long_description', models.TextField(default='')),
                ('FK_industry_name', models.ManyToManyField(to='app.MBAIndustryList')),
                ('FK_school_name', models.ManyToManyField(to='app.MBASchoolList')),
            ],
        ),
    ]
