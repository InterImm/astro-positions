import logging
from poliastro.bodies import Earth, Mars, Sun


logging.basicConfig()
logger = logging.getLogger("astroposition.bodies")

BODIES ={
    "earth": Earth,
    "mars": Mars,
    "sun": Sun
}