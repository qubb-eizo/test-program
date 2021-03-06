from django.urls import path

from testsuite.views import LeaderBoardView, TestListView, TestRunView, StartTestView, slow_func

app_name = 'test'

urlpatterns = [
    path('', TestListView.as_view(), name='test_list'),

    path('leader_board/', LeaderBoardView.as_view(), name='leader_list'),
    path('<int:pk>/next', TestRunView.as_view(), name='next'),
    path('<int:pk>/start/', StartTestView.as_view(), name='start'),
    path('slow', slow_func, name='slow'),
]
