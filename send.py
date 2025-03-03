import os
from pynetdicom import AE, StoragePresentationContexts
import pydicom

def send_dicom(file_path, target_ip, target_port, target_ae):
    ae = AE()
    
    for context in StoragePresentationContexts:
        ae.add_requested_context(context.abstract_syntax)

    assoc = ae.associate(target_ip, target_port, ae_title=target_ae)

    if assoc.is_established:
        ds = pydicom.dcmread(file_path)
        status = assoc.send_c_store(ds)
        print(f"Sent {file_path} to {target_ae} - Status: {status}")
        assoc.release()
    else:
        print(f"Failed to connect to {target_ae}")

servers = [
    {"ip": "127.0.0.1", "port": 4242, "ae": "ORTHANC1"},
    {"ip": "127.0.0.1", "port": 4243, "ae": "ORTHANC2"},
    {"ip": "127.0.0.1", "port": 4244, "ae": "ORTHANC3"},
]

dicom_folder = "./data/T1_TRA_SE-69134"

for file_name in os.listdir(dicom_folder):
    file_path = os.path.join(dicom_folder, file_name)
    if file_path.endswith(".dcm"):
        for server in servers:
            send_dicom(file_path, server["ip"], server["port"], server["ae"])
