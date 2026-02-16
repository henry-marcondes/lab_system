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
    # home relatórios
    path("relatorios/",views.relatorios_home,name="relatorios_home"),
    # equipamentos em uso
    path("relatorios/em-uso/",views.relatorio_em_uso,name="relatorio_em_uso"),
    path("relatorios/em-uso/csv/",views.relatorio_em_uso_csv,name="relatorio_em_uso_csv"),
    path("relatorios/em-uso/excel/",views.relatorio_em_uso_excel,name="relatorio_em_uso_excel"),
    # por usuário
    path("relatorios/por-usuario/",views.relatorio_por_usuario,name="relatorio_por_usuario"),
    path("relatorios/por-usuario/csv/",views.relatorio_por_usuario_csv,name="relatorio_por_usuario_csv"),
    path("relatorios/por-usuario/excel/",views.relatorio_por_usuario_excel,name="relatorio_por_usuario_excel"),
]

