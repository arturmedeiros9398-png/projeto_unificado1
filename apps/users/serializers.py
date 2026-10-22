from rest_framework import serializers
from .models import Usuario, Perfil


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id', 'descricao')


class UsuarioSerializer(serializers.ModelSerializer):
    perfil_descricao = serializers.CharField(source='perfil.descricao', read_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Usuario
        fields = (
            'email', 'nome', 'data_nascimento', 'perfil', 'perfil_descricao',
            'password', 'is_staff', 'is_active', 'criado_em',
        )
        extra_kwargs = {
            'perfil': {'required': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'criado_em': {'read_only': True},
        }

    def validate_perfil(self, value):
        request = self.context.get('request')
        if (
            (not request or not getattr(request.user, 'is_staff', False))
            and value.descricao == 'Administrador'
        ):
            raise serializers.ValidationError(
                'O perfil Administrador não está disponível para cadastro público.'
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        return Usuario.objects.create_user(password=password, **validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UsuarioMeSerializer(serializers.ModelSerializer):
    """Serializer enxuto para /auth/me/"""
    perfil_descricao = serializers.CharField(source='perfil.descricao', read_only=True)

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'data_nascimento', 'perfil', 'perfil_descricao', 'is_staff')
