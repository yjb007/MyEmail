#!/usr/bin/env python
# encoding: utf-8

import smtplib
import os
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class myEmail(object):
    def __init__(self,options):
        self.options = options
    # options是一个字典dict
    def sendEmail(self):
        smtp_host = self.options['smtp_host']
        smtp_port = self.options['smtp_port']
        smtp_user = self.options['smtp_user']
		smtp_alias = self.options['smtp_alias']
        smtp_password = self.options['smtp_password']
        mail_to_list = self.options['mail_to_list']
        # mail_to_list = [ '14339989@qq.com','jianbo.yu@agrant.cn' ]
        content = '''
        <h1>这是一封测试邮件</h1>
        <p>邮件发送服务器:{0}</p>
        <p>邮件发送服务器端口:{1}</p>
        <p>发生警告服务器:</p>
        <p>故障服务:</p>
        <p>故障时间:{2}</p>
        '''.format(smtp_host,smtp_port,datetime.datetime.now())
        mail_content = MIMEText(content,_subtype='html',_charset='utf-8')
        #构造附件1
        file1 = 'D:\\1.txt'
        att1 = MIMEText(open('%s' %(file1,),'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=%s' %(os.path.basename(file1),)
        #这里的filename可以任意写，写什么名字，邮件中显示什么名字

        #构造附件2
        file2 = 'D:\\2.txt'
        att2 = MIMEText(open('%s' %(file2,),'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename=%s' %(os.path.basename(file2),)

        msg = MIMEMultipart()
        msg.attach(mail_content)
        msg.attach(att1)
        msg.attach(att2)
        msg['To'] = ",".join(mail_to_list)
		msg['from'] = '%s<%s>' %(smtp_alias,smtp_user)
        msg['subject'] = 'Hello World {0}   {1}'.format(os.popen("hostname").read(),datetime.datetime.now())

        server = smtplib.SMTP_SSL()
        server.connect(smtp_host,smtp_port)
        server.login(smtp_user,smtp_password)
        server.sendmail(smtp_user,mail_to_list,msg.as_string())
        # sendmail的参数需要的是一个列表
        server.quit()






