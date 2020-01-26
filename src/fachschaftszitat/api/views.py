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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator.id != self.request.user.id:
            return Response("Wrong user. Cannot delete Quote, because you are not the creator.",
                            status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


@permission_classes((IsAuthenticated,))
class ApiGifs(generics.ListCreateAPIView):
    serializer_class = GifSerializer

    def get_queryset(self):
        return Gif.objects.filter(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = GifSerializer(data=request.data)
        if serializer.is_valid():
            # YOUR CODE HERE
            serializer.creator = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def registration_gif(request):
#     if request.method == 'POST':
#         form = GifForm(request.POST)
#         if form.is_valid():
#             gif = form.save(commit=False)
#             gif.creator = request.user
#             gif.save()
#             return JsonResponse({'url': get_random_sucess_url()}, status=201)
#         return JsonResponse({'url': get_random_error_url()}, status=400)
#     else:
#         gifs = Gif.objects.filter(creator=request.user)
#         form = GifForm()
#     return render(request, 'gif.jinja2', {"form": form, "gifs": gifs})

class ApiGetAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
