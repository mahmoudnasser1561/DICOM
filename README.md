# Transfer DICOM
### description:
* A project to set up three Orthanc DICOM servers
* DICOM C-STORE SCP Client to send DICOM data to those servers
![unpdated_Arch](https://github.com/user-attachments/assets/99731025-a408-48ec-8937-6cf796844051)


### structure :
```bash
.
├── add_server.sh
├── data
│   ├── generate.py
│   ├── test.dcm
│   └── test_template.json
├── docker-compose.yml
├── media
│   ├── diagram modified.png
│   ├── DICOM_Instances.png
│   ├── sending_to_servers.png
│   └── specific_Instance.png
├── monitoring.log
├── README.md
├── requirements.txt
├── scripts
│   ├── monitor.py
│   └── send.py
└── servers
    ├── monitor_containers.sh
    ├── orthanc1.json
    ├── orthanc2.json
    ├── orthanc3.json
    └── start_servers.sh

```

### Features:
* Deploys multiple Orthanc servers (ORTHANC1, ORTHANC2, ORTHANC3) using docker compose file.
* A Python client (using pynetdicom) sends DICOM files to multiple servers.
* Uses REST API queries to inspect orthanc servers and inspect stored DICOM instances.
###### we can extend that that REST API and make a flask dashboard or something like that but I prefer The CLI as it's more flexible

### how it works:
* run ```docker compose up -d``` this will give you three preconfigured Orthanc servers on ports 8042, 8043, 8044
* then login to the orthanc servers
* - **Orthanc Servers:**
  - `ORTHANC1` → [http://localhost:8042](http://localhost:8042)
  - `ORTHANC2` → [http://localhost:8043](http://localhost:8043)
  - `ORTHANC3` → [http://localhost:8044](http://localhost:8044)
  - orthanc:orthanc
 
##### you can also launch more by utilizing the bash script start_servers.sh
##### just run the file with ./start_servers.sh and give add an incremental number from 4 forwad
##### ps: ```./start_servers.sh 4```

#### make sure that any new servers you launch add them to send.py to make them visible and send DICOM to them

### Interaction with the servers:
* first you need to genrate DICOM Images (.dcm)
* you can use ./data/generate.py to genrate dummy dcm Images but missing metadata will make requests fail
* so I got some actual dcm data from [cancerimagingarchive](https://www.cancerimagingarchive.net/)
* you can use that data ./data/T1_TRA_SE-69134
* **now we are ready to send some DICOM to Orthanc servers**

### Interacting with Orthanc servers
* run the file send.py after configuring data paths and servers if you launched new ones  
* ![sending_to_servers](https://github.com/user-attachments/assets/f9dda8db-259f-4983-847c-d9c8120d5714)
* status (0000) !success

### Uses REST API queries to inspect stored DICOM instances and query your servers.
![DICOM_Instances](https://github.com/user-attachments/assets/58812ef9-81df-41c3-98a4-ac6ddab6d574)
* Inspecting DICOM Instances on a specific server

![specific_Instance](https://github.com/user-attachments/assets/755a6091-1121-4e5a-bc1f-fafece141580)
* Inspecting a specific DICOM Instance

* you can do some monitoring using monitoy_containers.sh this will give you life data about you containers
* monitoring data will go into monitoring.log

## Next Steps

- Implement a load balancing mechanism to distribute DICOM data efficiently.
- Enhance security by configuring authentication, encryption, and access control.
- Explore data replication or federation between servers to ensure consistency.
- Automate deployment and scaling using container orchestra




