import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()

    # Sort asc
    sorted1 = MATCHES[match_id][0]
    sorted1.sort()

    sorted2 = MATCHES[match_id][1]
    sorted2.sort()
    
    msg = "Match found" if (is_match(sorted1, sorted2, 0, len(sorted1)-1)) else "Not found"

    end = time.time()

    return {
        "message": msg, 
        "elapsedTime": end - start,
    }, 200

#function for matching
def is_match(fave_numbers_1, fave_numbers_2, low, high):
    found = False

    for number in fave_numbers_2:
        while low <= high: # check
            mid = low + (high - low)//2

            if fave_numbers_1[mid] == number:
                print(number)
                found = True
                break

            elif fave_numbers_1[mid] < number:
                low = mid+1

            else:
                high = mid-1

        if found == False: 
            break
        
    return found
