from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def profiles(request):
    if request.method == 'GET':
        # TODO: Добавить обработку GET запроса
        JsonResponse({
            'name': 'Yeremisa NJ',
            'login': 'notojoyoo',
            'status': 'Waiting for new Minions 🤡',
            'following': '6664',
            'followers': '9991',
            'cover': 'https://images.pexels.com/photos/12345815/pexels-photo-12345815.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'avatar': 'https://images.pexels.com/photos/13075751/pexels-photo-13075751.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
        })
    else:
        return