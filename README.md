# Port Scanner

This is a simple Python script for scanning ports on a target machine using multithreading. It utilizes the `socket` library for establishing connections to ports and `threading` for concurrent scanning of multiple ports.

## Overview

This script allows users to specify a target IP address (or `localhost`) and range of ports to scan. It then checks each port within the specified range for openness by attempting to establish a TCP connection. If the connection is successful (`connect_ex` returns 0), the port is considered open, otherwise, it's marked as closed.

## Features

- **Multithreaded Scanning**: The script uses threading to scan multiple ports concurrently, which can significantly reduce scanning time, especially when scanning a wide range of ports.
  
- **Customizable Port Range**: Users can specify the range of ports to scan, allowing flexibility based on their requirements.
  
- **Real-time Feedback**: The script provides real-time feedback on whether each scanned port is open or closed, making it easy to monitor the progress of the scan.

## How to Use

1. **Clone the Repository**: Clone or download the repository containing the script.

2. **Install Python**: Make sure you have Python installed on your system. The script is compatible with Python 3.

3. **Run the Script**: Execute the script using Python from the command line. Provide the target IP address or `localhost` when prompted, and optionally specify the range of ports to scan.

   ```bash
   python port_scanner.py
