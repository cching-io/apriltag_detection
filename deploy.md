# Local deployment

## Build and install

Clone the repository and enter it:

```bash
git clone <repository-url>
cd apriltag
```

Configure a Release build, then build and install it:

```bash
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --target install
```

The default install prefix is usually `/usr/local`. If your account cannot write
there, run the install command with the appropriate administrator privileges, or
configure CMake with a writable `CMAKE_INSTALL_PREFIX`.

## Select the camera

Before running, set the camera index in `apriltag_cc.py` to the correct device:

```python
cap = cv2.VideoCapture(0)
```

Replace `0` with the index for the desired camera. On Linux, camera device nodes
are typically `/dev/video0`, `/dev/video1`, and so on; the intended camera may
not be index `0`.

## Run

If your default Python package path is `/usr/local/lib/python3.12/dist-packages/`,
run the script with the installed package directory included in `PYTHONPATH`:

```bash
PYTHONPATH=/usr/local/lib/python3.12/site-packages python3 apriltag_cc.py
```

Adjust the Python version and package path if your installation uses different
locations.
