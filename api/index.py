from http.server import BaseHTTPRequestHandler
from ._getter import get_timetable_url, Courses, Fields
import urllib.parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        field = dic.get('field')
        course = dic.get('course')
        try:
            url = get_timetable_url(Fields[field].value, Courses[course].value)
            self.send_response(302)
            self.send_header('Location', urllib.parse.quote(url, safe=':/'))
            self.end_headers()
        except:
            self.send_response(404)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            if "field" in dic and "course" in dic:
                message = "No info found for " + dic["field"] + " and " + dic["course"] + "!"
            else:
                message = "No info found!"
            self.wfile.write(message.encode())
            return