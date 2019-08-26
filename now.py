from http.server import BaseHTTPRequestHandler
import json
import debugserver
import datetime
from poliastro.bodies import Earth, Mars, Sun
from astropy import units as u
from poliastro.twobody import Orbit
from astropy import time
from poliastro import ephem

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        epoch_now = time.Time(datetime.datetime.now())

        res = {
            "earth": str(
                Orbit.from_body_ephem(Earth, epoch_now)
            ),
            "mars": str(
                Orbit.from_body_ephem(Mars, epoch_now)
            )
        }

        self.wfile.write(json.dumps(res).encode("utf-8"))

        return

if __name__ == '__main__':
    debugserver.serve(handler)