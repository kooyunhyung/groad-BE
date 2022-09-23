from .models import user, alarm, qrcode, review, pedometer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('gu_seq', 'gu_id', 'gu_pw')

class PedometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedometer
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = alarm
        fields = '__all__'

class QrcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = qrcode
        fields = '__all__'
