# http://beanstalkc.readthedocs.io/en/latest/tutorial.html

#!/usr/bin/python
#encoding=utf-8
import beanstalkc

beanstalk = beanstalkc.Connection(host='172.16.254.45', port=25)
beanstalk.put('hey')

job = beanstalk.reserve()
print(job.body)
job.delete()