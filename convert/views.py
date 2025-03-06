from django.shortcuts import render
from .models import Convert
from .serializer import ConvertSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class ConvertView(APIView):
    def post(self, request):
        num = request.data.get('number')
        to = request.data.get('to')
        if to == "kilogram":
            num = int(num) / 1000
            return Response({
                'success': num
            })
        elif to == "miligram":
            num = int(num) * 1000000
            return Response({
                'success': num
            })
        else:
            return Response({
                'error': 'it is not valid'
            })