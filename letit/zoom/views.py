from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import random
from .models import *
import requests
from PIL import Image
from io import BytesIO
import base64
import json


def site(request):
    
    if request.method == 'POST':
        nickName = request.POST.get('nickName')
        n = user(nickName = nickName )
        n.save()
        save_session(request, nickName)
    food_id = random.randint(1,283)
    food = food_list.objects.get(pk=food_id)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content)) # Your image here!
    img1 = img1.resize((500,400))
    output = BytesIO()
    img1.save(output, format='JPEG')
    output.seek(0)
    output_s = output.read()
    b64 = base64.b64encode(output_s)
    b64 = str(b64)[2:-1]
    return render(request, 'zoom/site.html', {'b64' : b64, 'food' : food})


def save_session(request, nickName):
    request.session['nickName'] = nickName



def data(request): #1단계
    score = int(request.POST.get('score')) 
    food_id = random.randint(1,283)
    food = food_list.objects.get(pk=food_id)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content)) # Your image here!
    img1 = img1.resize((500,400))
    center = (500/2, 400/2)
    change = 1
    i_list=[ 0.5,0.339, 0.24285, 0.1785714285714286,0.14642857142857146, 0.08214285714285716, 0.05]
    if score//change >= len(i_list):
        idx = random.randint(3,len(i_list)-1)
        i = i_list[idx]
        mulnum = random.normalvariate(0.5,0.1)
        center = (500*mulnum, 400*mulnum)
    else: 
        i = i_list[score//change]
    left = center[0] - 500 * i
    top = center[1] - 400 * i
    right = center[0] + 500 * i
    bottom = center[1] + 400 * i
    area = (left, top, right, bottom)
    img1 = img1.crop(area).resize((500,400))



    output = BytesIO()
    img1.save(output, format='JPEG')
    output.seek(0)
    output_s = output.read()
    b64 = base64.b64encode(output_s)
    b64 = str(b64)[2:-1]
    f_json = ({'b64' : b64, 'foodName': food.foodName, 'foodId' : food_id}) 
    return HttpResponse(json.dumps(f_json), content_type='application/json')
    
def score(request):

    answer = request.POST.get('answer')
    foodid = request.POST.get('foodid')
    score = request.POST.get('score')

    print(answer, foodid, score)
    
    food = food_list.objects.get(pk=foodid)
    if food.foodName == answer:
        score += 5
    return render(request, 'zoom/site.html', {})


def answer(request):
    answer = request.POST.get('foodId')
    print(answer)
    food = food_list.objects.get(pk=answer)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content)) # Your image here!
    img1 = img1.resize((500,400))
    output = BytesIO()
    img1.save(output, format='JPEG')
    output.seek(0)
    output_s = output.read()
    b64 = base64.b64encode(output_s)
    b64 = str(b64)[2:-1]
    f_json = ({'b64' : b64, 'foodName': food.foodName}) 
    return HttpResponse(json.dumps(f_json), content_type='application/json')