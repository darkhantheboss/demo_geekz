# coding=utf-8
import json
import random
import requests
from collections import Counter
from django.utils.translation import pgettext
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pair
from .genom import eaGenerateUpdate


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

    def merge(self, alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf, righthalf = alist[:mid], alist[mid:]
            self.merge(lefthalf)
            self.merge(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i += 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist

    def bin(self, array, target):
        lower = 0
        upper = len(array)
        while lower < upper:
            x = lower + (upper - lower) // 2
            val = array[x]
            if target == val:
                return x
            elif target > val:
                if lower == x:
                    break
                lower = x
            elif target < val:
                upper = x
        return lower, upper

    def generate_pair(self, text):
        a = requests.get('https://google.kz')
        s = []
        for i in a:
            s.append(i)
        if set(text.split(' ')).issubset(set(s)):
            print text
        c = Counter()
        for i in text.split(' '):
            c[i] += 1
        ranking = c
        print ranking
        eaGenerateUpdate(text, 10)
        json_data = open('geekz/dict.json').read()
        data = json.loads(json_data)[random.randint(1, 11)]
        Pair.objects.create(word=data['word'], synonym=data['synonym'])
        return True

    def post(self, request, *args, **kwargs):
        url = request.data.get('url', None)
        title = request.data.get('title', None)
        text = request.data.get('text', None)
        if url and title and text:
            if self.check_head(url) and self.check_head(title):
                self.generate_pair(text)
                return Response(self.transpose_text(text), status=status.HTTP_200_OK)
            else:
                return Response(self.messages['1'], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(self.messages['2'], status=status.HTTP_400_BAD_REQUEST)
