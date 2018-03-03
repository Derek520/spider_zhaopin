import random
import urllib.request
def User_Agt():
    user_agent=[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt) ",
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; TUCOWS) ",
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 ) ",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) ",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG) ",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.0.3705) ",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0 ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1 ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.00 ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; TencentTraveler ) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.0 ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.50 ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; FDM) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; MathPlayer 2.0; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; {FF0C8E09-3C86-44CB-834A-B8CEEC80A1D7}; iOpus-I-M) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; i-Nav 3.0.1.0F; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040616 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; rv:1.5) Gecko/20031007 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; m18) Gecko/20010131 Netscape6/6.01 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/7.0.0 Safari/700.13 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.53 Safari/534.3 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 ",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 "
    ]
    ua = random.choice(user_agent)
    header = {"User-Agent":ua}
    return header

def use_proxy(proxy_addr,url):
    headers = User_Agt()
    # urllib.request.ProxyHandler 设置代理服务器信息
    proxy =urllib.request.ProxyHandler({'http':proxy_addr})
    # urllib.request.build_opener 创建一个自定义的openr对象
    openr =urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    # urllib.request.install_opener 创建全局默认的openr对象
    openr.addheaders = [headers]
    urllib.request.install_opener(openr)
    # 打开对应的网页读取
    data = urllib.request.urlopen(url).read()
    return data
