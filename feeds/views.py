
from django.shortcuts import get_object_or_404
from .models import Feeds
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import simple_feed_ser as SimpleFeedSerializer




from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FeedListView(generics.ListAPIView):
    """API view to retrieve list of feeds with pagination."""
    queryset = Feeds.objects.all()
    serializer_class = SimpleFeedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None  # You can set a pagination class here if needed


# API view for home (example endpoint)

class HomeView(APIView):
    """API view for home endpoint."""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        """Return a welcome message."""
        return Response({"message": "Hello"}, status=status.HTTP_200_OK)


# API view for feed detail

class FeedDetailView(APIView):
    """API view to retrieve a feed by id."""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, feed_id, *args, **kwargs):
        """Retrieve a feed by its ID."""
        feed = get_object_or_404(Feeds, id=feed_id)
        serializer = SimpleFeedSerializer(feed)
        return Response(serializer.data, status=status.HTTP_200_OK)


## ...existing code...


