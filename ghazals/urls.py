from django.urls import path
from . import views
# from .views import GhazalCreateAndRead,GhazalGetUpdateDelete,DiscussionCreate,DiscussionRUD,ReactionCreate,ReactionRUD

urlpatterns = [
    path('poem/create/',views.CreatePoem.as_view()),
    path('poem/list/',views.ListPoems.as_view()),
    path('reaction/create/',views.CreateReaction.as_view()),
    path('poem/update/<int:pk>/',views.FetchUpdateDeletePoem.as_view()),
    path('poem/fetch/<int:pk>/',views.FetchUpdateDeletePoem.as_view()),
    path('poem/delete/<int:pk>/',views.FetchUpdateDeletePoem.as_view()),
]







##########################################################################################################

###LIST OF POEMS

'''{
    {
id : 8,
name : qais,
author : ghalib,
likes : 2,
love : 3,
insightful : 1,
clap : 8,
user_reaction : like,
posted_by : bhupendra jogi
}
,
{
id : 9,
name : a_qais,
author : a_ghalib,
likes : 2,py
love : 3,
insightful : 1,
clap : 8,
user_reaction : love,
posted_by : bhupendra jogi
}
}

Accessible To Everyone
'''



### Single Poem(GET)
'''
{
id : 1,
name : qais,
interpretaion : Big Text,
author : mirza ghalib,
posted_by : Divyansh,
likes : 2,
love : 3,
insightful : 1,
clap : 8,
user_reaction : likes,
posted_by : bhupendra jogi
}

ATA
'''   

### Single Poem(POST)
'''{
name : qais,
interpretaion : Big Text,
author : mirza ghalib,
posted_by : user.auth

Accessible to Authenticated Users
}'''


### Single Poem(Patch)

'''{
Update Anything()
Check is it the same person who has posted it
}'''


### Reaction On Poem(Post)
'''
{
reacted_by : auth.user,
reaction : love,
poem_id : 1
}
'''
