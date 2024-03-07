from django.urls import path
from .views import *
urlpatterns = [
    path('home/', homepage,name="home"),
    # path('login/',login, name="login"),
    path('login/', Login_user, name='login'),
    path('searchProf/', searchProf, name="searchProf"),
    path('searchEtud/', searchEtud, name="searchEtud"),
    path('etudiants/', etudiant_list, name='etudiant_list'),
    path('students/',DisplayStudentsList, name="students_list"),
    path('prof/',prof_list, name="prof_list"),
    path('excel/', excel_view, name='excel_view'),
    path('chart/', chart_view, name='chart_view'),
    path('generatePDF/', generate_pdf, name='generate_pdf'),
    path('send-email/', send_email_Etud, name='send_email'),
    path('sendMailProf/', send_email_Prof, name='send_email_prof'),
    path('attendance/',attendance,name='attendance'),
    path('camera/',attendance_page,name='camera'),

]