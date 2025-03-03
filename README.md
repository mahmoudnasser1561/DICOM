# DynamicDICOMRouter
### description:
* A project to set up multiple Orthanc DICOM servers
* DICOM C-STORE SCP Client to send DICOM data to those servers

### Features:
* Deploys multiple Orthanc servers (ORTHANC1, ORTHANC2, ORTHANC3) using custom JSON configurations.
* A Python client (using pynetdicom) sends DICOM files to multiple servers.
* Uses REST API queries to inspect stored DICOM instances.
