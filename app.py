import web
import requests
import time
import json
import feed

urls = (
    '/', 'home',
    '/addFeed', 'addFeed'
)
app = web.application(urls, globals())

render = web.template.render('templates')
class home:        
    def GET(self):
        global render
        return render.index()

class addFeed:
    def POST(self):
        pass

if __name__ == "__main__":
    app.run()