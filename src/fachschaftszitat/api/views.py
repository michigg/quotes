from django.urls import reverse
from rest_framework import views, status, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fachschaftszitat.models import Quote, Author, Gif
from .serializer import QuoteSerializer, AuthorSerializer, GifSerializer


@permission_classes((IsAuthenticated,))
class ApiGetLatestQuote(views.APIView):
    """
     Returns the servers default image location
    """

    def get(self, request):
        results = QuoteSerializer(Quote.objects.last(), many=False).data
        return Response(results, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
class ApiGetQuotes(generics.ListAPIView):
    def get_queryset(self):
        quotes = Quote.objects.filter(owner__in=self.request.user.groups.all()).order_by('-timestamp')
        quotes_wrapper = [
            {"id": quote.id,
             "timestamp": quote.timestamp,
             "owner": quote.owner,
             "statements": quote.statements.all(),
             "is_creator": quote.creator.id == self.request.user.id,
             "delete_url": reverse("fachschaftszitat.api:delete-quote", args=[quote.id])}
            for quote in quotes]
        return quotes_wrapper

    serializer_class = QuoteSerializer


@permission_classes((IsAuthenticated,))
class ApiRemoveQuote(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get_queryset(self):
        return Quote.objects.filter(creator=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator.id != self.request.user.id:
            return Response("Wrong user. Cannot delete Quote, because you are not the creator.",
                            status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


@permission_classes((IsAuthenticated,))
class ApiGifs(generics.ListAPIView):
    serializer_class = GifSerializer

    def get_queryset(self):
        gifs = Gif.objects.filter(creator=self.request.user)
        gifs_wrapper = [
            {"id": gif.id,
             "video_url": gif.video_url,
             "type": gif.type,
             "is_creator": gif.creator.id == self.request.user.id,
             "delete_url": reverse("fachschaftszitat.api:delete-gif", args=[gif.id])}
            for gif in gifs]
        return gifs_wrapper


@permission_classes((IsAuthenticated,))
class ApiGif(generics.DestroyAPIView):
    serializer_class = GifSerializer

    def get_queryset(self):
        return Gif.objects.filter(creator=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator.id != self.request.user.id:
            return Response("Wrong user. Cannot delete Gif, because you are not the creator.",
                            status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


class ApiGetAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
