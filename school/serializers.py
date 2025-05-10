from rest_framework import serializers
from .models import Student,Course,Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','email','cpf_id','date_of_birth','phone_number']
    
    def validate(self,data):
        if len(data['cpf']) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos!')
        if not data['nome'].isalpha():
            raise serializers.ValidationError('O nome só pode ter letras')
        if len(data['celular']) != 13:
            raise serializers.ValidationError('O celular precisa ter 13 dígitos')
        return data
        
 
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ListEnrollmentStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    shift = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course','shift']
    def get_shift(self,obj):
        return obj.get_shift_display()
    
class ListEnrollmentCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student']
