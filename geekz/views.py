# coding=utf-8
from django.utils.translation import pgettext
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pair


class CheckView(APIView):
    permission_classes = ()
    http_method_names = ['post']

    messages = {
        '1': {'message': pgettext('This site is not safe', 'This site is not safe'),
              'message_header': ('Error'),
              'error': True},
        '2': {'message': pgettext('Error!', 'Please check data.'),
              'message_header': ('Warning'),
              'error': True}
    }

    def check_head(self, content):
        for i in Pair.objects.all().values_list('word', flat=True):
            if i in content:
                return False
            else:
                pass
        return True

    def transpose_text(self, text):
        new_text = ''
        for word in text.split(' '):
            if Pair.objects.filter(word__iexact=word):
                new_text += u' ' + Pair.objects.filter(word__iexact=word).first().synonym
            else:
                new_text += u' ' + word
        return new_text

    def post(self, request, *args, **kwargs):
        url = request.data.get('url', None)
        title = request.data.get('title', None)
        text = request.data.get('text', None)
        if url and title and text:
            if self.check_head(url) and self.check_head(title):
                return Response(self.transpose_text(text), status=status.HTTP_200_OK)
            else:
                return Response(self.messages['1'], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(self.messages['2'], status=status.HTTP_400_BAD_REQUEST)
