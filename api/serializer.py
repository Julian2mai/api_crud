from rest_framework import serializers
from .models import programmer
from .models import student

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields = ('id', 'fullname', 'nickname', 'age', 'is_active') #ejemplo largo o selectivo
        fields = '__all__' #todos los campos de la tabla
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
