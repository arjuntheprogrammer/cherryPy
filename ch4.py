import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head>
                <body>
                    <form method = "get" action = "generate" >
                        <input type="text" value = "8" name="length">
                        <button type = "submit">Give it Now!</button>
                    </form>
                </body>
            </head>
        <html>"""
    
    @cherrypy.expose
    def generate(self, length = 8):
        return ''.join(random.sample(string.hexdigits, int(length)))

def main():
    cherrypy.quickstart(StringGenerator())


if __name__ == '__main__':
    main()