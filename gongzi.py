#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: qiantu
#qq 261767353

import  xdrlib ,sys
import xlrd
import os,time
import requests

content='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>无标题文档</title>
</head>

<body>
<table width="869" border="1">
  <tr>
    %s
  </tr>

  <tr>
    %s
  </tr>
</table>
</body>
</html>

'''

data=xlrd.open_workbook('gongzi.xlsx')
table = data.sheet_by_index(0)
title_list=[]
row_title = table.row_values(2)
for i in row_title:
    print type(i)
    title_list.append("<td>"+i+"</td>")
title=''.join(title_list).encode('utf-8')
nrows = table.nrows
for x in range(3,nrows-1,1):
    row_gongzi=table.row_values(x)
    gongzi_list=[]
    for y in row_gongzi:
        gongzi_list.append("<td>"+unicode(y).encode('utf-8')+"</td>")
    gongzi=''.join(gongzi_list)
    #print title
    #print gongzi
    html = content % (title,gongzi)
    # cmd="curl -d \"toaddr="+gongzi_list[17][4:][:-5] +"&content="+html+"&header=邮件标题\" http://192.168.2.168:11111/mail"
    # cmd = "curl -d \"toaddr=" + gongzi_list[17][4:][:-5] + "&content=" + "ceshi" + "&header=邮件标题\" http://192.168.2.168:11111/mail"
    requests.post('http://192.168.2.168:11111/mail', data={'toaddr': gongzi_list[17][4:][:-5],'content':html,'header':'邮件标题'})
    print 'sendmailok'
    time.sleep(2)





