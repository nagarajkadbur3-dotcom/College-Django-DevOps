from django.contrib import admin
from django.urls import path, include
from Student import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("about/", views.about, name="about"),
    path("courses/", views.courses, name="courses"),
    path("team/", views.team, name="team"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("contact/", views.contact, name="contact"),
    path("404/", views.page_404, name="page_404"),

    path("students/", views.students, name="students"),

    # All student details
    path("all_students/", views.all_students, name="all_students"),

    # Newsletter
    path('newsletter/', views.newsletter_signup, name='newsletter'),

    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path('login/', views.login, name='login'),

    path('register/', views.register, name='register'),

    path('all_students/', views.all_students, name='all_students'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("student-profile/", views.student_profile, name="student_profile"),
     
]