from http.server import BaseHTTPRequestHandler
from ._getter import get_timetable_url
import urllib.parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = get_timetable_url()
        self.send_response(302)
        self.send_header('Location', urllib.parse.quote(url, safe=':/'))
        self.end_headers()