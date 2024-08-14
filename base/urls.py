from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .import views


urlpatterns = [
    path('', views.HomePageView, name='home'),
    
    path('article-details/<str:pk>/', views.ArticlePageView, name='article-details'),
    path('article/', views.ArticlePage, name='article'),
    path('create-article/', views.CreateArticlePageView, name='create-article'),
    path('delete-article/<str:pk>', views.DeleteArticlePageView, name='delete-article'),
    

    path('logout/', views.LogoutPageView, name='logout'),
    path('login/', views.LoginPageView, name='login'),
    path('signup/', views.SignupPageView, name='signup'),

    path('delete-comment/<str:pk>/', views.DeleteCommentPageView, name='delete-comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
