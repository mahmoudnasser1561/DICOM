import requests

servers = [
    {"name": "ORTHANC1", "url": "http://localhost:8042", "auth": ("orthanc", "orthanc")},
    {"name": "ORTHANC2", "url": "http://localhost:8043", "auth": ("orthanc", "orthanc")},
    {"name": "ORTHANC3", "url": "http://localhost:8044", "auth": ("orthanc", "orthanc")},
]

total_instances = 0  

def check_server_status(server):
    global total_instances  
    try:
        response = requests.get(f"{server['url']}/instances", auth=server["auth"], timeout=5)
        
        if response.status_code == 200:
            num_instances = len(response.json())
            print(f"[✔] {server['name']} is running. DICOM Instances: {num_instances}")
            total_instances += num_instances 
        else:
            print(f"[✖] {server['name']} is unreachable (Status Code: {response.status_code})")


        system_res = requests.get(f"{server['url']}/system", auth=server["auth"], timeout=5)
        system_info = system_res.json() if system_res.status_code == 200 else {}
        print(f"[*] StorageCompression: {system_info.get("StorageCompression")}")

        stats_res = requests.get(f"{server['url']}/statistics", auth=server["auth"], timeout=5)
        stats_info = stats_res.json() if stats_res.status_code == 200 else {}

        print(f"[*] TotalDiskSize: {stats_info.get('TotalDiskSizeMB')} MB")


    except requests.exceptions.RequestException as e:
        print(f"[✖] {server['name']} is down: {e}")

if __name__ == "__main__":
    for server in servers:
        check_server_status(server)
    
    print(f"\nTotal DICOM Instances across all servers: {total_instances}")
