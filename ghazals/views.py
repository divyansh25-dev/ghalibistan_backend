from django.shortcuts import render
from .models import Poem,PoemReactions
from rest_framework import generics
from .serializers import PoemSerializer,PoemReactionsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .helpers import Aggregate
# Create your views here.



class ListPoems(generics.ListAPIView):
    serializer_class = PoemSerializer
    
    def get_queryset(self):
        custom_query = """
        with reactions as (select poem_id,reaction,count(1) as react_count from ghazals_poemreactions
        group by 1,2)

        select gp.id,gp.name,gp.author
        ,reactions.reaction,reactions.react_count from ghazals_poem gp
        left join reactions 
        on reactions.poem_id = gp.id
        """

        return Poem.objects.raw(custom_query)


    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        modified_data = Aggregate().aggregate_reactions(serializer.data)
        return Response(modified_data)



class FetchUpdateDeletePoem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PoemSerializer
    queryset = Poem.objects.all()


class CreatePoem(generics.CreateAPIView):
    serializer_class = PoemSerializer
    queryset=Poem.objects.all()

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class CreateReaction(generics.CreateAPIView):
    serializer_class = PoemReactionsSerializer
    queryset = PoemReactions.objects.all()
    

    def perform_create(self,serializer):    
        instance = Poem.objects.get(id=self.request.data.get('poem_id'))
        serializer.save(poem=instance,reacted_by=self.request.user)

        




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



### Single Poem(Patch)

'''{
Update Anything()
Check is it the same person who has posted it
}'''


