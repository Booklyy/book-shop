from django.urls import path, include
from app import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView 
urlpatterns = [
    path('home/',views.homeview.as_view()),
    path('contact/',views.contactview.as_view()),
    path('insertcontact/',views.insertcontact),
    path('featured/<str:type>/',views.featuredview),
    #path('arrivals/',views.arrivalsview.as_view()),
    path('reviews/',views.reviewsview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('signup/',views.signup),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    path('bookdetail/<int:id>',views.bookdetail),
    path('faq/',views.faqview.as_view()),
    path('blog/',views.blogview),
    path('payment/',views.paymentview.as_view()),
    path('privacy/',views.privacyview.as_view()),
    path('terms/',views.termsview.as_view()),
    path('copyright/',views.copyrightview.as_view()),
    path('blogdetail/<int:id>',views.blogdetailview),
    path('Myorder/',views.Myorderview),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]
'''path('english/',views.englishview.as_view()),
    path('punjabi/',views.punjabiview.as_view()),
    path('hindi/',views.hindiview.as_view()),'''