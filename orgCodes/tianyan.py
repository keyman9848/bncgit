import requests
header = {
'Host': 'www.tianyancha.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Tyc-From': 'normal',
'CheckError': 'check',
'Connection': 'keep-alive',
'Referer': 'http://www.tianyancha.com/company/22822',
'Cache-Control': 'max-age=0'
,
'Cookie': '%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgyODUxNTk1MiIsImlhdCI6MTUwMTAzNDY4MCwiZXhwIjoxNTE2NTg2NjgwfQ.WbkTKcMp_7WfPv3pkHo9lDH9BQiYQegZ9n9Vw14_MRz-x7wcMKDvcoGHOT-AVyxh5wwtg2xYgpPt6rhFWlrCKg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215828515952%2522%257D'
}
r = requests.get('https://www.tianyancha.com/company/22822', headers=header)
print(r.text)
print(r.status_code)