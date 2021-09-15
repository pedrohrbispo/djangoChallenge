from rest_framework import serializers
from articles.models import Articles, Authors, Usuario

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    class Meta:
        model = Usuario
        fields = ('username','email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = Usuario(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']

        conta.set_password(password)
        conta.save()
        return conta