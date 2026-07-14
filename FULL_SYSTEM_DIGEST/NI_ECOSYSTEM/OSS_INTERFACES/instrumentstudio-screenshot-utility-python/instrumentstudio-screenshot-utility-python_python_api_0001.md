# NI PYTHON API DIGEST: instrumentstudio-screenshot-utility-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/instrumentstudio-screenshot-utility-python commit=10b3210f8add27a4cfa3e123468874265c8ce6da -->

<!--NI_PYTHON_API repo=instrumentstudio-screenshot-utility-python path=source/screenshot_utility.py -->
## PYTHON MODULE: source/screenshot_utility.py

### MODULE DOCSTRING


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


- `PW_RENDERFULLCONTENT = 2`

- `SRCCOPY = 13369376`

- `BLACK_THRESHOLD = 10`

- `WINDOW_RESTORE_DELAY = 0.3`

- `SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')`

### `class RECT(ctypes.Structure)`

Windows RECT structure for window coordinates

### `class BITMAPINFOHEADER(ctypes.Structure)`

Windows BITMAPINFOHEADER structure for bitmap information

### `def _enum_windows_helper(match_func)`


    Helper to enumerate all visible windows.
    
    Args:
        match_func: Callable that takes window title (str) and returns bool
        
    Returns:
        List[int] - Window handles matching the function
    

### `def list_all_windows()`


    Get list of all visible window titles.
    
    Returns:
        List[str] - Window titles (max 50 for readability)
    

### `def find_window_by_title(title_substring)`


    Find window handle by partial title match (case-insensitive).
    
    Args:
        title_substring (str) - Substring to search for in window titles
        
    Returns:
        int or None - Window handle if found, None otherwise
    

### `def get_window_rect(hwnd)`


    Get window's bounding rectangle in screen coordinates.
    
    Args:
        hwnd (int) - Window handle
        
    Returns:
        RECT - Window rectangle (includes decorations and borders)
    

### `def auto_crop_black_borders(image, threshold=BLACK_THRESHOLD)`


    Remove black borders from image by detecting non-black content bounds.
    
    Uses a quick sampling to detect if cropping is needed, then finds exact
    boundaries. Much faster than pixel-by-pixel on large images.
    
    Args:
        image (PIL.Image) - Image to crop
        threshold (int) - Brightness level to consider black (0-255)
        
    Returns:
        PIL.Image - Cropped image, or original if no borders detected
    

### `def _create_bitmap_info(width, height)`

Create and initialize BITMAPINFOHEADER structure.

### `def capture_instrument_studio(output_dir, base_filename, add_timestamp=True)`


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
        success, msg = capture_instrument_studio('C:\Temp\screenshot.png')
        print(msg)
    
