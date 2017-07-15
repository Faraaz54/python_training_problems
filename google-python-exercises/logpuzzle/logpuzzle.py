#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib


"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    server = re.search(r'_([\S]*)',filename).group(1)
    complete_url_list = list()
    try:
        logfile = open(filename,'r')
        readfile = re.findall(r'GET ([\S]*puzzle/a-([\S]*).jpg) HTTP',logfile.read())
        incomplete_urls = sorted(set(readfile),key=lambda read_temp: read_temp[1])
        complete_url_list = ['http://{0}{1}'.format(server,in_url[0]) for in_url in incomplete_urls]
        logfile.close()
        return complete_url_list
    except IOError as e:
        print e

  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  os.mkdir(dest_dir)
  try:
      for i in range(len(img_urls)):
          filename = os.path.join(dest_dir,'img{0}'.format(i))
          print 'retrieving...', img_urls[i]
          urllib.urlretrieve(img_urls[i],filename)
  except Exception as e:
      print e
  catch = os.system("echo . > index.html")



  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]


  img_urls = read_urls(args[0])


  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
