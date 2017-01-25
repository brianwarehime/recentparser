# recentparser
Parses the recent applications and documents in the com.apple.sharedfilelist directory

Prerequisites:

`pip install binplist`

Usage:
```
> python recentparser.py
usage: recentparser.py [-h] [--docs] [--apps]

Parse the LSSharedFileList plist for Recent Items

optional arguments:
  -h, --help  show this help message and exit
  --docs      Lists Recent Documents in LSSharedFileList
  --apps      Lists Recent Applications in LSSharedFileList
 ```
 
Disclaimer:

I'm sure there are better ways to do this and this code may not be ideal, but, it works for me, so feel free to submit any issues or bugs that come up.
