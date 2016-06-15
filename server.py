#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import socket

import scrollphat
scrollphat.clear()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        print(settings['template_path'])

class scrollphat(tornado.web.RequestHandler):
    def get(self):
        leds= range(1,56)
        self.render("index.html", leds=leds)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
#        self.write_message("Hello World")
    def on_message(self, message):
#        print 'message received %s' % message
        action = True
        rawled=int(message)
        if rawled < 0:
            rawled=rawled*-1
            action= False

        led= rawled-1
        a= led % 11
        b= led // 11
        import scrollphat
#        scrollphat.clear()
        scrollphat.set_pixel(a,b,action)
        scrollphat.update()
#        print a
#        print b


    def on_close(self):
      print 'connection closed'



settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/scrollphat", scrollphat),
        (r'/ws', WSHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
