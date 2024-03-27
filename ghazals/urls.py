from django.urls import path
from .views import GhazalCreateAndRead,GhazalGetUpdateDelete,DiscussionCreate,DiscussionRUD,ReactionCreate,ReactionRUD

urlpatterns = [

    #CRUD GHAZALS
    path('create/', GhazalCreateAndRead.as_view()),
    path('',GhazalCreateAndRead.as_view()),
    path('read/<int:pk>/',GhazalGetUpdateDelete.as_view()),
    path('update/<int:pk>/',GhazalGetUpdateDelete.as_view()),
    path('delete/<int:pk>/',GhazalGetUpdateDelete.as_view()),
    
    #CRUD DISCUSSIONS
    path('discussion/',DiscussionCreate.as_view()),
    path('discussion/<int:pk>/',DiscussionRUD.as_view()),

    #CRUD REACTiONS
    path('reaction/',ReactionCreate.as_view()),
    path('reaction/<int:pk>/',ReactionRUD.as_view())
        
]