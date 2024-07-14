#!/bin/bash

while true; do
    # Run the Python script in the background
    python main.py &

    # Get the process ID of the last background command
    PID=$!

    # Wait for 5 hours (18000 seconds)
    sleep 3600

    # Kill the Python script
    kill $PID

    # Wait a moment to ensure the process is killed
    sleep 1
done
