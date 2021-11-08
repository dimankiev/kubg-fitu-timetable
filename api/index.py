from http.server import BaseHTTPRequestHandler
from _getter import get_timetable_url

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        url = get_timetable_url()
        self.send_header('Location',url)
        self.end_headers()
        return