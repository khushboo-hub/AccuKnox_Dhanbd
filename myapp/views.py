# myapp/views.py

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, UserSerializer, FriendRequestSerializer,FriendListSerializer
from django.contrib.auth import get_user_model
from .models import FriendRequest
from .serializers import PendingFriendRequestSerializer
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSearchPagination(PageNumberPagination):
    page_size = 10

class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.query_params.get('q', '').lower()
        users = User.objects.all()

        if '@' in search_query:
            users = users.filter(email__iexact=search_query)
        else:
            users = users.filter(name__icontains=search_query)

        paginator = UserSearchPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

#check the number of requests sent by the user in the last minute before allowing a new request.

class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        to_user_id = request.data.get('to_user_id')
        if to_user_id:
            try:
                to_user = User.objects.get(id=to_user_id)
                if request.user == to_user:
                    return Response({'error': 'You cannot send a friend request to yourself'},
                                    status=status.HTTP_400_BAD_REQUEST)

                # Rate limiting: Allow a maximum of 3 requests per minute
                one_minute_ago = timezone.now() - timedelta(minutes=1)
                recent_requests = FriendRequest.objects.filter(
                    from_user=request.user,
                    timestamp__gte=one_minute_ago
                ).count()

                if recent_requests >= 3:
                    return Response({'error': 'You cannot send more than 3 friend requests within a minute'},
                                    status=status.HTTP_429_TOO_MANY_REQUESTS)

                if FriendRequest.objects.filter(from_user=request.user, to_user=to_user).exists():
                    return Response({'error': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)

                friend_request = FriendRequest(from_user=request.user, to_user=to_user)
                friend_request.save()
                return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)

            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

class AcceptFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, request_id):
        try:
            friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
            friend_request.is_accepted = True
            friend_request.save()
            return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_200_OK)
        except FriendRequest.DoesNotExist:
            return Response({'error': 'Friend request not found'}, status=status.HTTP_404_NOT_FOUND)

class RejectFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, request_id):
        try:
            friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
            friend_request.delete()
            return Response({'message': 'Friend request rejected'}, status=status.HTTP_200_OK)
        except FriendRequest.DoesNotExist:
            return Response({'error': 'Friend request not found'}, status=status.HTTP_404_NOT_FOUND)

#API to list friends(list of users who have accepted friend request)
class ListFriendsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Find friend requests where the user is either the sender or receiver and is accepted
        sent_requests = FriendRequest.objects.filter(from_user=user, is_accepted=True)
        received_requests = FriendRequest.objects.filter(to_user=user, is_accepted=True)

        # Collect friend ids
        friend_ids = set(sent_requests.values_list('to_user', flat=True)) | set(
            received_requests.values_list('from_user', flat=True))

        friends = User.objects.filter(id__in=friend_ids)
        serializer = FriendListSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# myapp/views.py

class ListPendingFriendRequestsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Get all friend requests where the user is the receiver and the request is not yet accepted
        pending_requests = FriendRequest.objects.filter(to_user=user, is_accepted=False)

        serializer = PendingFriendRequestSerializer(pending_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
