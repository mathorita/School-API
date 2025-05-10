from django.contrib import admin
from school.models import Student,Course,Enrollment

class Students(admin.ModelAdmin):
    list_display = ('id','name','email','cpf_id','date_of_birth','phone_number')
    list_display_links = ('id','name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Student,Students)

class Courses(admin.ModelAdmin):
    list_display = ('id','code','description')
    list_display_links = ('id','code',)
    list_per_page = 20
    search_fields = ('code',)

admin.site.register(Course, Courses)

class Enrollments(admin.ModelAdmin):
    list_display = ('id','student','course','shift')
    list_display_links = ('id',)

admin.site.register(Enrollment,Enrollments)