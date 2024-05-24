import time
from obswebsocket import obsws, requests

# Connection settings
host = "10.0.0.225"
port = 4444
password = ""

# Scene and source settings
scene_name = "Master"
source_name = "4. Camera"

# Quadrant positions (x, y)
quadrants = [
    (0, 0),  # Top-left
    (960, 0),  # Top-right
    (0, 540),  # Bottom-left
    (960, 540)  # Bottom-right
]

def move_source_to_quadrant(ws, scene, source, position):
    x, y = position
    ws.call(requests.SetSceneItemProperties(source, positionX=x, positionY=y, scene_name=scene))

def main():
    ws = obsws(host, port, password)
    ws.connect()

    try:
        for pos in quadrants:
            move_source_to_quadrant(ws, scene_name, source_name, pos)
            time.sleep(2)  # Wait for 2 seconds before moving to the next quadrant
    finally:
        ws.disconnect()

if __name__ == "__main__":
    main()

