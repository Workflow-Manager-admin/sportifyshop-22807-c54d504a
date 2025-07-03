import os
import subprocess
import socket

def is_port_open(port, host='127.0.0.1'):
    """Check if the backend port is open and listening."""
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except OSError:
        return False

def check_uvicorn_process():
    """Check if a uvicorn or FastAPI-related server is running."""
    try:
        procs = subprocess.check_output(['ps', 'aux'], encoding='utf-8')
        uvicorn_lines = [line for line in procs.split('\n') if 'uvicorn' in line or 'fastapi' in line]
        return '\n'.join(uvicorn_lines) if uvicorn_lines else "No uvicorn/FastAPI process running."
    except Exception as e:
        return f"Error checking processes: {e}"

def find_nginx_conf():
    """Locate nginx config files in backend root & analyze for upstream settings. Also check project root for nginx configuration."""
    confs = []
    # Check . and parent directory (project root)
    search_dirs = ['.', '..']
    for basedir in search_dirs:
        for root, dirs, files in os.walk(basedir):
            for fn in files:
                if fn.endswith('.conf') or fn.startswith('nginx'):
                    confs.append(os.path.join(root, fn))
    return confs

def show_recent_logs(logfile_path=''):
    """Display last 20 lines of a .log file if exists."""
    if logfile_path and os.path.exists(logfile_path):
        try:
            with open(logfile_path, 'r') as f:
                lines = f.readlines()
                return "".join(lines[-20:])
        except Exception as e:
            return f"Could not read log: {e}"
    return "No log file found."

if __name__ == '__main__':
    print("==== FastAPI/Uvicorn Process Check ====")
    print(check_uvicorn_process())
    print("\n==== Is 127.0.0.1:8000 Listening? ====")
    print("Yes" if is_port_open(8000, '127.0.0.1') else "No (port 8000 is not reachable internally)")
    print("==== Is 0.0.0.0:8000 Listening? (common for nginx/docker proxy) ====")
    try:
        # 0.0.0.0 is not directly connectable in most OSes, we use LAN interface IPs as a proxy check
        import netifaces
        any_open = False
        for iface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(iface)
            inet_addrs = addrs.get(netifaces.AF_INET, [])
            for addr_dict in inet_addrs:
                ip = addr_dict.get('addr')
                if ip and ip != '127.0.0.1':
                    if is_port_open(8000, ip):
                        print(f"Yes (listening on {ip}:8000)")
                        any_open = True
        if not any_open:
            print("No (port 8000 not reachable on LAN interfaces)")
    except ImportError:
        # netifaces not installed, fallback attempt
        print("Skipped: Install netifaces for advanced interface scanning. [pip install netifaces]")
    print("\n==== Nginx Configurations (if any) in Backend or Project ====")
    confs = find_nginx_conf()
    print(confs if confs else "No nginx config files found in backend/project directory.")
    if confs:
        for cf in confs:
            print(f"--- {cf} ---")
            try:
                with open(cf) as f:
                    print("".join(f.readlines()[:30]))  # Print first 30 lines for review
            except Exception as e:
                print(f"Error reading {cf}: {e}")

    # Extra: Look for common nginx/proxy config files and document references
    root_files = os.listdir('..')
    for fname in root_files:
        if 'nginx' in fname.lower() or fname.endswith('.conf'):
            print(f"[MAY BE RELEVANT] Found potential nginx config or documentation in project root: ../{fname}")
            try:
                with open(os.path.join('..', fname)) as f:
                    print("".join(f.readlines()[:30]))
            except Exception as e:
                print(f"Error reading {fname}: {e}")

    print("\n==== Recent Gunicorn/Uvicorn .log (look in backend root) ====")
    logfiles = [f for f in os.listdir('.') if f.endswith('.log')]
    for logf in logfiles:
        print(f"-- {logf} --")
        print(show_recent_logs(logf))
