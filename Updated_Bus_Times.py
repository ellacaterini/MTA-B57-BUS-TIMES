import json
import requests
import time

def bustime(link):
    while True:
        try:
            response = requests.get(link)
            data = response.json()

            # Print summaries
            print("\nTop-level keys:")
            print(data.keys())

            print("\n'Siri' keys:")
            print(data['Siri'].keys())

            print("\n'ServiceDelivery' keys:")
            print(data['Siri']['ServiceDelivery'].keys())

            print("\n'StopMonitoringDelivery' keys:")
            print(data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0].keys())

            # Optional: full formatted output
            print("\n--- Full JSON Output ---\n")
            print(json.dumps(data, indent=2))

            # Save to JSON for HTML to access
            with open("bus_data.json", "w") as f:
                json.dump(data, f)

        except Exception as e:
            print("Error:", e)

        time.sleep(35)

bustime('https://bustime.mta.info/api/siri/stop-monitoring.json?key=65f5be5b-632d-4092-8eed-f740d3b1e8f3&OperatorRef=MTA&MonitoringRef=307493&LineRef=MTA%20NYCT_B57')