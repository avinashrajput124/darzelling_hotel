from rest_framework.decorators import api_view
from rest_framework.response import Response
from ello.models import Add_Hotal
from ello.serializers import Add_hotelSerializer


# all hotel data api
@api_view(['GET'])
def hotel(request):
    if request.method == 'GET':
        data=Add_Hotal.objects.all()
        serializer=Add_hotelSerializer(data,many=True)
        print(serializer)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



