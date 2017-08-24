from django.shortcuts import render

# Create your views here.
def index(request):
    '''项目统计分析平台主页'''
    return render(request,'xmjc/index.html') # 首页

def xmjf(request):
    lnav="项目经费统计" # 可视化主题
    lcontent = "这里是可视化主题的描述->项目经费统计" # 可视化主题的描述

    data=[{"value": 55, "name": '优先55'},
         {"value": 70,  "name": '普通70'},
         {"value": 25,  "name": "紧急25"}]
    data1 = [{"keys":"衬衫", "values":5},
            {"keys":"羊毛衫", "values":20},
            {"keys":"雪纺衫", "values":36},
            {"keys":"裤子", "values":10},
            {"keys":"高跟鞋", "values":10},
            {"keys":"袜子", "values":20}]
    return render(request,'xmjc/xmjf.html',{'lnav':lnav,'lcontent':lcontent,'data':data,'data1':data1})