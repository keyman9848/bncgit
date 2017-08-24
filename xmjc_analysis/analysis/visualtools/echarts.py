from django.shortcuts import render
from analysis.models import User
import json
from django.core import serializers


def xmksh(request):
    lnav="项目可视化测试" # 可视化主题
    lcontent = "这里是可视化主题的描述->可视化测试" # 可视化主题的描述

    # data = eval(serializers.serialize("json", User.objects.all())) # json
    # userdata = json.dumps(data)
    # userdata = serializers.serialize("json", User.objects.all()) # json
    #
    userdata = User.objects.using('default').all()
    return render(request,'visual/ksh.html',{'lnav': lnav,'lcontent':lcontent,'data':userdata})