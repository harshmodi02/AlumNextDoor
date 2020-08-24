from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# ----------- BlogPost Model
class Post(models.Model):
    title = models.CharField(max_length = 255)
    intro = models.TextField(default="Add a 2 line summary of the blog here!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='blogimages/', max_length=255, null=True, blank=True)
    publish_date = models.DateField()
    high_priority = models.BooleanField(default=False)
    has_a_form = models.BooleanField(default=False)
    form_subject = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])



# ----------- MBA SchoolList Model
class MBASchoolList(models.Model):
    school_name = models.CharField(max_length = 255, default='')

    def __str__(self):
        return self.school_name



# ----------- MBA IndustryList Model
class MBAIndustryList(models.Model):
    # FK_school_name = models.ForeignKey(MBASchoolList, blank=False, null=False, default='', on_delete=models.CASCADE)
    FK_school_name = models.ManyToManyField(MBASchoolList)
    industry_name = models.CharField(max_length = 255, default='')

    def __str__(self):
        return self.industry_name



# ----------- MBA AlumniDetail Model
class MBAAlumniDetail(models.Model):
    name = models.CharField(max_length = 255, default='')
    # FK_school_name = models.ForeignKey(MBASchoolList, blank=False, null=False, on_delete=models.CASCADE)
    FK_school_name = models.ManyToManyField(MBASchoolList)
    FK_industry_name = models.ManyToManyField(MBAIndustryList)
    school_batch = models.CharField(max_length = 255, default='')
    pre_mba_education = models.CharField(max_length = 255, default='')
    pre_mba_job_role = models.CharField(max_length = 255, default='')
    pre_mba_job_experience = models.CharField(max_length=2, default='')
    post_mba_job_role = models.CharField(max_length = 255, default='')
    linkedin = models.CharField(max_length = 255, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=50, default='')
    long_description = models.TextField(default='')

    def __str__(self):
        return self.name



# ----------- MBA BlogSubsciberList Model
class MBABlogSubcriberList(models.Model):
    email = models.CharField(max_length=255, editable=False)

    def __str__(self):
        return self.email



# ----------- MS FutureMajor Model
class MSMajorList(models.Model):
    # FK_school_name = models.ForeignKey(MSSchoolList, blank=False, null=False, on_delete=models.CASCADE)
    # FK_school_name = models.ManyToManyField(MSSchoolList)
    major_name = models.CharField(max_length = 255, default= '')

    def __str__(self):
        return self.major_name



# ----------- MS SchoolList Model
class MSSchoolList(models.Model):
    school_name = models.CharField(max_length = 255, default='')
    FK_major_name = models.ManyToManyField(MSMajorList)

    def __str__(self):
        return self.school_name



# ----------- MS AlumniDetail Model
class MSAlumniDetail(models.Model):
    name = models.CharField(max_length = 255, default='')
    # FK_school_name = models.ForeignKey(MSSchoolList, blank=False, null=True, on_delete=models.CASCADE)
    FK_school_name = models.ManyToManyField(MSSchoolList)
    # FK_major_name = models.ForeignKey(MSMajorList, blank=False, null=False, on_delete=models.CASCADE)
    FK_major_name = models.ManyToManyField(MSMajorList)
    school_batch = models.CharField(max_length = 255, default='')
    pre_ms_education = models.CharField(max_length = 255, default='')
    pre_ms_job_role = models.CharField(max_length = 255, default='')
    pre_ms_job_experience = models.CharField(max_length=2, default='')
    post_ms_job_role = models.CharField(max_length = 255, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=50, default='')
    linkedin = models.CharField(max_length = 255, default='')
    long_description = models.TextField(default='')

    def __str__(self):
        return self.name



# ----------- MBA BlogSubsciberList Model
class MSBlogSubcriberList(models.Model):
    email = models.CharField(max_length=255, editable=False)

    def __str__(self):
        return self.email