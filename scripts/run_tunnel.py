#!/usr/bin/env python
"""
Script to setup ngrok tunnel for public access.

Usage:
    python scripts/run_tunnel.py
"""

from src.utils.tunnel import setup_ngrok_tunnel, keep_tunnel_alive


def main():
    """Main tunnel entry point"""
    try:
        public_url = setup_ngrok_tunnel()
        print(f"✅ Tunnel active at: {public_url}")
        keep_tunnel_alive()
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
