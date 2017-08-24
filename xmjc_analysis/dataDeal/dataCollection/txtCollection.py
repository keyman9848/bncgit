
import pymysql

# 打开数据库连接
db = pymysql.connect(host='172.16.143.66',port = 3306,user='kjt', passwd='kjt$',db ='kjt',charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
sql = "SELECT VERSION()"
sql1= "select * from users"
cursor.execute(sql1)


# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # 打印结果
    print (fname, lname, age, sex, income)


# 关闭数据库连接
db.close()