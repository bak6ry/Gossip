# _*_ coding: utf-8 _*_
import urlparse
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

class parser(object):
    def __init__(self):
        self.old_urls = set()

    def cut_url(self, root_url):
        urlBlock = []
        root_url = urlparse.urlparse(root_url)
        path = root_url.path.replace("/", "", 1).split("/")
        urlBlock.append(root_url.scheme)
        urlBlock.append(root_url.netloc)
        urlBlock.extend(path)

        return urlBlock

    def get_Link(self, urlBlock):
        fullUrl = urlBlock[0]
        for block in urlBlock[0:]:
            block += "/"
            fullUrl += block
        return fullUrl

    def url_clean(self, urlBlock ,url):
        key = urlBlock[1].split(".")[-2]

        if "javascript" in url:
            return None

        # 筛选出内链，前4种情况均为相对路径
        if url.startswith("//"):
            url = "http:" + url
        elif url.startswith("/"):
            urlBlock = urlBlock[0:2] + url.replace("/", "", 1).split("/")
            url = self.get_Link(urlBlock)
        elif url.startswith("./"):
            urlBlock[-1] = url.replace("./", "")
            url = self.get_Link(urlBlock)
        elif url.startswith("../"):
            count = url.count("../")
            for i in range(0,count):
                urlBlock.pop()
            urlBlock.extend(url.replace("../", "").split("/"))
            url = self.get_Link(urlBlock)
        # 如果不是相对路径，那就可能是“http”、“www”、…… 开头
        # 加上"http://"再进行判断
        elif url.startswith("http://"):
            if "." + key + "." in urlparse.urlparse(url).netloc:
                url = url
        else:
            url = "http://" + url
            if "." + key + "." in urlparse.urlparse(url).netloc:
                url = url

        if url in self.old_urls: # 如果是已收集的 url 则返回None
            return None

        return url

    def get_new_urls(self, urlBlock, html_source):
        cur_urls = set()
        urls = html_source.findAll("a", attrs={"href": True})

        for url in urls:
            url = self.url_clean(urlBlock, url["href"])
            if url is None:
                continue
            else:
                self.old_urls.add(url)
                cur_urls.add(url)

        return cur_urls

    def match_rule(self, keywords):
        rule = '^'
        for keyword in keywords:
            rule += "(?=.*?%s)" % (keyword)
        rule += '.+$'

        return rule

    def get_key_message(self, html_sourc, keywords):
        key_message = []
        rule = self.match_rule(keywords)
        # pLabel = html_sourc.findAll("p")
        aLabel = html_sourc.findAll("a")
        # for p in pLabel:
        #     msg = re.compile(rule).findall(p.get_text())
        #     if msg:
        #         key_message.extend(msg)
        for a in aLabel:
            serch = re.compile(rule)
            wenben = a.get_text().encode('utf-8')
            msg = serch.findall(wenben)
            print type(wenben)
            print wenben
            if msg:
                key_message.extend(msg)

        return key_message


    def parse(self, root_url, html_source, keywords):
        urlBlock = self.cut_url(root_url)
        new_urls = self.get_new_urls(urlBlock, html_source)
        key_message = self.get_key_message(html_source, keywords)

        return new_urls, key_message