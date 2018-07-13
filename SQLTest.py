from pathlib import Path
import sqlite3

import gpsd
import pendulum

def insert_position(packet):

    print('Inserting initial data')

    conn.execute(
        "insert into point_of_interest (alt, climb, hspeed, lat, lon, mode, sats, sats_valid, time_btn_pushed, track) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (packet.alt, packet.climb, packet.hspeed, packet.lat, packet.lon, packet.mode, packet.sats,
         packet.sats_valid, packet.time, packet.track))

def get_current_position(gpsd):
    # Get current GPS Data
    packet = gpsd.get_current()

    return packet

db_filename = 'PoI.db'
schema_filename = 'PoI_Schema.sql'

db_is_new = not Path.exists(Path(db_filename))

conn = sqlite3.connect(db_filename)

if db_is_new:
    print('Need to create schema')
else:
    print('Database exists, check tables and columns')

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

    else:
        print('Database exists, assume schema does, too.')

# Connect to the local gpsd
gpsd.connect()

# GPIO event/Button push here!

packet = get_current_position(gpsd)

# Error trapping for no fix yet
if packet.mode == 0 or packet.mode == 1:
    print("[!] No fix yet. Try again in a moment.")
elif packet.mode == 2:
    print("[*] 3D fix acquired.")
    insert_position(packet)
else:
    print("[*] 2D fix acquired.")
    print("[!] Not written to database because your code is bad m'kay?")
    # insert_position(packet)