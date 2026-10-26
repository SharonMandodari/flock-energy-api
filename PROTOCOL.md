# Protocol Discovery: Urja Meter Ops Portal

## Overview
* **Target Base URL**: `https://urja-ops.flockenergy.tech`
* **Purpose**: Reverse-engineering and wrapping the legacy Urja Meter Ops portal to provide clean, programmatic JSON endpoints for smart meter details and consumption history.

## Authentication Mechanism
* **Type**: Session Cookie (`__Secure-better-auth.session_token`)
* **Behavior**: The portal uses `better-auth` for session management. Tokens have a short lifespan and are subject to frequent rotation or expiration, requiring fresh session cookie injection via browser developer tools.

## Discovered Internal Endpoints
1. **Meter Search / Details**
   * **URL**: `/portal/meters/search`
   * **Method**: `GET`
   * **Parameters**: `q` (search query/meter ID), `page` (page number)
   * **Response**: JSON payload containing a list of matched meter objects (`meterId`, `serialNo`, `make`, `phaseType`, `status`, `dt`).

2. **Consumption History**
   * **URL**: `/portal/meters/{meter_id}/energy`
   * **Method**: `GET`
   * **Response**: Time-series JSON array containing intervals, timestamps, kWh, kVAh, and voltage readings.