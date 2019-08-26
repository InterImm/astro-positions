from astropy import units as u
# from functions.bodies import BODIES as _BODIES
from poliastro.twobody import Orbit

from astropy import time
import datetime

from poliastro import ephem




if __name__ == "__main__":

    from poliastro.bodies import Earth, Mars, Sun

    epoch = time.Time(datetime.datetime.now())  # UTC by default

    res = Orbit.from_body_ephem(Earth, epoch)

    print(
        res.
        )


    print("END OF GAME")