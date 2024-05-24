import asyncio
import websockets
import json
import hashlib
import base64

# Connection settings
host = "10.0.0.225"
port = 4444
password = ""  # If no password, leave it empty
scene_name = "Master"
source_name = "Bug"

# Position settings (example positions)
positions = [
    {"x": 0.0, "y": 0.0},       # Top-left corner
    {"x": 1920.0, "y": 0.0},    # Top-right corner
    {"x": 0.0, "y": 1080.0},    # Bottom-left corner
    {"x": 1920.0, "y": 1080.0}  # Bottom-right corner
]

async def get_scene_item_id(websocket, scene_name, source_name):
    # Fetch the scene items and find the ID of the specified source
    get_scene_item_list_message = {
        "op": 6,
        "d": {
            "requestType": "GetSceneItemList",
            "requestId": "get-scene-item-list",
            "requestData": {
                "sceneName": scene_name
            }
        }
    }
    await websocket.send(json.dumps(get_scene_item_list_message))
    scene_item_list_response = await websocket.recv()
    scene_item_list_data = json.loads(scene_item_list_response)
    print(f"Scene Item List Response: {scene_item_list_data}")
    if "sceneItems" not in scene_item_list_data["d"]["responseData"]:
        print(f"Error: 'sceneItems' key not found in the response")
        return None
    for item in scene_item_list_data["d"]["responseData"]["sceneItems"]:
        if item["sourceName"] == source_name:
            return item["sceneItemId"]
    return None

async def connect_to_obs():
    uri = f"ws://{host}:{port}"
    async with websockets.connect(uri) as websocket:
        # Wait for the "Hello" message from the server
        hello_message = await websocket.recv()
        hello_data = json.loads(hello_message)
        print(f"Received Hello message: {hello_data}")

        # Send Identify message
        identify_message = {
            "op": 1,
            "d": {
                "rpcVersion": hello_data["d"]["rpcVersion"]
            }
        }

        # If authentication is required
        if hello_data["d"].get("authentication"):
            auth = hello_data["d"]["authentication"]
            secret = base64.b64encode(hashlib.sha256((password + auth["salt"]).encode('utf-8')).digest()).decode('utf-8')
            auth_response = base64.b64encode(hashlib.sha256((secret + auth["challenge"]).encode('utf-8')).digest()).decode('utf-8')
            identify_message["d"]["authentication"] = auth_response

        await websocket.send(json.dumps(identify_message))
        identify_response = await websocket.recv()
        identify_data = json.loads(identify_response)
        print(f"Received Identify response: {identify_data}")

        if identify_data["op"] != 2:
            print("Identification failed.")
            return
        print("Identified successfully.")

        # Get the scene item ID for the source
        scene_item_id = await get_scene_item_id(websocket, scene_name, source_name)
        if not scene_item_id:
            print(f"Could not find scene item ID for source '{source_name}' in scene '{scene_name}'")
            return

        # Example: Move the scene source to different positions
        for pos in positions:
            set_transform_message = {
                "op": 6,  # The request op code
                "d": {
                    "requestType": "SetSceneItemTransform",
                    "requestId": "set-transform",
                    "requestData": {
                        "sceneName": scene_name,
                        "sceneItemId": scene_item_id,
                        "sceneItemTransform": {  # This is the correct field name
                            "positionX": pos["x"],
                            "positionY": pos["y"],
                            "rotation": 0.0,
                            "scaleX": 1.0,
                            "scaleY": 1.0
                        }
                    }
                }
            }
            await websocket.send(json.dumps(set_transform_message))
            transform_response = await websocket.recv()
            transform_data = json.loads(transform_response)
            print(f"Move source response: {transform_data}")

            # Wait for a while before moving to the next position
            await asyncio.sleep(2)

        input("Press Enter to disconnect...\n")

asyncio.run(connect_to_obs())

