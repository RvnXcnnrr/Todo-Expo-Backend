from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse

class CustomAPIRoot(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({
            'tasks': reverse('task-list', request=request, format=format),
            'api-token-auth': reverse('api_token_auth', request=request, format=format),
        })
