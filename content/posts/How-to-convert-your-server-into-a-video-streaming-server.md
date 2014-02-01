Title: How to convert your server into a video streaming server
Date: 2012-01-30 19:15:34
Category: English
Tags: video, streaming, vlc
Author: frommelmak

Dependencies:

    :::console
    apt-get install vlc-nox

File to stream:
    
    :::console
    cvlc -v file.mp4 --sout '#standard{access=http,mux=asf,dst=0.0.0.0:8080}'

Authenticated Stream to Stream (without audio)

    :::console
    cvlc -v http://x.x.x.x:pppp/test --no-sout-audio --sout-http-user foo --sout-http-pwd foopass --sout '#standard{access=http,mux=asf,dst=0.0.0.0:8080}'

More options:

    :::console
    vlc -H

More info:

[http://www.videolan.org/doc/streaming-howto/en/]()

[http://www.videolan.org/doc/streaming-howto/en/ch04.html]()
