from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'mensagem': 'API Unificada - Prevenção Escolar',
        'autenticacao': {
            'login': reverse('login', request=request, format=format),
            'register': reverse('register', request=request, format=format),
            'me': reverse('me', request=request, format=format),
            'refresh': reverse('token_refresh', request=request, format=format),
            'perfis': reverse('perfis', request=request, format=format),
        },
        'comum': {
            'categorias': reverse('categoria-list', request=request, format=format),
            'administradores': reverse('administrador-list', request=request, format=format),
        },
        'drogas': {
            'conteudos': reverse('conteudodrogas-list', request=request, format=format),
            'faqs': reverse('faqdrogas-list', request=request, format=format),
            'canais-apoio': reverse('canalapoiodrogas-list', request=request, format=format),
            'relatos': reverse('relatoanonimodrogas-list', request=request, format=format),
        },
        'saude_mental': {
            'conteudos': reverse('conteudosaudemental-list', request=request, format=format),
            'faqs': reverse('faqsaudemental-list', request=request, format=format),
            'canais-apoio': reverse('canalapoiosaudemental-list', request=request, format=format),
            'relatos': reverse('relatoanonimosaudemental-list', request=request, format=format),
        },
        'qualidade_vida': {
            'conteudos': reverse('conteudoqualidadevida-list', request=request, format=format),
            'faqs': reverse('faqqualidadevida-list', request=request, format=format),
            'canais-apoio': reverse('canalapoioqualidadevida-list', request=request, format=format),
            'relatos': reverse('relatoanonimoqualidadevida-list', request=request, format=format),
        },
    })