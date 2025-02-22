from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Solution
from .serializers import SolutionSerializer, UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer


class LoginView(APIView):
    def post(self, request):
        # Implement login logic here
        email = request.data['email']
        password = request.data['password']


        user = authenticate(email=email, password=password)
        if user is None:
            raise AuthenticationFailed('Invalid credentials')
        
        token =  RefreshToken.for_user(user)

        return Response({
            "status": True,
            "message": "Login Successful",
            'access_token': str(token.access_token),
            'expires_in': '3600',
            'token_type': 'Bearer',
          })

class RegisterView(APIView):
      serializer_class = UserSerializer
      def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
