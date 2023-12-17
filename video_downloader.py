import urllib.request

import urllib3
test = urllib.request.FancyURLopener()
test.retrieve("http://www.animefun.com/dl/googDev.php?url=/108994262975881368074/Po270.flv", "testout.flv")
