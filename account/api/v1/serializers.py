from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
        extra_kwargs = {'password':{'write_only':True}}

    def save(self, **kwargs):
        user = User(email=self.validated_data.get('email'),
                    username=self.validated_data.get('username')
                    )
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError(
                {
                    'password': "Password doesn't match"
                }
            )
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user
