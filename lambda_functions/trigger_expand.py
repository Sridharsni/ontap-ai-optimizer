import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ontap_api.ontap_client import ONTAPClient

def lambda_handler(event=None, context=None):
    usage = event.get('usage') if event else 85  # Default to 85 if no input
    if usage > 80:
        ontap = ONTAPClient('http://localhost:8000')
        volumes = ontap.get_volumes()
        target_volume = volumes['records'][0]
        ontap.expand_volume(target_volume['uuid'], target_volume['size'] + 1000000000)
        print("✅ Volume expanded!")
        return {'status': 'Volume Expanded'}
    print("⚠️ No expansion needed.")
    return {'status': 'No action needed'}

if __name__ == '__main__':
    lambda_handler()