from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import User
from .serializers import RegisterSerializer
from .user_serializers import UserSerializer
from .permissions import IsAdminUserOnly


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def get(self, request):
        queryset = User.objects.all()

        # ?? Search & filters
        name = request.GET.get('name')
        email = request.GET.get('email')
        state = request.GET.get('state')
        city = request.GET.get('city')

        if name:
            queryset = queryset.filter(username__icontains=name)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if state:
            queryset = queryset.filter(state__icontains=state)
        if city:
            queryset = queryset.filter(city__icontains=city)

        # ?? Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated"})
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        user = User.objects.get(id=id)
        user.delete()
        return Response({"message": "User deleted"})
