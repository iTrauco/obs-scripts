# OBS WebSocket Automation

This project provides a Python script to automate the movement of scene sources within OBS Studio using OBS WebSocket. The script allows you to move sources dynamically within specified scenes and includes functionalities for starting and stopping streaming.

## Features

- Connect to OBS WebSocket server
- Move scene sources within specified scenes
- Dynamic positioning of sources
- Start and stop streaming
- Easy configuration through a centralized config object

## Prerequisites

- OBS Studio with OBS WebSocket Plugin installed
- Python 3.6+
- Node.js (if any Node.js related functionality is added)
- [websockets](https://pypi.org/project/websockets/) Python library

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/obs-websocket-automation.git
    cd obs-websocket-automation
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```bash
    pip install websockets
    ```

4. **Ensure OBS WebSocket server is running:**

    - Open OBS Studio.
    - Go to `Tools` > `WebSocket Server Settings`.
    - Ensure `Enable WebSocket server` is checked.
    - Set the port to 4444 and note the IP address (e.g., `10.0.0.225`).
    - Leave the password field empty if no password is set.
    - Click `OK` to save the settings.

## Configuration

Modify the `config` object in `obs_websocket_automation.py` to match your OBS setup:

```python
config = {
    "host": "10.0.0.225",
    "port": 4444,
    "password": "",
    "scenes": {
        "master": {
            "name": "Master",
            "source": "Bug",
            "positions": [
                {"x": 0.0, "y": 0.0},
                {"x": 1920.0, "y": 0.0},
                {"x": 0.0, "y": 1080.0},
                {"x": 1920.0, "y": 1080.0}
            ]
        },
        "bug": {
            "name": "Bug",
            "source": "ItemInBugScene",
            "positions": [
                {"x": 100.0, "y": 100.0},
                {"x": 800.0, "y": 100.0},
                {"x": 100.0, "y": 600.0},
                {"x": 800.0, "y": 600.0}
            ]
        }
    }
}
Usage
Run the script to connect to the OBS WebSocket server and automate the movement of scene sources:

bash
Copy code
python obs_websocket_automation.py
.gitignore
The .gitignore file includes common exclusions for Python, Node.js, and other development environments. It ensures that unnecessary files are not included in the repository.

plaintext
Copy code
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.env/
.venv/

# PyCharm
.idea/

# VS Code
.vscode/

# Environments variables
.env

# Pytest
.cache/

# Jupyter Notebook
.ipynb_checkpoints

# Pyre type checker
.pyre/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyright
.pyright/

# Caches
*.log
*.pot
*.pyc
__pycache__/
.cache/
coverage/
.tox/
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
*.sql

# Logs
*.log

# MacOS
.DS_Store

# Windows
Thumbs.db

# Node.js
node_modules/
npm-debug.log
yarn-error.log
yarn-debug.log

# Bower
bower_components/

# Compiled JavaScript files
*.jsx.js
*.js.map
*.jsx.map

# TypeScript
*.tsbuildinfo
Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

Fork the repository
Create a feature branch (git checkout -b feature-name)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin feature-name)
Create a new Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.

css
Copy code

