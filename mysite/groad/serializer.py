from .models import user, alarm, review, course1Position, course2Position, course3Position, course4Position
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('gu_seq', 'gu_id', 'gu_pw')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = alarm
        fields = '__all__'

class Course1PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = course1Position
        fields = '__all__'

class Course2PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = course2Position
        fields = '__all__'

class Course3PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = course3Position
        fields = '__all__'

class Course4PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = course4Position
        fields = '__all__'