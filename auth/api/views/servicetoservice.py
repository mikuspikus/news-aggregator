from django.shortcuts import render

from ..models import ServicesToken
from ..serializers.tokens import ServicesTokenSerializer

from ..authentication import ServicesAuthentication

from ..tokenauthentication.permissions import IsAuthenticatedForMethods
from ..tokenauthentication.views import TokenView

from ..base.views import BaseView


from rest_framework.views import Request, Response
import rest_framework.status as st


class ServicesTokenView(TokenView):
    token_model = ServicesToken
    token_serializer = ServicesTokenSerializer
    authentication_classes = (ServicesAuthentication,)