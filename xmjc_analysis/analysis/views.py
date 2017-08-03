from django.shortcuts import render

# Create your views here.
def index(request):
    '''项目统计分析平台主页'''
    return render(request,'xmjc/index.html') # 首页

def xmjf(request):
    lnav="项目经费统计" # 可视化主题
    lcontent = "这里是可视化主题的描述->项目经费统计" # 可视化主题的描述
    return render(request,'xmjc/xmjf.html',{'lnav':lnav,'lcontent':lcontent})