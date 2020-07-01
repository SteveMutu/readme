
from django.conf.urls import url

from django.urls import path, re_path
from .views import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI,Hometrial,StatisticsAPI


urlpatterns = [
    url(r'^kata/?$', Hometrial.as_view()),
	path("my-quizzes/", MyQuizListAPI.as_view()),
	path("quizzes/", QuizListAPI.as_view()),
	path("saveanswer/", SaveUsersAnswer.as_view()),
	# path(r"test/<slug>/", QuizDetailAPI.as_view()),
	# path(r"result/<slug>/", SubmitQuizAPI.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()),
	path('statistics/', StatisticsAPI.as_view()),
	
]
