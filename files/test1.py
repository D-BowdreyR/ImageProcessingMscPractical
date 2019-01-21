#!python

import pydicom

FILENAME = "/Users/daniel/coding-workspace/dicom/images/00004-MR-t2_pep_apl_orn/00001.dcm"

dcm = pydicom.read_file(FILENAME)
print(dcm.PatientName)


