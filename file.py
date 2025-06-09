import platform
import time
import subprocess

def get_linux_uptime():
    """Get uptime on Linux systems using /proc/uptime."""
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds
    except Exception as e:
        print(f"Error reading /proc/uptime: {e}")
        return None

def get_macos_uptime():
    """Get uptime on macOS systems using subprocess and sysctl."""
    try:
        result = subprocess.run(
            ["sysctl", "-n", "kern.boottime"],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        boot_time = int(output.split('sec =')[1].split(',')[0].strip())
        uptime_seconds = time.time() - boot_time
        return uptime_seconds
    except Exception as e:
        print(f"Error getting uptime on macOS: {e}")
        return None

def get_windows_uptime():
    """Get uptime on Windows using ctypes."""
    try:
        import ctypes
        GetTickCount64 = getattr(ctypes.windll.kernel32, 'GetTickCount64', None)
        if GetTickCount64:
            uptime_ms = GetTickCount64()
        else:
            uptime_ms = ctypes.windll.kernel32.GetTickCount()
        return uptime_ms / 1000.0
    except Exception as e:
        print(f"Error getting uptime on Windows: {e}")
        return None

def print_system_uptime():
    """Detect OS and print the system uptime in human-readable format."""
    system = platform.system()
    uptime_seconds = None

    if system == "Linux":
        uptime_seconds = get_linux_uptime()
    elif system == "Darwin":
        uptime_seconds = get_macos_uptime()
    elif system == "Windows":
        uptime_seconds = get_windows_uptime()
    else:
        print(f"Unsupported OS: {system}")
        return

    if uptime_seconds is None:
        print("Could not determine uptime.")
        return

    days = int(uptime_seconds // (24 * 3600))
    hours = int((uptime_seconds % (24 * 3600)) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)

    print(f"System Uptime: {days}d {hours}h {minutes}m {seconds}s")

if __name__ == "__main__":
    print_system_uptime()
