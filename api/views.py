from django.shortcuts import render,HttpResponse
import  datetime
import json
import re
# Create your views here.

def add(request):
    if request.method == "POST":
        varry = json.loads(request.body)
        print(varry)
        sum = 0
        for i in varry["value_array"]:
            sum += i["value"]
        return HttpResponse(json.dumps({"result":sum}), content_type="application/json")


def get_date(request):
    if request.method == "GET":
        today = datetime.date.today()
        r = json.dumps({'date':str(today)})
        print(r)
        return HttpResponse(r, content_type="application/json")

def chat(request):
    if request.method == "POST":
        Q = json.loads(request.body)
        pattrn = re.search("您好",Q["msg"])
        pattrn1 = re.search("再见",Q["msg"])

        if pattrn:
            res = "您好，您吃了吗？"

        if pattrn1:
            res = "回见了您内。"
        if pattrn and pattrn1:
            res = "天气不错。"
        return HttpResponse(json.dumps({"result": res}), content_type="application/json")