import socket

# Test DNS resolution
hostname = "ep-autumn-brook-ad2tvvqx-pooler.c-2.us-east-1.aws.neon.tech"
print(f"Testing DNS resolution for: {hostname}")

try:
    ip = socket.gethostbyname(hostname)
    print(f"✓ Resolved to: {ip}")
except socket.gaierror as e:
    print(f"✗ DNS resolution failed: {e}")
    print("\nPossible solutions:")
    print("1. Check if you're behind a corporate firewall/proxy")
    print("2. Try using a different network (mobile hotspot)")
    print("3. Check if your antivirus is blocking connections")
    print("4. Verify the database URL is correct")
