# DynamicDICOMRouter
### description:
* A project to set up multiple Orthanc DICOM servers
* DICOM C-STORE SCP Client to send DICOM data to those servers

  ![diagram modified](https://github.com/user-attachments/assets/25dff47c-f87e-49bf-a0fd-e6bc32b9a36c)

### structure :
```bash
├── data
│   ├── generate.py
│   ├── test.dcm
│   └── test_template.json
├── media
│   ├── diagram modified.png
│   ├── DICOM_Instances.png
│   ├── sending_to_servers.png
│   └── specific_Instance.png
├── README.md
├── requirements.txt
├── send.py
└── servers
    ├── orthanc1.json
    ├── orthanc2.json
    ├── orthanc3.json
    └── start_servers.sh
```

### Features:
* Deploys multiple Orthanc servers (ORTHANC1, ORTHANC2, ORTHANC3) using custom JSON configurations.
* A Python client (using pynetdicom) sends DICOM files to multiple servers.
* Uses REST API queries to inspect stored DICOM instances.

### how it works:
* run file - `./servers/start_servers.sh`
* then login to the orthanc servers
* - **Orthanc Servers:**
  - `ORTHANC1` → [http://localhost:8042](http://localhost:8042)
  - `ORTHANC2` → [http://localhost:8043](http://localhost:8043)
  - `ORTHANC3` → [http://localhost:8044](http://localhost:8044)
  - orthanc:orthanc
 
* **feel free too modify json configurations to launch Orthanc servers on which free ports you have on your machine**

### Interaction with the servers:
* first you need to genrate DICOM Images (.dcm)
* you can use ./data/generate.py to genrate dummy dcm Images but missing metadata will make requests fail
* so I got some actual dcm data from [cancerimagingarchive](https://www.cancerimagingarchive.net/)
* you can use that find that data ./data/T1_TRA_SE-69134
* **now we are ready to send some DICOM to Orthanc servers**

### Interacting with Orthanc servers
* run the file send.py after configuring data paths to send some DICOM
* ![sending_to_servers](https://github.com/user-attachments/assets/f9dda8db-259f-4983-847c-d9c8120d5714)
* status (0000) !success

### Uses REST API queries to inspect stored DICOM instances.
![DICOM_Instances](https://github.com/user-attachments/assets/58812ef9-81df-41c3-98a4-ac6ddab6d574)
* Inspecting DICOM Instances on a specific server

![specific_Instance](https://github.com/user-attachments/assets/755a6091-1121-4e5a-bc1f-fafece141580)
* Inspecting a specific DICOM Instance   

## Limitations

- The infrastructure currently sends DICOM data to every Orthanc server without differentiation.
- No load balancing mechanism is implemented, leading to potential inefficiencies.
- There is no monitoring or status tracking for each Orthanc server.
- Security measures are minimal, making the system vulnerable to unauthorized access.
- No redundancy or failover mechanism in case a server goes down.

## Next Steps

- Implement a load balancing mechanism to distribute DICOM data efficiently.
- Introduce a health-check system to monitor the state of each Orthanc server.
- Enhance security by configuring authentication, encryption, and access control.
- Add logging and monitoring tools for better observability and debugging.
- Explore data replication or federation between servers to ensure consistency.
- Automate deployment and scaling using container orchestra




