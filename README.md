# SSH-Bruteforcer

A simple Python script that performs an SSH password brute-force attack using a username and a wordlist. Built for **CTFs, labs, and authorized security testing only**.

## Features

* Uses **Paramiko** (SSH library for Python)
* Attempts each password from a wordlist
* Auto-adds unknown SSH host keys
* Stops immediately when a valid password is found
* Minimal and easy to modify for learning

## Usage

```bash
python3 SSH_Bruteforcer.py <SSH_server_IP> <username> <passwords-file>
```

### Example

```bash
python3 SSH_Bruteforcer.py 10.10.11.22 administrator ./passwords.txt
```

Wordlist must contain **one password per line**.

## Requirements

Install Paramiko:

```bash
pip install paramiko
```

## Notes

* SSH brute forcing is slower by nature — servers can enforce rate limits, lockouts, or ban IPs.
* Recommended only for controlled environments like **TryHackMe**, **Hack The Box**, or your own machines.
* Edit the script to add:

  * delays between attempts
  * connection timeouts
  * proxy/socks support
  * multi-threading (careful: SSH servers block fast)

## Ethical Notice

**Unauthorized access to systems is illegal.**
Use this script **only** in environments where you have explicit permission.
