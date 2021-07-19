from rest_framework import serializers

from .models import Account, Laptop


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only= True)

    class Meta:
        model = Account
        fields = ['id','username','email','password','password2']
        extra_kwargs = {
                'password': {'write_only': True}
        }

    def save(self):
        account = Account(email = self.validated_data['email'],
                        username = self.validated_data['username'],
                        )
        account.is_admin = True
        account.is_staff = True

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Password must match.'})
        account.set_password(password)
        account.save()
        return account