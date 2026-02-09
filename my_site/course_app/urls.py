from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, TeacherViewSet,NetworkTeachersViewSet,
                    CategoryListAPIView,CategoryDetailAPIView,SubcategoryListAPIView,SubcategoryDetailAPIView,LanguageViewSet,
                    CourseListAPIView,CourseDetailAPIView, ChapterViewSet,
                    NetworkStudentViewSet,LessonAPIView,LessonDetailAPIView, AssignmentViewSet,
                    ExamListAPIView,ExamDetailAPIView,QuestionViewSet,OptionViewSet,
                    CertificateAPIView,ReviewViewSet,ReviewLikeViewSet,CourseCreateAPIView,CourseEditAPIView,
                    RegisterView,LoginView,LogoutView)


router = routers.DefaultRouter()

router.register('users',UserProfileViewSet)
router.register('teachers',TeacherViewSet)
router.register('network_teachers',NetworkTeachersViewSet)
router.register('languages',LanguageViewSet)
router.register('chapters',ChapterViewSet)
router.register('network_students',NetworkStudentViewSet)
router.register('assignments',AssignmentViewSet)
router.register('questions',QuestionViewSet)
router.register('options',OptionViewSet)
router.register('reviews',ReviewViewSet)
router.register('review_likes',ReviewLikeViewSet)


urlpatterns = (
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('course/',CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name = 'course_detail'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', CourseEditAPIView.as_view(), name='course_edit'),
    path('lesson/', LessonAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('my_certificate/', CertificateAPIView.as_view(), name='my_certificate'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('subcategory/', SubcategoryListAPIView.as_view(), name='sub_category_list'),
    path('subcategory/<int:pk>/', SubcategoryDetailAPIView.as_view(), name='sub_category_detail'),

)
