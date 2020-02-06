from django.shortcuts import render
import random
from .models import *
import requests
from PIL import Image
from io import BytesIO
import base64

def site(request):
    if request.method == 'POST':
        nickName = request.POST.get('nickName')
        n = user(nickName = nickName)
        n.save()
        #save_session(request, nickName)
    food_id = random.randint(1,283)
    food = food_list.objects.get(pk=food_id)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content)) # Your image here!
    output = BytesIO()
    img1.save(output, format='JPEG')
    output.seek(0)
    output_s = output.read()
    b64 = base64.b64encode(output_s)
    b64 = str(b64)[2:-1]
    return render(request, 'zoom/site.html', {'b64' : b64, 'food' : food})



# def save_session(request, nickName):
#     request.session['nickName'] = nickName


def data(request):
    food_id = random.randint(1,283)
    food = food_list.objects.get(pk=food_id)
    print(food.foodName)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content))
    img1 = img1.resize((500, 400))
    output = BytesIO()
    img1.save(output, format='JPEG')
    output.seek(0)
    output_s = output.read()
    b64 = base64.b64encode(output_s)
    b64 = str(b64)[2:-1]
    return render(request, 'zoom/data.html', {'b64' : b64, 'url' : url, 'food' : food})

def score(request):
    answer = request.POST.get('answer')
    foodid = request.POST.get('foodid')
    score = request.POST.get('score')
    print(answer, foodid, score)
    food = food_list.objects.get(pk=foodid)
    if food.foodName == answer:
        score += 5
    return render(request, 'zoom/site.html', {})



def foodgame(request):
    food_id = random.randint(1,283)
    food = food_list.objects.get(pk=1)
    url = food.foodImg
    url1 = requests.get(url)
    img1 = Image.open(BytesIO(url1.content)) # Your image here!
    output = BytesIO()
    img1.save(output, format='JPEG')
    output.seek(0)
    output_s = output.read()
    b64 = base64.b64encode(output_s)
    b64 = str(b64)[2:-1]
    return render(request, 'zoom/foodgame.html', {'b64' : b64, 'food' : food})
