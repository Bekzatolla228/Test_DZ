from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('comment', views.comment, name='comment'),
    path('report', views.report, name='report'),
    path('Bekzatolla', views.Bekzatolla, name='Bekzatolla'),
    path('anime', views.secret, name='secret'),
    path('create', views.create, name='create'),
    path('delete/<int:post_id>', views.delete_post),
    path('update/<int:post_id>', views.update_post),
    path('comment_number/<slug:post_slug>', views.show_comment, name='comment_number'),
    path('pages', views.page, name='page'),
    path('page/<slug:post_slug>', views.page_slug, name='page_slug'),
    path('addpage/', views.addpage, name='add_page'),
    path('send/', views.send_message),
    path('send_2/', views.send_message_seccond),
]