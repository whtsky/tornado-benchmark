import tornado.ioloop
import tornado.web

from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio
AsyncIOMainLoop().install()

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world")

application = tornado.web.Application([
	(r"/", MainHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	asyncio.get_event_loop().run_forever()
