#!/usr/bin/env python
# encoding: utf-8

import smtplib
import os
import datetime
import time
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
        content = '''
        <h1>每日统计北京自动化报税结果统计</h1>
        <h1>发送时间:{0}</h1>
        '''.format(datetime.datetime.now())
        mail_content = MIMEText(content,_subtype='plain',_charset='utf-8')
        #构造附件
        file1 = '/scripts/mysql/baoshuitongji/{0}.csv'.format(time.strftime("%Y%m%d",time.localtime()))
        att1 = MIMEText(open('%s' %(file1,),'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=%s' %(os.path.basename(file1),)
        #这里的filename可以任意写，写什么名字，邮件中显示什么名字

        msg = MIMEMultipart()
        msg.attach(mail_content)
        msg.attach(att1)
        msg['To'] = ",".join(mail_to_list)
        msg['from'] = '%s<%s>' %(smtp_alias,smtp_user)
        msg['subject'] = '每日统计北京自动化报税结果统计 {0}'.format(datetime.datetime.now())

        server = smtplib.SMTP_SSL()
        server.connect(smtp_host,smtp_port)
        server.login(smtp_user,smtp_password)
        server.sendmail(smtp_user,mail_to_list,msg.as_string())
        # sendmail的参数需要的是一个列表
        server.quit()
