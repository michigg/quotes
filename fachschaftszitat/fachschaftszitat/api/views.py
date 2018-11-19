from django.templatetags.static import static
from rest_framework import views, status, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializer import QuoteSerializer, AuthorSerializer
from fachschaftszitat.models import Quote, Author


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
        return Quote.objects.filter(owner__in=self.request.user.groups.all()).order_by('-timestamp')

    serializer_class = QuoteSerializer


class ApiGetAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
