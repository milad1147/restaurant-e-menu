import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler
s = socketserver.TCPServer
s.server_name = ''  # Without this it does not work
s.server_port = ''
httpd = s(("localhost", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

POST https://p108-fmfmobile.icloud.com/fmipservice/friends/10947559981/00008030-00162521227B402E/first/initClient HTTP/1.1
Host: p108-fmfmobile.icloud.com
User-Agent: Find%20My/259.4.17 CFNetwork/1331.0.7 Darwin/21.4.0
X-Apple-Realm-Support: 1.0
X-MME-CLIENT-INFO: <iPhone12,1> <iPhone OS;15.4.1;19E258> <com.apple.AuthKit/1 (com.apple.findmy/259.4.17)>
Content-Length: 517
X-Apple-AuthScheme: Forever
Connection: keep-alive
X-Apple-I-Client-Time: 2023-03-11T01:02:53Z
X-Apple-Find-API-Ver: 2.0
X-FMF-Model-Version: 1
Authorization: Basic MTA5NDc1NTk5ODE6SUFBQUFBQUFCTHdJQUFBQUFHSlVuVTBSRG1kekxtbGpiRzkxWkM1aGRYUm92UUJQRU9MaENuVzEtYklTUmVMY1U2TERreWhkZ2lISUduSmljN1RGNV8xTjlaOVJEdEVBYk1aV3R0ajlSZjNDeHR4TktDREVEOU12SmhabW5wTGI5bnV1ckw3Ym9tRk1VN2RFWWQ3Y0UtYUxWM21NY3VLM0lZdVN0VmNDNVVEdDVNaS1VZEZQYzcxUE94UTRTWVBWTTMycUJtYlpWUX5+
Accept-Language: en-US,en;q=0.9
X-Apple-I-TimeZone: GMT+3:30
X-Apple-I-MD-RINFO: 84215040
Accept: application/json
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
X-Apple-I-MD-M: 6749cXeWAjbhxZrCNtsNkXuBYOWL/Wu6pHDYhtD1DN+jv6q4Pb+DTo4J0UsXwBoRQLhjbGJ2AdOlgj5m
X-Apple-I-Locale: en_IR@calendar=gregorian
X-Apple-I-MD: AAAABQAAABD9LTiYhS1Vql3yUsc57Y/OAAAAAw==

{"dataContext":{},"clientContext":{"countryCode":"IR","appPushModeAllowed":true,"deviceUDID":"00008030-00162521227B402E","osVersion":"15.4.1","productType":"iPhone12,1","apsToken":"139BF830BD09BEB14398EFACC488565619DB25F023E7EB7228842C823533F923","currentTime":700189373584.68298,"deviceClass":"iPhone","regionCode":"IR","osBuild":"19E258","deviceSKU":"ZA","limitedPrecision":true,"appVersion":"7.0","liveSessionStatistics":{},"legacyFallbackData":{},"userInactivityTimeInMS":5000,"pushMode":true},"serverContext":{}}
