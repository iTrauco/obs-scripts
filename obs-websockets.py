import obswebsocket
from obswebsocket import obsws, requests, events, exceptions

# Connection settings
host = "10.0.0.225"  # The IP address of the machine running OBS WebSocket server
port = 4444          # The port you're using for OBS WebSocket
password = ""        # No password

def on_switch_scenes(message):
    print(f"Switching scenes to {message.getSceneName()}")

def main():
    ws = obsws(host, port, password)
    connected = False
    try:
        print("Connecting to OBS WebSocket...")
        ws.connect()
        connected = True
        print("Connected to OBS WebSocket.")
        
        # Register event handler
        ws.register(on_switch_scenes, events.SwitchScenes)
        
        # Example: Get the current scene
        response = ws.call(requests.GetCurrentProgramScene())
        print(f"Current scene: {response.getName()}")
        
        # Keep the connection open to listen for events
        input("Press Enter to disconnect...\n")
    except exceptions.ConnectionFailure as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connected:
            try:
                ws.disconnect()
                print("Disconnected from OBS WebSocket.")
            except Exception as e:
                print(f"An error occurred while disconnecting: {e}")

if __name__ == "__main__":
    main()

