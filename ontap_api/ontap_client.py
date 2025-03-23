import requests

class ONTAPClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.verify = False  # Only if you're using self-signed SSL cert
        self.session.headers.update({'Content-Type': 'application/json'})

    def get_volumes(self):
        response = self.session.get(f"{self.base_url}/api/storage/volumes")
        return response.json()

# Example usage
if __name__ == "__main__":
    client = ONTAPClient("https://<your-sim-ip>", "admin", "netapp1!")
    volumes = client.get_volumes()
    print(volumes)
