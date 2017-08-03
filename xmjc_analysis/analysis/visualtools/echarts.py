from django.shortcuts import render


def xmksh(request):
    lnav="项目可视化测试" # 可视化主题
    lcontent = "这里是可视化主题的描述->可视化测试" # 可视化主题的描述
    return render(request,'visual/ksh.html',{'lnav': lnav,'lcontent':lcontent})