# NI OSS SOURCE SNAPSHOT: instrumentstudio-screenshot-utility-python

<!--NI_OSS_SNAPSHOT repo=ni/instrumentstudio-screenshot-utility-python commit=10b3210f8add27a4cfa3e123468874265c8ce6da -->

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=.github/CODEOWNERS sha256=a42358ab6b1a1718df4a56639a293c8745d22d13616ac343bfce23aca6cb2eff bytes=74 -->
## FILE: .github/CODEOWNERS

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `.github/CODEOWNERS`
- sha256: `a42358ab6b1a1718df4a56639a293c8745d22d13616ac343bfce23aca6cb2eff`
- bytes: 74

````text
# Default code owner for \<reponame\>
benmont #replace for \<reponame\>
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7 bytes=363 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7`
- bytes: 363

````markdown
### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=CONTRIBUTING.md sha256=288209ce5ce6df686db1d79483d121dfca212385e93b427785dd300f71a84fe1 bytes=2996 -->
## FILE: CONTRIBUTING.md

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `CONTRIBUTING.md`
- sha256: `288209ce5ce6df686db1d79483d121dfca212385e93b427785dd300f71a84fe1`
- bytes: 2996

````markdown
# Contributing to instrumentstudio-screenshot-utility

Contributions to instrumentstudio-screenshot-utility are welcome from all!

instrumentstudio-screenshot-utility is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/<reponame>/).

instrumentstudio-screenshot-utility follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

Please remember to sign off your commits (e.g., by using `git commit -s` if you
are using the command line client). This amends your git commit message with a line
of the form `Signed-off-by: Name Lastname <name.lastmail@emailaddress.com>`. Please
include all authors of any given commit into the commit message with a
`Signed-off-by` line. This indicates that you have read and signed the Developer
Certificate of Origin (see below) and are able to legally submit your code to
this repository.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

## 📝 Making a Code Contribution 📝

All code contributions should be in the form of [Pull Requests](https://guides.github.com/activities/forking/).

Please follow these steps to have your contribution considered by the maintainers:

1. Follow the styleguide
1. After you submit your pull request, verify that all status checks are passing

# Developer Certificate of Origin (DCO)

   Developer's Certificate of Origin 1.1

   By making a contribution to this project, I certify that:

   (a) The contribution was created in whole or in part by me and I
       have the right to submit it under the open source license
       indicated in the file; or

   (b) The contribution is based upon previous work that, to the best
       of my knowledge, is covered under an appropriate open source
       license and I have the right under that license to submit that
       work with modifications, whether created in whole or in part
       by me, under the same open source license (unless I am
       permitted to submit under a different license), as indicated
       in the file; or

   (c) The contribution was provided directly to me by some other
       person who certified (a), (b) or (c) and I have not modified
       it.

   (d) I understand and agree that this project and the contribution
       are public and that a record of the contribution (including all
       personal information I submit with it, including my sign-off) is
       maintained indefinitely and may be redistributed consistent with
       this project or the open source license(s) involved.

(taken from [developercertificate.org](https://developercertificate.org/))

See [LICENSE](https://github.com/ni/<reponame>/blob/main/LICENSE)
for details about how \<reponame\> is licensed.
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=LICENSE sha256=01dbc90e2165efb0106c29fc75ee00e94ad2087d8479e5e63dcc2f81ea17bb71 bytes=1091 -->
## FILE: LICENSE

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `LICENSE`
- sha256: `01dbc90e2165efb0106c29fc75ee00e94ad2087d8479e5e63dcc2f81ea17bb71`
- bytes: 1091

````text
Copyright (c) 2026, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=README.md sha256=4479dde80dde3d0394c756b1239250d06ad2d7a8846ab8f2d52578c43d631018 bytes=5914 -->
## FILE: README.md

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `README.md`
- sha256: `4479dde80dde3d0394c756b1239250d06ad2d7a8846ab8f2d52578c43d631018`
- bytes: 5914

````markdown
# InstrumentStudio Screenshot Utility (Python)

## Overview

The InstrumentStudio Screenshot Utility captures the rendered content of an active **NI InstrumentStudio** window using Windows GDI APIs.

It uses the Windows `PrintWindow` API to capture the actual rendered window content — even if the window is:

- Minimized  
- Behind other windows  

The utility automatically removes black borders and saves a clean image file.

It is intended for automated validation and reporting workflows where visual documentation of instrument configuration or measurement results is required.

It can be invoked from:

- Python scripts  
- NI TestStand  
- LabVIEW (via Python Node)  
- Any application capable of running Python  

---

## Features

- Uses Windows `PrintWindow` (with fallback to `BitBlt`)
- Works with minimized or background windows
- Automatically removes black borders
- Supports multiple image formats
- Automatically creates output directories
- Optional timestamp appended to filename
- Minimal dependencies (`ctypes`, `Pillow`)

---

## System Requirements

- Windows operating system  
- NI InstrumentStudio installed  
- Python 3.8 or later  
- Pillow library  

Install dependency:

```bash
pip install pillow
```

---

## Prerequisites

Before running the utility:

- InstrumentStudio must already be launched  
- Required Soft Front Panel (SFP) must be open  
- The SFP must be fully loaded and stable  
- InstrumentStudio must not be starting up or shutting down  

> **Note:**  
> The utility does not launch InstrumentStudio or configure instruments.  
> It captures the current visual state of an already running session.

---

# Function API

```python
capture_instrument_studio(output_dir, base_filename, add_timestamp=True)
```

## Parameters

| Parameter       | Type  | Description |
|-----------------|-------|-------------|
| `output_dir`    | str   | Directory where the screenshot will be saved |
| `base_filename` | str   | Base filename including extension (e.g., `image.png`) |
| `add_timestamp` | bool  | If `True`, appends timestamp before extension |

## Returns

```python
(success: bool, message: str)
```

- `success` → `True` if capture succeeded  
- `message` → Status or error description  

---

# Basic Usage (Python)

## Example Script (`example.py`)

```python
from screenshot_utility import capture_instrument_studio

# Specify folder and base filename (including extension)
output_folder = r"C:\Temp"
base_filename = "InstrStudio_screenshot.png"

# Capture (timestamp appended by default)
success, message = capture_instrument_studio(output_folder, base_filename)

if success:
    print(f"\n✅ {message}")
else:
    print(f"\n❌ {message}")
```

## Run

```bash
python example.py
```

Example output file:

```
C:\Temp\InstrStudio_screenshot_03Mar2026_184530.png
```

---

# Timestamp Behavior

If `add_timestamp=True` (default):

```
InstrStudio_screenshot_03Mar2026_184530.png
```

If `add_timestamp=False`:

```
InstrStudio_screenshot.png
```

---

# Supported Output Formats

The file extension determines image format.

Supported formats:

- `.png`
- `.jpg`
- `.jpeg`
- `.bmp`
- `.gif`

If an unsupported format is provided, the function returns an error.

---

# Automatic Directory Creation

- If `output_dir` does not exist, it is automatically created.
- Nested folders are supported.

Example:

```python
output_folder = r"C:\Reports\Run1\Screenshots"
```

The full folder structure will be created automatically.

---

# Running from NI TestStand

The utility can be integrated with NI TestStand using either System Exec or Python Adapter.

---

## Option 1 – System Exec Step

1. Insert a **System Exec** step.
2. Configure:

**Executable**
```
python
```

**Arguments**
```
"C:\Path\example.py"
```

Ensure:
- Python is in system PATH  
- Pillow is installed in that Python environment  

---

## Option 2 – Python Adapter (Recommended)

### Configure Python Adapter

1. Navigate to:
```
Configure → Adapters → Python
```
2. Select the correct Python environment.

### Add Python Action Step

1. Insert **Python Action** step  
2. Select:
   - Module: `screenshot_utility`
   - Function: `capture_instrument_studio`

3. Provide parameters:

```
output_dir: "C:\\Temp"
base_filename: "TS_Screenshot.png"
add_timestamp: True
```

### Return Values

The function returns:

```
(success: bool, message: str)
```

You may:
- Use `success` to determine pass/fail behavior  
- Log `message` into TestStand results  

---

# How It Works (Internally)

The utility performs:

1. Enumerates visible Windows  
2. Finds InstrumentStudio by partial title match  
3. Restores window if minimized  
4. Retrieves window dimensions  
5. Captures content using `PrintWindow`  
6. Falls back to `BitBlt` if necessary  
7. Extracts bitmap using `GetDIBits`  
8. Converts to PIL Image  
9. Automatically removes black borders  
10. Saves image to disk  

---

# Known Limitations

- Works only on Windows  
- Window must exist in active user session  
- Hardware-accelerated UI elements may render differently  
- In multi-monitor systems, consistent DPI scaling is recommended  
- Window title must contain `"InstrumentStudio"`  

---

# Typical Automation Workflow

1. Launch NI InstrumentStudio  
2. Open required Soft Front Panels  
3. Configure instrument settings  
4. Execute measurement  
5. Invoke screenshot utility  
6. Archive image for validation or reporting  

---

# Example Project Structure

```
project/
│
├── screenshot_utility.py
├── example.py
└── README.md
```

---

# Author / Team

Add team or ownership details here.
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=SECURITY.md sha256=902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11 bytes=1330 -->
## FILE: SECURITY.md

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `SECURITY.md`
- sha256: `902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11`
- bytes: 1330

````markdown
<!-- Begin NI SECURITY.md V1.0 -->

# Security

NI views the security of our software products as an important part of our commitment to our users.  This includes source code repositories managed through the [NI](https://github.com/ni) GitHub organization.

## Reporting Security Issues

We encourage you to report security vulnerabilities to us privately so we can follow the principle of [Coordinated Vulnerability Disclosure (CVD)](https://vuls.cert.org/confluence/display/CVD).  This allows us time to thoroughly investigate security issues and publicly disclose them when appropriate.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them by sending an email to [security@ni.com](mailto:security@ni.com) with sufficient details about the type of issue, the impact of the issue, and how to reproduce the issue.  You may use the [NI PGP key](https://www.ni.com/en/support/security/pgp.html) to encrypt any sensitive communications you send to us. When you notify us of a potential security issue, our remediation process includes acknowledging receipt and coordinating any necessary response activities with you. 

## Learn More

To learn more about NI Security, please see [https://ni.com/security](https://ni.com/security)

<!-- End NI SECURITY.md -->
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=source/example.py sha256=626903cafcc99f4862c74b28cddf878fb1d7daadab277e5d265e1c28ced37535 bytes=405 -->
## FILE: source/example.py

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `source/example.py`
- sha256: `626903cafcc99f4862c74b28cddf878fb1d7daadab277e5d265e1c28ced37535`
- bytes: 405

````python
from screenshot_utility import capture_instrument_studio

# Specify folder and base filename (including extension)
output_folder = r"C:\Temp"
base_filename = "InstrStudio_screenshot.png"

# Capture (timestamp will be appended by default)
success, message = capture_instrument_studio(output_folder, base_filename)

if success:
    print(f"\n✅ {message}")
else:
    print(f"\n❌ {message}")
````

<!--NI_OSS_SOURCE repo=instrumentstudio-screenshot-utility-python path=source/screenshot_utility.py sha256=1896417593770e553a8af8bd66454462650cc22cda267c3f3072faba802c8858 bytes=12136 -->
## FILE: source/screenshot_utility.py

- repository: `ni/instrumentstudio-screenshot-utility-python`
- source_path: `source/screenshot_utility.py`
- sha256: `1896417593770e553a8af8bd66454462650cc22cda267c3f3072faba802c8858`
- bytes: 12136

````python
"""
InstrumentStudio Screenshot Utility

Captures the InstrumentStudio window content using Windows GDI APIs.
Works even when the window is hidden/minimized/behind other windows.
Automatically removes black borders and saves clean content.

Features:
  - Captures window using PrintWindow (renders actual window content)
  - Works across multiple monitors automatically
  - Auto-crops black borders
  - Supports PNG, JPG, BMP, GIF formats
  - Minimal dependencies (ctypes, PIL/Pillow)
"""

import ctypes
from ctypes import wintypes
from PIL import Image
import os
import time
from datetime import datetime

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# ============================================================================
# Windows API Constants
# ============================================================================
PW_RENDERFULLCONTENT = 0x00000002  # PrintWindow flag for full rendering
SRCCOPY = 0x00CC0020               # BitBlt raster operation code
BLACK_THRESHOLD = 10               # Brightness threshold for black detection
WINDOW_RESTORE_DELAY = 0.3         # Delay after restoring minimized window (seconds)

# Supported image file formats
SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')


# ============================================================================
# Windows Structures
# ============================================================================
class RECT(ctypes.Structure):
    """Windows RECT structure for window coordinates"""
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]


class BITMAPINFOHEADER(ctypes.Structure):
    """Windows BITMAPINFOHEADER structure for bitmap information"""
    _fields_ = [
        ('biSize', wintypes.DWORD),
        ('biWidth', wintypes.LONG),
        ('biHeight', wintypes.LONG),
        ('biPlanes', wintypes.WORD),
        ('biBitCount', wintypes.WORD),
        ('biCompression', wintypes.DWORD),
        ('biSizeImage', wintypes.DWORD),
        ('biXPelsPerMeter', wintypes.LONG),
        ('biYPelsPerMeter', wintypes.LONG),
        ('biClrUsed', wintypes.DWORD),
        ('biClrImportant', wintypes.DWORD),
    ]


# ============================================================================
# DPI Awareness Initialization
# ============================================================================
try:
    user32.SetProcessDPIAware()
except Exception:
    pass  # Not critical if DPI awareness fails


# ============================================================================
# Window Finding Functions
# ============================================================================
def _enum_windows_helper(match_func):
    """
    Helper to enumerate all visible windows.
    
    Args:
        match_func: Callable that takes window title (str) and returns bool
        
    Returns:
        List[int] - Window handles matching the function
    """
    results = []

    def enum_callback(hwnd, lParam):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buff, length + 1)
                if match_func(buff.value):
                    results.append((hwnd, buff.value))
        return True

    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumWindows(EnumWindowsProc(enum_callback), 0)
    return results


def list_all_windows():
    """
    Get list of all visible window titles.
    
    Returns:
        List[str] - Window titles (max 50 for readability)
    """
    windows = _enum_windows_helper(lambda t: True)
    return [title for _, title in windows[:50]]


def find_window_by_title(title_substring):
    """
    Find window handle by partial title match (case-insensitive).
    
    Args:
        title_substring (str) - Substring to search for in window titles
        
    Returns:
        int or None - Window handle if found, None otherwise
    """
    results = _enum_windows_helper(
        lambda t: title_substring.lower() in t.lower()
    )
    return results[0][0] if results else None


# ============================================================================
# Window Geometry Functions
# ============================================================================
def get_window_rect(hwnd):
    """
    Get window's bounding rectangle in screen coordinates.
    
    Args:
        hwnd (int) - Window handle
        
    Returns:
        RECT - Window rectangle (includes decorations and borders)
    """
    rect = RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect


# ============================================================================
# Image Processing Functions
# ============================================================================
def auto_crop_black_borders(image, threshold=BLACK_THRESHOLD):
    """
    Remove black borders from image by detecting non-black content bounds.
    
    Uses a quick sampling to detect if cropping is needed, then finds exact
    boundaries. Much faster than pixel-by-pixel on large images.
    
    Args:
        image (PIL.Image) - Image to crop
        threshold (int) - Brightness level to consider black (0-255)
        
    Returns:
        PIL.Image - Cropped image, or original if no borders detected
    """
    gray = image.convert('L')
    pixels = gray.load()
    w, h = image.width, image.height
    
    # Quick check: sample pixels to see if cropping needed
    sample_size = max(1, min(w, h) // 10)
    sample_pixels = [
        pixels[x, y] 
        for x in range(0, w, sample_size)
        for y in range(0, h, sample_size)
    ]
    
    # If >70% are non-black, likely no borders
    black_ratio = sum(1 for p in sample_pixels if p < threshold) / len(sample_pixels)
    if black_ratio < 0.3:
        return image
    
    # Find exact non-black boundaries
    left = next((x for x in range(w) 
                 if any(pixels[x, y] >= threshold for y in range(h))), 0)
    
    top = next((y for y in range(h) 
                if any(pixels[x, y] >= threshold for x in range(w))), 0)
    
    right = next((x + 1 for x in range(w - 1, -1, -1) 
                  if any(pixels[x, y] >= threshold for y in range(h))), w)
    
    bottom = next((y + 1 for y in range(h - 1, -1, -1) 
                   if any(pixels[x, y] >= threshold for x in range(w))), h)
    
    # Return cropped image if borders found
    if left > 0 or top > 0 or right < w or bottom < h:
        return image.crop((left, top, right, bottom))
    
    return image


def _create_bitmap_info(width, height):
    """Create and initialize BITMAPINFOHEADER structure."""
    bmi = BITMAPINFOHEADER()
    bmi.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.biWidth = width
    bmi.biHeight = -height  # Negative = top-down bitmap
    bmi.biPlanes = 1
    bmi.biBitCount = 32
    bmi.biCompression = 0  # BI_RGB
    return bmi


# ============================================================================
# Main Capture Function
# ============================================================================
def capture_instrument_studio(output_dir, base_filename, add_timestamp=True):
    """
    Capture InstrumentStudio window screenshot.
    
    Captures the window's actual rendered content using Windows GDI PrintWindow,
    which works even if the window is hidden/minimized/behind other windows.
    Automatically detects and removes black borders.
    
    Args:
        output_dir (str) - Directory to save the screenshot
        base_filename (str) - Base filename including extension (e.g. 'screenshot.png')
        add_timestamp (bool) - If True, append a timestamp to the filename before the extension
        
    Returns:
        Tuple[bool, str] - (Success flag, Status message)
        
    Example:
        success, msg = capture_instrument_studio('C:\\Temp\\screenshot.png')
        print(msg)
    """
    
    # Find InstrumentStudio window
    hwnd = find_window_by_title("InstrumentStudio")
    
    if not hwnd:
        return False, "Instrument Studio window not open. Please open the application and try again"
    
    # Restore if minimized
    if user32.IsIconic(hwnd):
        print("⚠️  Window is minimized, restoring...")
        user32.ShowWindow(hwnd, 9)  # SW_RESTORE
        time.sleep(WINDOW_RESTORE_DELAY)
    
    # Get window dimensions
    rect = get_window_rect(hwnd)
    width = rect.right - rect.left
    height = rect.bottom - rect.top
    
    if width <= 0 or height <= 0:
        return False, f"Invalid window dimensions: {width}x{height}"
    
    print(f"Capturing window ({width}x{height})...")
    
    # Set up GDI resources
    hwndDC = None
    memDC = None
    bitmap = None
    
    try:
        # Get device context
        hwndDC = user32.GetWindowDC(hwnd)
        if not hwndDC:
            return False, "Failed to get window DC"

        # Create compatible DC and bitmap
        memDC = gdi32.CreateCompatibleDC(hwndDC)
        if not memDC:
            return False, "Failed to create compatible DC"
            
        bitmap = gdi32.CreateCompatibleBitmap(hwndDC, width, height)
        if not bitmap:
            return False, "Failed to create compatible bitmap"
        
        gdi32.SelectObject(memDC, bitmap)

        # Capture window content
        result = user32.PrintWindow(hwnd, memDC, PW_RENDERFULLCONTENT)
        if not result:
            # Fallback to BitBlt
            result = gdi32.BitBlt(memDC, 0, 0, width, height, hwndDC, 0, 0, SRCCOPY)
            if not result:
                return False, "PrintWindow and BitBlt both failed"

        # Get bitmap bits
        bmi = _create_bitmap_info(width, height)
        buffer = ctypes.create_string_buffer(width * height * 4)
        bits = gdi32.GetDIBits(memDC, bitmap, 0, height, buffer, ctypes.byref(bmi), 0)

        if not bits:
            return False, "GetDIBits failed"

        # Convert to PIL image and auto-crop
        image = Image.frombuffer('RGB', (width, height), buffer, 'raw', 'BGRX', 0, 1)
        image = auto_crop_black_borders(image)
        
        # Build output path from directory + base filename
        if not base_filename:
            return False, "Base filename is required"

        os.makedirs(output_dir, exist_ok=True) if output_dir else None

        base, ext = os.path.splitext(base_filename)
        if not ext:
            return False, "Base filename must include an extension (e.g. '.png')"
        ext = ext.lower()

        timestamp = datetime.now().strftime("%d%b%Y_%H%M%S") if add_timestamp else ''
        filename = f"{base}_{timestamp}{ext}" if timestamp else f"{base}{ext}"
        output_file = os.path.join(output_dir, filename) if output_dir else filename

        # Validate and save
        ext = os.path.splitext(output_file)[1].lower()
        if ext not in SUPPORTED_FORMATS:
            return False, f"Unsupported format: {ext} (use {', '.join(SUPPORTED_FORMATS)})"
        
        directory = os.path.dirname(output_file)
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        image.save(output_file)
        msg = f"✓ Saved {image.width}x{image.height} to: {output_file}"
        print(msg)
        
        return True, "Screenshot captured successfully"
        
    except Exception as e:
        return False, f"Capture failed: {str(e)}"
    
    finally:
        # Cleanup GDI resources
        if bitmap:
            gdi32.DeleteObject(bitmap)
        if memDC:
            gdi32.DeleteDC(memDC)
        if hwndDC:
            user32.ReleaseDC(hwnd, hwndDC)
````
