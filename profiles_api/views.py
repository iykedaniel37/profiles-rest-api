from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters



from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions




class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list off APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post,patch, put, delete)',
            'is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                
            )
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """handle patching update of an object """
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """handle deleting an object"""
        return Response({'method': 'DELETE'})




class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer



    a_viewset =[
        'Use actions (list, create, retrieve, update,partial_update)',
        'Authomatically maps to URLS usging Routers',
        'provides more functionality with less code',
    ]


    def list(self, request):
        """Handle GET request to the endpoint"""
        return Response({'message': 'Hello!', 'a_viewset': self.a_viewset})
    
    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validate.request_data.get('name')
            message = f"Hello {name}!"
            return Response({'message': message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST

            )
    def retrieve(self, request, pk=None):
        """Handle getting and object by its ID"""
        return Response({'http_method': 'GET',})
    
    def update(self, request, pk=None):
        """Handle updating and object"""
        return Response({'http_method': 'PUT',})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH',})
    
    def delete(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE',})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class =serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



    
    

        
                                       

    



