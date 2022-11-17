from rest_framework import viewsets, views
from carefi_assign.settings import SECRET_KEY

from .models import Bitcoin, CustomUser
from .serializers import BitcoinSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .paginations import CustomPagination

from rest_framework.exceptions import AuthenticationFailed
import datetime
import jwt
import requests


class BitcoinViewSet(viewsets.ModelViewSet):
    serializer_class = BitcoinSerializer
    queryset = Bitcoin.objects.all()
    pagination_class = CustomPagination

    @action(methods=['get'], detail=False)
    def fetch_bitcoin_price(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        created_by_user = CustomUser.objects.get(id=payload['id'])

        if created_by_user is None:
            raise AuthenticationFailed('Unauthenticated!')

        url = "https://api.coingecko.com/api/v3/exchange_rates"
        response = requests.request("GET", url)
        bitcoin = Bitcoin(coin_name=response.json()['rates']['btc']['name'],
                          current_price=response.json()['rates']['usd']['value'])
        bitcoin.created_by = created_by_user
        bitcoin.save()

        serializer = BitcoinSerializer(bitcoin)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def list(self, request, *args, **kwargs):
        # return Response({"message":"Hello World"}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass


class RegisterView(views.APIView):

    def post(self, request):
        print("request.data", request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Regisration Successful",
        }, status=status.HTTP_201_CREATED)


class LoginView(views.APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = CustomUser.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': "Login Successful."
        }
        return response


class LogoutView(views.APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout Successful.'
        }
        return response
