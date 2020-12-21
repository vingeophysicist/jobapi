from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from jobapp.models import JobOffer
from jobapp.api.serializers import JobOfferSerializer




class JobOfferListCreateAPIView(APIView):
    
    def get(self, request):
        jobOffers = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobOffers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobOfferdetailAPIView(APIView):

    def get_object(self, pk):
        jobOffer = get_object_or_404(JobOffer, pk=pk)
        return jobOffer
    
    def get(self, request, pk):
        jobOffer = self.get_object(pk)
        serializer = JobOfferSerializer(jobOffer)
        return Response(serializer.data)
    
    def put(self,request, pk):
        jobOffer = self.get_object(pk)
        serializer = JobOfferSerializer(jobOffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        jobOffer = self.get_object(pk)
        jobOffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












