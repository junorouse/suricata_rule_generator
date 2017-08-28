from urlparse import urlparse

# have to fix
def make_dns_rule(hostname):
    global count
    rule = 'alert dns any any -> any any (msg:"juno\'s dns block {} rule"; content:"{}"; sid:{}; rev:1;)\n'.format(
        hostname, hostname, count
        )

    count += 1
    return rule

def make_http_rule(hostname):
    global count
    rule = 'alert tcp any any -> any 80 (msg:"juno\'s http block {} rule"; content:"Host: {}"; sid:{}; rev:1;)\n'.format(
        hostname, hostname, count
        )

    count += 1
    return rule

urls = '''http://hitomi.la
http://kass.org.kp/
http://kcna.kp/
http://kitribob.wiki/wiki/
http://ks8282.com/
http://linoit.com/users/men1212/canvases/19%EA%B8%88%20
http://naevr.com/
http://named.com/game/ladder/v2_index.php
http://naver6.com
http://onaratv.com/
http://pornpros.com
http://rodong.rep.kp/
http://snoopspy.com/download
http://test.gilgil.net/streaming/test.mp4
http://uriminzokkiri.com
http://www.4shared.com
http://www.bamwar25.com/
http://www.faa25.com/
http://www.ilbe.com/ilbe
http://www.kimmadam.net/
http://www.minjok.com
http://www.narutoxxx.com
http://www.naver.cm
http://www.ryomyong.com
http://www.sedisk.com
http://www.sk386.com/
http://www.tcosc.net/
http://www.torenzoa.net
http://www.umj262.com/
http://www.uriminzokkiri.com
http://www.uriminzokkiri.com/
http://www.winclub88.net/my/4D.html
https://graphgame.net/
https://mujige53770.wixsite.com
https://sex.com
https://torrenthaja.com
https://torrentkim10.net
https://webtoon.bamtoki.com/
https://www.facebook.com/profile.php?id=100019007882633
https://www.mtbucks.com
https://www.opioids.com/offshorepharmacy/index.html
https://www.phishtank.com/
https://yobit.net/en/dice/'''.split("\n")

count = 10000

data = ""

for url in urls:
    parse_data = urlparse(url)
    if parse_data.scheme == 'http':
        data += make_http_rule(parse_data.hostname)
    elif parse_data.scheme == 'https':
        data += make_dns_rule(parse_data.hostname)
    else:
        print "Can not find url's scheme"
        continue

print data
