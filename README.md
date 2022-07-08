# Third Hand


## 生成与连接后门 --ycy20090311

抱歉 由于本人英语能力较差，不得不用中文写.md 请谅解  

### Generate.py如何使用? 

Generate.py包含三个函数
```
def generate(i,src,ip_port):  #生成正反向TCP后门
def connect(ip_port):         #连接正向TCP后门
def listen(ip_port):          #接受反向TCP后门的连接
```    
generate()的使用
```
def generate(i,src,ip_port):  #生成正反向TCP后门
'''
1.当参数i为0 生成的后门脚本为反向TCP
2.当参数i为1 生成的后门脚本为正向TCP
3.参数src为生成脚本路径 例如"/home/hack.py"
4.参数ip_port为一个元组 它是这样的("ip",port)
  当参数i为0 ip_port为本机的ip与端口
  当参数i为1 ip_port为目标的ip与端口
'''
```  

## Translation --onion108

We officially support `zh_CN`, `en_US` and `ja_JP` translations. If you are interested in translating this software into other languages, just fork it, and go to the `src/thirdhand/Strings.py`, and edit the dictionary `STRINGS`. After doing that, please give us a pull request, and use `[i18n]` as the prefix of your pull request's title.  
Please translate the following text as the content of `str_third_party_warn` when translating as a third-party translator:
```
This translation is offered by a third-party translator.
The translation may be not 100% accurate.
```
