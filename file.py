import subprocess

def get_system_uptime():
    """
    Returns the system uptime as a string.
    Uses subprocess.run() for command execution and includes exception handling.
    """
    try:
        result = subprocess.run(['uptime', '-p'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except FileNotFoundError:
        return "The 'uptime' command is not available on this system."
    except subprocess.CalledProcessError as e:
        return f"An error occurred while retrieving uptime: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

if __name__ == "__main__":
    print("System Uptime:", get_system_uptime())
