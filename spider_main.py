# _*_ coding: utf-8 _*_
# 三个处理模块
import html_download # 用于下载源码，考虑js
import html_parser # 用于解析源码，关键字处理
import message_output # 输出数据
import argparse
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderMain(object):
    def __init__(self):
        self.download = html_download.HtmlDownloader()
        self.parser = html_parser.parser()
        self.output = message_output.output()

    def get_parameter(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-r", "--root", nargs='+',help="start url", required=True)
        parser.add_argument("-k", "--keywords", help="the words you want find", nargs='+', required=True)
        parser.add_argument("-d", "--depth", type=int, help="the depth", default=1, )
        args = parser.parse_args()
        root_url = args.root
        keywords = args.keywords
        depth = args.depth

        return root_url, keywords, depth

    def crawl(self, urls, keywords, depth, curDepth):
        for url in urls:
            if url in root_url and curDepth != depth:
                continue
            if depth != 0: # 深度达到则回溯
                html_source = self.download.download(url)
                urls, key_message = self.parser.parse(url, html_source, keywords)
                print urls
                key_message = json.dumps(key_message, encoding="UTF-8", ensure_ascii=False)
                print key_message
                # self.output.output(key_message)
                self.crawl(urls, keywords, depth - 1, curDepth)
            else:
                return

    def main(self, root_url, keywords, depth, curDepth):
        # urls = [root_url] # 把 root_url 处理成列表
        self.crawl(root_url, keywords, depth, curDepth)

if __name__ == "__main__":
    obj_spider = SpiderMain()
    # root_url, keywords, depth = obj_spider.get_parameter()
    root_url = ["http://www.chinanews.com/"]
    keywords = ["台湾","历史"]
    depth = 1
    curDepth = depth

    obj_spider.main(root_url, keywords, depth, curDepth) # url（域名 网站地址）、关键字、深度，由用户提供；注意点：url要处理成可访问的