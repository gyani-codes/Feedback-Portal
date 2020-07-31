# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import Max, Min, Avg
from django.contrib.auth.models import User

#Course class used for storing course in the database
# ltp in the Course stands for credits for the course 
class Course(models.Model):
    course_code = models.CharField(max_length=20,primary_key=True,blank=False)
    course_name = models.CharField(max_length=40,blank=False)
    semester = models.PositiveIntegerField(validators=[MaxValueValidator(10)],default=1)
    department = models.CharField(max_length=3,choices=(('IT','IT'),('ECE','ECE')),default='IT')
    ltp = models.PositiveIntegerField(validators=[MaxValueValidator(333)],blank=False)

    def __str__(self):
        return self.course_code

#Class Teacher is one of the user of our project
class Teacher(models.Model):
    #Teacher is user, becuase it will login and logout of the system
    user = models.OneToOneField(User)
    fac_code = models.CharField(primary_key=True,max_length=5,blank=False)
    first_name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20,blank=False)
    designation = models.CharField(max_length=20,blank=False)
    department = models.CharField(max_length=3,choices=(('IT','IT'),('ECE','ECE')),default='IT')
    #TODO://
    # What is the use of related_name
    courses = models.ManyToManyField(Course,blank=False,related_name='course_teacher')


    def __str__(self):
        return self.fac_code

    #return the max, min and average rating for each feedback criteria of Teacher
    def get_max_field1(self):
        return self.fac_codes.all().aggregate(Max('skills')).get('skills__max')

    def get_avg_field1(self):
        return self.fac_codes.all().aggregate(Avg('skills')).get('skills__avg')

    def get_min_field1(self):
        return self.fac_codes.all().aggregate(Min('skills')).get('skills__min')

    def get_max_field2(self):
        return self.fac_codes.all().aggregate(Max('knowledge')).get('knowledge__max')

    def get_avg_field2(self):
        return self.fac_codes.all().aggregate(Avg('knowledge')).get('knowledge__avg')

    def get_min_field2(self):
        return self.fac_codes.all().aggregate(Min('knowledge')).get('knowledge__min')

    def get_max_field3(self):
        return self.fac_codes.all().aggregate(Max('interactivity')).get('interactivity__max')

    def get_avg_field3(self):
        return self.fac_codes.all().aggregate(Avg('interactivity')).get('interactivity__avg')

    def get_min_field3(self):
        return self.fac_codes.all().aggregate(Min('interactivity')).get('interactivity__min')


#Student class is one of the user of our Portal which gives feedback to our teachers
class Student(models.Model):
    user = models.OneToOneField(User,related_name='student')
    first_name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20,blank=False)
    semester = models.PositiveIntegerField(validators=[MaxValueValidator(10)],blank=False)
    department = models.CharField(max_length=3,choices=(('IT','IT'),('ECE','ECE')),default='IT')

    def __str__(self):
        return self.user.username

#This the feedback course which is going to be stored in the database    
class Feedback(models.Model):
    #TODO:://
    # 1) Autofield
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE,blank=False)
    feedback_id = models.AutoField(primary_key=True,blank=False)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='fac_codes',blank=False)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course_codes',blank=False)
    skills = models.PositiveIntegerField(validators=[MaxValueValidator(5)],default=1)
    knowledge = models.PositiveIntegerField(validators=[MaxValueValidator(5)],default=1)
    interactivity = models.PositiveIntegerField(validators=[MaxValueValidator(5)],default=1)
    review = models.TextField(blank=False)

    def __str__(self):
        return str(self.feedback_id)