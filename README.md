# Third Hand

## 生成与连接后门 --ycy20090311

抱歉 由于本人英语能力较差，不得不用中文写.md 请谅解  

为Third Hand提供生成与连接后门功能的文件为Generate.py  

Generate.py包含三个函数
```
def generate(i,src,ip_port):  #生成正反向TCP后门
def connect(ip_port):         #连接正向TCP后门
def listen(ip_port):          #接受反向TCP后门的连接
```
## Translation --onion108

We officially support `zh_CN`, `en_US` and `ja_JP` translations. If you are interested in translating this software into other languages, just fork it, and go to the `src/thirdhand/Strings.py`, and edit the dictionary `STRINGS`. After doing that, please give us a pull request, and use `[i18n]` as the prefix of your pull request's title.  
Please translate the following text as the content of `str_third_party_warn` when translating as a third-party translator:
```
This translation is offered by a third-party translator.
The translation may be not 100% accurate.
```
