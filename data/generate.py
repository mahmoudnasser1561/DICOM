from dicomgenerator.generators import quick_dataset
import pydicom
from pydicom.uid import ExplicitVRLittleEndian, generate_uid

ds = quick_dataset(PatientName='John Doe', StudyDescription='Brain MRI')

ds.is_little_endian = True
ds.is_implicit_VR = False  
ds.SOPClassUID = "1.2.840.10008.5.1.4.1.1.1"
ds.SOPInstanceUID = generate_uid()

file_meta = pydicom.dataset.FileMetaDataset()
file_meta.MediaStorageSOPClassUID = generate_uid()
file_meta.MediaStorageSOPInstanceUID = generate_uid()
file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
file_meta.ImplementationClassUID = generate_uid()

ds.file_meta = file_meta

ds.save_as("test.dcm", write_like_original=False)

print("DICOM file saved: test.dcm")
