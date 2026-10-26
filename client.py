import httpx

class UrjaPortalClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": f"{self.base_url}/meters",
            "Cookie": "__Secure-better-auth.session_token=fIzsQJZHLneQw2EBo1QcIUlIOyZqEDIE.%2BphXGnHiPadkrYfpZ3F31P3eNSKnST6w4bUXael%2FlTo%3D"
        }
        
        self.client = httpx.Client(
            base_url=self.base_url, 
            follow_redirects=True, 
            headers=headers
        )

    def get_meter_details(self, meter_id: str):
        response = self.client.get("/portal/meters/search", params={"q": meter_id, "page": 1})
        
        if response.status_code != 200:
            raise Exception(f"Portal returned status {response.status_code}: {response.text}")
            
        result = response.json()
        items = result.get("data", [])
        
        for item in items:
            if item.get("meterId", "").lower() == meter_id.lower():
                return {
                    "meter_id": item.get("meterId"),
                    "serial_number": item.get("serialNo"),
                    "make": item.get("make"),
                    "phase": item.get("phaseType"),
                    "status": item.get("status"),
                    "dt": item.get("dt")
                }
                
        raise Exception(f"Meter ID '{meter_id}' not found in portal response.")

    def get_meter_consumption(self, meter_id: str):
        response = self.client.get(f"/portal/meters/{meter_id}/energy")
        
        if response.status_code != 200:
            raise Exception(f"Portal returned status {response.status_code}: {response.text}")
            
        return response.json()