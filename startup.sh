#!/bin/bash
set -e
 
echo ">>> Starting Xvfb..."
Xvfb :99 -screen 0 1920x1080x24 &
 
echo ">>> Starting x11vnc..."
x11vnc -forever -nopw -shared -display :99 -rfbport 5900 &
 
echo ">>> Starting XFCE4..."
DISPLAY=:99 startxfce4 &
 
# Small delay to let XFCE load
sleep 3
 
echo ">>> Starting xfce4-terminal..."
DISPLAY=:99 xfce4-terminal &
 
echo ">>> Starting noVNC..."
websockify --web=/usr/share/novnc/ --wrap-mode=ignore 6080 localhost:5900 &
 
export DISPLAY=:99
echo ">>> Environment ready. Access GUI at: http://localhost:6080/vnc.html"
 
# -------------------------
# Run tests if available
# -------------------------
if [ -f "main.py" ]; then
    echo ">>> Running main.py ..."
    python main.py || true
elif [ -f "pytest.ini" ] || [ -d "tests" ]; then
    echo ">>> Running pytest ..."
    pytest -v || true
elif [ -d "features" ]; then
    echo ">>> Running behave ..."
    behave || true
else
    echo "⚠️ No entrypoint found (main.py / pytest / behave). Skipping tests."
fi
 
# -------------------------
# Keep container alive
# -------------------------
tail -f /dev/null
