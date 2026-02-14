from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('usar/<int:equipamento_id>/', views.usar_equipamento, name='usar_equipamento'),
    path('devolver/<int:equipamento_id>/',views.devolver_equipamento,name='devolver_equipamento'),
    path('em-uso/', views.equipamentos_em_uso, name='equipamentos_em_uso'),
    path('historico/<int:equipamento_id>/', views.historico_equipamento, name='historico_equipamento'),
    path("equipamentos/", views.lista_equipamentos, name="lista_equipamentos"),
    path('meus_equipamentos/', views.meus_equipamentos, name='meus_equipamentos'),
    path("manutencao/<int:equipamento_id>/", views.manutencao, name="manutencao"),
    path("finalizar_manutencao/<int:equipamento_id>/", views.finalizar_manutencao, name="finalizar_manutencao"),
    path("relatorios/manutencao/",views.relatorio_manutencao,name="relatorio_manutencao"),
    path("relatorios/manutencao/csv/",views.relatorio_manutencao_csv,name="relatorio_manutencao_csv"),
    path("relatorios/manutencao/excel/",views.relatorio_manutencao_excel,name="relatorio_manutencao_excel"),

]

