from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(
                {"detail": serializer.errors if hasattr(serializer, "errors") else str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        groups = user.groups.values_list("name", flat=True)
        perfil = groups[0] if groups else None

        user_info = {
            "id": user.id,
            "username": getattr(user, "username", None),
            "email": getattr(user, "email", None),
            "perfil": perfil,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        }

        return Response(
            {
                "access": access_token,
                "refresh": refresh_token,
                "user": user_info,
            },
            status=status.HTTP_200_OK,
        )