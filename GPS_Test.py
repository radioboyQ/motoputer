from pprint import pprint
import gpsd
import pendulum



def gps_str_to_local_human(gps_str):
    """
    Convert raw GPS string to local time and humanize it
    """

    dt = pendulum.parse(gps_str)

    dt = dt.in_timezone(pendulum.now().timezone_name)

    return dt


def dt_format(dt, military=True):
    """
    Format dt object to use DayName, 23:01:01 PM
    """
    if military:
        return dt.format('dddd, HH:mm:ss')
    else:
        return dt.format('dddd, hh:mm:ss A')

try:
    # Connect to the local gpsd
    gpsd.connect()
except UserWarning as e:
    print(e)


# Get gps position
packet = gpsd.get_current()

# See the inline docs for GpsResponse for the available data
# pprint(vars(packet), indent=4)

dt = gps_str_to_local_human(packet.time)

dt_formated = dt_format(dt, military=False)

print("Current time: {}".format(dt_formated))
print("Latitude: {}".format(packet.lat))
print("Longitude: {}".format(packet.lon))
print("Altitude: {}".format(packet.alt))

# 'alt': float,
# 'climb': float,
# 'hspeed': float,
# 'lat': float,
# 'lon': float,
# 'mode': int,
# 'sats': int,
# 'sats_valid': int,
# 'time': str,
# 'track': float