# _*_ coding: utf-8 _*_
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


class HtmlDownloader(object):

    # def download(self, url):
    #     if url is None:
    #         return None
    #
    #     reponse = requests.get(url)
    #
    #     reponse.encoding = 'utf-8'
    #
    #     if reponse.status_code != 200:
    #         return None
    #
    #     soup = BeautifulSoup(reponse.text, "html.parser")
    #
    #     return soup

    def download(self, url):
        if url is None:
            return
        diver = webdriver.PhantomJS(executable_path='D:/pyscript/pypy1/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        diver.get(url)
        soup = BeautifulSoup(diver.page_source, "html.parser")

        return soup