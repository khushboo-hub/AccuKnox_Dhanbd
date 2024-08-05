# myapp/urls.py

from django.urls import path
from .views import (
    RegisterView, CustomTokenObtainPairView, UserSearchView,
    SendFriendRequestView, AcceptFriendRequestView, RejectFriendRequestView,
    ListFriendsView, ListPendingFriendRequestsView
)

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('search/', UserSearchView.as_view(), name='user_search'),
    path('friend-request/send/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('friend-request/accept/<int:request_id>/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('friend-request/reject/<int:request_id>/', RejectFriendRequestView.as_view(), name='reject_friend_request'),
    path('friends/', ListFriendsView.as_view(), name='list_friends'),
    path('pending-requests/', ListPendingFriendRequestsView.as_view(), name='list_pending_requests'),  # New URL pattern
]
