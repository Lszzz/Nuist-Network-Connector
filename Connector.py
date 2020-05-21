import requests as req;
import re as re;
import base64

username=int(input('username: '))
initpassword=input('password: ')
domain=input('domain: ')#运营商，例如移动是CMCC；
initpassword=initpassword.encode()#base64传入的参数必须是二进制形式
password=base64.b64encode(initpassword).decode('utf-8')#提交的表单的形式是utf-8
table={
  'username':username,
  'domain':domain,#运营商
  'password':password,#密码base64编码；
  'enablemacauth':0
}
url='http://a.nuist.edu.cn/index.php/index/login'
res=req.post(url,data=table);
res.encoding='utf-8'
response=res.text.encode('utf-8').decode('unicode_escape')#python3中字符串要先手动指定其为一段编码的字节码之后才能好使用decode
print(response)
pattern='.*?"info":"(.*?)","s';#正则表达式匹配返回的json字符串；
result=re.match(pattern,response);
print(result.group(1))
