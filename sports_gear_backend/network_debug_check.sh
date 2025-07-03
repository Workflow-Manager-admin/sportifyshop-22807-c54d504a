#!/bin/bash
# Advanced diagnostics for FastAPI/Uvicorn network accessibility

echo "==== Interface & Port Listening Check (netstat/ss/lsof) ===="

if command -v ss > /dev/null; then
    ss -tulnp | grep 8000
else
    echo "(ss not found, falling back to netstat or lsof)"
fi

if command -v netstat > /dev/null; then
    netstat -tulnp | grep 8000
fi

if command -v lsof > /dev/null; then
    lsof -i :8000
fi

echo; echo "==== Is firewall/iptables blocking 8000? (Linux - ufw/iptables) ===="
if command -v ufw > /dev/null; then
    sudo ufw status verbose | grep 8000
else
    echo "(ufw not found)"
fi

if command -v iptables > /dev/null; then
    sudo iptables -L INPUT -n | grep 8000
else
    echo "(iptables not found)"
fi

echo; echo "==== OS (and Docker) network info (ip addr, docker network ls) ===="
ip addr
if command -v docker > /dev/null; then docker network ls; fi

echo; echo "==== Routing table ===="
route -n

echo; echo "==== Is another process using 8000? (ps aux | grep 8000/uvicorn) ===="
ps aux | grep -E '8000|uvicorn'

echo; echo "==== Nginx/gunicorn check (if relevant) ===="
ps aux | grep -E 'nginx|gunicorn'

echo; echo "==== If STILL NOT ACCESSIBLE on 192.168.70.40:8000:"
echo "1. Check you can 'curl http://127.0.0.1:8000' and 'curl http://0.0.0.0:8000' on the backend machine itself."
echo "2. Temporarily disable firewall for a test: sudo ufw disable"
echo "   - or open selectively: sudo ufw allow 8000/tcp"
echo "   - for firewalld: sudo firewall-cmd --add-port=8000/tcp --permanent && sudo firewall-cmd --reload"
echo "3. Confirm you are NOT using VPN, Docker bridge, or NAT that isolates containers."
echo "4. Are you running inside a Docker container? Map the port: docker run -p 8000:8000 ... "
echo "5. If running on a VM/cloud/codespace: port-forward 8000, or use the provided public/external URL."
echo "6. Still stuck? Check 'run_backend.sh' is launching 'uvicorn ... --host 0.0.0.0', not default localhost."
echo
echo "If you need further help, copy-paste the entire output of this script to your support request!"

echo
echo "==== END OF NETWORK DEBUG ===="
