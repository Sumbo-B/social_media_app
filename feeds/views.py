from django.shortcuts import render
from .models import Feeds
from rest_framework import generics
from .serializers import simple_feed_ser


class UserList(generics.ListAPIView):
    queryset = Feeds.objects.all()
    serializer_class = simple_feed_ser


# Create your views here.




# def home_views (request, *args, **kwargs):
#     print(args, kwargs)
#     return HttpResponse("<h1>Hello</h1>")

# def feed_detail_views (request, feed_id, *args, **kwargs):
#     try:
#         obj = Feeds.objects.get(id=feed_id)
#     except:
#         raise Http404
#     return HttpResponse(f"<h1>Hello {feed_id} - {obj.content}</h1>")

  
