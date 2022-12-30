from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "S U P E R H E R O   A P I   I S   W O R K I N G ! "
    })
