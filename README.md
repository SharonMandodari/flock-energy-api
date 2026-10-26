# Flock Energy - Urja Meter Ops API Wrapper

A modern, well-documented REST API wrapper built with **FastAPI** and **httpx** that bridges the legacy "Urja Meter Ops" portal into clean, structured JSON endpoints.

## Project Structure
```text
flock-energy-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI route definitions
│   └── client.py        # Urja Portal HTTP adapter layer
├── PROTOCOL.md          # Legacy portal reconnaissance notes
├── REFLECTION.md        # Architectural reflections & challenges
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies