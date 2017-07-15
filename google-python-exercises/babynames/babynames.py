#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    try:
        baby_file = open(filename[0], 'r')
        buff = baby_file.read()
        year = re.search('\d+', filename[0]).group()
        data = re.findall(r'<tr align="right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>',str(buff))
        names_dict = dict()
        for rank, boy_name, girl_name in data:
            names_dict[boy_name] = rank
            names_dict[girl_name] = rank
        lst = [year]
        for key in sorted(names_dict.iterkeys()):
            lst.append('{0} {1}'.format(key,names_dict[key]))
        summary = '\n'.join(lst) + '\n'
        sfile = filename[0]+'.summary'
        savefile = open(sfile,'w')
        savefile.write(summary)
        savefile.close()
        baby_file.close()
    except IOError as e:
        print e






def main():
    args = sys.argv[1:]
    print args
    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    #extract_names(args)





    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file

if __name__ == '__main__':
    main()
























