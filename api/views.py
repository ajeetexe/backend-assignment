from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import UserSerializers
from .models import UserModel
from django.http import Http404
from .paginations import CustomPagination



class GetUserList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    pagination_class = CustomPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name','last_name')
    ordering_fields = '__all__'



class Some(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        pass
    
    

# @api_view(['GET'])
# def get_user_list(request):
#     if request.method == 'GET':
#         paginator = PageNumberPagination()
#         paginator.page_size  = 5
#         paginator.page_size_query_param= 'limit'
#         name = request.query_params.get('name')
#         age = request.query_params.get('age')
#         # if name == None or age == None:
#         #     return
#         get_name = UserModel.objects.filter()
#         user = UserModel.objects.all()
#         filterset = UserFilter(request.GET,queryset=user)
#         print(filterset.qs.filter())
#         result_page = paginator.paginate_queryset(filterset.qs,request)
#         serializer = UserSerializers(result_page,many=True)
#         return paginator.get_paginated_response(serializer.data)





@api_view(['POST'])
def create_new_user(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_403_FORBIDDEN)



def user_object(pk):
    try:
        return UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        raise Http404

@api_view(['GET'])
def get_user_detail(request, pk):
    if request.method == 'GET':
        user = user_object(pk)
        serializer = UserSerializers(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_user(request, pk):
    if request.method == 'PUT':
        user = user_object(pk)
        serializer = UserSerializers(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def delete_user(request, pk):
    if request.method == 'DELETE':
        user = user_object(pk)
        user.delete()
        return Response(data={},status=status.HTTP_200_OK)
