#!/usr/bin/env python
#coding=utf8

import urllib2
import re
import time
import os
import sys

#from lxml import html as HTML

images_pat = re.compile(r'src="(.*?)[\.jpg|\.png]"')
css_pat = re.compile(r'href="(.*?)\.css"')
js_pat = re.compile(r'src="(.*?)\.js"')


def get_images(page, images_dir):
    print len(page)
    #page = HTML.fromstring(page)
    url_list = images_pat.findall(page)
    print len(url_list)    
    #print url_list    
    #url_list存在重复的images
    for url in url_list:
        url = url.strip()+'g'
        print 'download image_url\t'+url
        image_name = url.split('/')[-1]
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        image = response.read()
        f = open(images_dir+image_name, 'w')
        f.write(image)


def get_css(page, css_dir):
    css_list = css_pat.findall(page)
    #print css_list
    for url in css_list:
        url = url.strip()+'.css'
        css_name = url.split('/')[-1]
        print 'download css_url\t'+url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        css = response.read()
        f = open(css_dir+css_name, 'w')
        f.write(css)
     

def get_js(page, js_dir):
    js_list = js_pat.findall(page)
    #print js_list
    for url in js_list:
        url = url.strip()+'.js'
        print 'download js_url\t'+url
        js_name = url.split('/')[-1]
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        js = response.read()
        f = open(js_dir+js_name, 'w')
        f.write(js)
        

def main():
    
    argv_list = sys.argv 
    url = argv_list[4].strip()
    tmp_dir = argv_list[-1].strip()[1:]
    back_time = argv_list[2].strip()
    #print dir(time)
    #print url, tmp_dir, back_time
    while True: 
        timesp = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        file_dir = tmp_dir+'/'+timesp+'/'
        js_dir, css_dir, images_dir = file_dir + 'js/', file_dir + 'css/', file_dir + 'images/'
        print file_dir, js_dir, css_dir, images_dir 
        print os.getcwd()
        if not os.path.isdir(os.path.join(os.getcwd(), file_dir)):
            os.makedirs(os.path.join(os.getcwd(), file_dir))
        if not os.path.isdir(os.path.join(os.getcwd(), js_dir)):
            os.makedirs(os.path.join(os.getcwd(), js_dir))
        if not os.path.isdir(os.path.join(os.getcwd(), css_dir)):
            os.makedirs(os.path.join(os.getcwd(), css_dir))
        if not os.path.isdir(os.path.join(os.getcwd(), images_dir)):
            os.makedirs(os.path.join(os.getcwd(), images_dir))
         
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        page = response.read()
         
        f = open(os.path.join(os.path.join(os.getcwd(), file_dir), 'index.html'), 'w')
        f.write(page)
        
        '''
        with open('./index.html', 'r') as f:
            page = f.read()
        print len(page)
        '''
        
        get_images(page, images_dir)
        get_css(page, css_dir)
        get_js(page, js_dir)
        
        time.sleep(60)
    

if __name__ == '__main__':
    main()
