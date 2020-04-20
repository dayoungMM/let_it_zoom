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
from django.db import connection
from django.conf import settings
from django.utils import timezone




def site(request):
    current_user = -1
    if request.method == 'POST':
        nickName = request.POST.get('nickName')
        n = user(nickName = nickName,pub_date = timezone.now() )
        n.save()
        current_user = n.id
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
    rankings = user.objects.order_by('-score')
    return render(request, 'zoom/site.html', {'b64' : b64, 'food' : food, 'current_user': current_user,'rankings':rankings})


def finalscore(request):
    score = request.POST.get('score')
    current_user = int(request.POST.get('current_user'))
    usernow = user.objects.get(pk=current_user)
    usernow.score = score
    usernow.save()
    res_json = showmyrank(request, score)
    return HttpResponse(json.dumps(res_json), content_type='application/json')

def showmyrank(request, score):
    cursor = connection.cursor()
    sql = '''SELECT COUNT(*) as rank FROM user WHERE score > %s ORDER BY score DESC;''' %score
    cursor.execute(sql)
    row = cursor.fetchone()
    res_json = ({'rank' : row[0]+1})
    return res_json


def save_session(request, nickName):
    request.session['nickName'] = nickName



def data(request): #1단계
    score = int(request.POST.get('score'))
    category = request.POST.get('category')
    category_dict = {"food" : 283, "animal" : 173}
    food_id = random.randint(1,category_dict[category])
    table = category+'_list'
    food = eval('%s.objects.get(pk=food_id)' %table)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content)) # Your image here!
    img1 = img1.resize((500,400))
    center = (500/2, 400/2)
    change = 300
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
    food = food_list.objects.get(pk=foodid)
    if food.foodName == answer:
        score += 5
    return render(request, 'zoom/site.html', {})


def answer(request):
    category = request.POST.get('category')
    answer = request.POST.get('foodId')
    table = category+'_list'
    food = eval('%s.objects.get(pk=answer)' %table)
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