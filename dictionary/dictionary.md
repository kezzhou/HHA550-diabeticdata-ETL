# Full Data Dictionary for clean_diabetic_data.csv
This dictionary starts from the first column and proceeds down to the last one in chronological order.

## encounter_id
- ID associated with the time stamp of their encounter

## patient_nbr
- Unique ID associated with each patient 

## race
- ? = 0
- Caucasian = 1
- AfricanAmerican = 2
- Hispanic = 3
- Asian = 4
- Other = 5


## gender
- Unknown/Invalid - 0
- Male = 1
- Female = 2

## age
- 0-10 = 10
- 10-20 = 20
- 20-30 = 30
- 30-40 = 40
- 40-50 = 50
- 50-60 = 60
- 60-70 = 70
- 70-80 = 80
- 80-90 = 90
- 90-100 = 100

## weight
- REMOVED

## admission_type_id
- Emergency = 1
- Urgent = 2
- Elective = 3
- Newborn = 4
- Not Available = 5
- NULL = 6
- Trauma Center = 7
- Not Mapped = 8

## discharge_disposition_id
- Discharged to home = 1
- Discharged/transferred to another short term hospital = 2
- Discharged/transferred to SNF = 3
- Discharged/transferred to ICF = 4
- Discharged/transferred to another type of inpatient care institution = 5
- Discharged/transferred to home with home health service = 6
- Left AMA = 7
- Discharged/transferred to home under care of Home IV provider = 8
- Admitted as an inpatient to this hospital = 9 
- Neonate discharged to another hospital for neonatal aftercare = 10
- Expired = 11
- Still patient or expected to return for outpatient services = 12
- Hospice / home = 13
- Hospice / medical facility = 14
- Discharged/transferred within this institution to Medicare approved swing bed = 15
- Discharged/transferred/referred another institution for outpatient services = 16
- Discharged/transferred/referred to this institution for outpatient services = 17
- NULL = 18
- Expired at home. Medicaid only, hospice = 19
- Expired in a medical facility. Medicaid only, hospice = 20
- Expired, place unknown. Medicaid only, hospice = 21
- Discharged/transferred to another rehab fac including rehab units of a hospital = 22
- Discharged/transferred to a long term care hospital = 23
- Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare = 24
- Not Mapped = 25
- Unknown/Invalid = 26
- Discharged/transferred to a federal health care facility = 27
- Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital = 28
- Discharged/transferred to a Critical Access Hospital (CAH) = 29
- Discharged/transferred to another Type of Health Care Institution not Defined Elsewhere = 30

## admission_source_id
- Physician Referral = 1
- Clinic Referral = 2
- HMO Referral = 3
- Transfer from a hospital = 4
- Transfer from a Skilled Nursing Facility (SNF) = 5
- Transfer from another health care facility = 6
- Emergency Room = 7
- Court/Law Enforcement = 8
- Not Available = 9
- Transfer from critial access hospital = 10
- Normal Delivery = 11
- Premature Delivery = 12
- Sick Baby = 13
- Extramural Birth = 14
- Not Available = 15
- NULL = 17
- Transfer From Another Home Health Agency = 18
- Readmission to Same Home Health Agency = 19
- Not Mapped = 20
- Unknown/Invalid = 21
- Transfer from hospital inpt/same fac reslt in a sep claim = 22
- Born inside this hospital = 23
- Born outside this hospital = 24
- Transfer from Ambulatory Surgery Center = 25
- Transfer from Hospice = 26

## time_in_hospital
***Time currently unknown, assumed hours***
- 1 
- 2
- 3
- 4
- 5 
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14

## payer_code
- REMOVED

## medical_specialty
- ? = 0 
- Pediatrics-Endocrinology = 1
- InternalMedicine = 2
- Family/GeneralPractice = 3
- Cardiology = 4
- Surgery-General = 5
- Orthopedics = 6
- Gastroenterology = 7
- Surgery-Cardiovascular/Thoracic = 8
- Nephrology = 9
- Orthopedics-Reconstructive = 10
- Psychiatry = 11
- Emergency/Trauma = 12
- Pulmonology = 13
- Surgery-Neuro = 14
- Obsterics&Gynecology-GynecologicOnco = 15
- ObstetricsandGynecology = 16
- Pediatrics = 17
- Hematology/Oncology = 18
- Otolaryngology = 19
- Surgery-Colon&Rectal = 20
- Pediatrics-CriticalCare = 21
- Endocrinology = 22
- Urology = 23
- Psychiatry-Child/Adolescent = 24
- Pediatrics-Pulmonology = 25
- Neurology = 26
- Anesthesiology-Pediatric = 27
- Radiology = 28
- Pediatrics-Hematology-Oncology = 29
- Psychology = 30
- Podiatry = 31
- Gynecology = 32
- Oncology = 33
- Pediatrics-Neurology = 34
- Surgery-Plastic = 35
- Surgery-Thoracic = 36
- Surgery-PlasticwithinHeadandNeck = 37
- Ophthalmology = 38
- Surgery-Pediatric = 39
- Pediatrics-EmergencyMedicine = 40
- Rheumatology = 41
- AllergyandImmunology = 42
- Surgery-Maxillofacial = 43
- Pediatrics-InfectiousDiseases = 44
- Pediatrics-AllergyandImmunology = 45
- Dentistry = 46
- Surgeon = 47
- Surgery-Vascular = 48
- Osteopath = 49
- Psychiatry-Addictive = 50
- Surgery-Cardiovascular = 51
- PhysicianNotFound = 52
- Hematology = 53
- Proctology = 54
- Obstetrics = 55
- SurgicalSpecialty = 56
- Radiologist = 57
- Pathology = 58
- Dermatology = 59
- SportsMedicine = 60
- Speech = 61
- Hospitalist = 62
- OutreachServices = 63
- Cardiology-Pediatric = 64
- Perinatology = 65
- Neurophysiology = 66
- Endocrinology-Metabolism = 67
- DCPTEAM = 68
- Resident = 69

## num_lab_procedures
- Depicted as total

## num_procedures 
- Depicted as total

## num_medications
- Depicted as total

## number_outpatient 
- Depicted as total

## number_emergency 
- Depicted as total

## number_inpatient 
- Depicted as total

## diag_1-3
- ***Diagnosis codes are not available***

## number_diagnoses
- Depicted as total

## max_glu_serum (Serum phospholipid fatty acid composition levels)
- None = 0
- Norm = 1
- (>200) = 2
- (>300) = 3

## a1cresult
- None = 0
- Norm = 1
- (>7) = 7
- (>8) = 8

## metformin 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## repaglinide 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## nateglinide 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## chlorpropamide
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## glimepiride 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## acetohexamide 
- No = 0
- Steady = 1

## glipizide 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## glyburide 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## tolbutamide
- No = 0
- Steady = 1

## pioglitazone 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## rosiglitazone 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## acarbose 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## miglitol 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## troglitazone
- No = 0
- Steady = 1

## tolazamide 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## examide 
- No = 0

## citoglipton 
- No = 0

## insulin
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## glyburide-metformin 
- No = 0
- Steady = 1
- Up = 10
- Down = 5

## glipizide-metformin
- No = 0
- Steady = 1

## glimepiride-pioglitazone 
- No = 0
- Steady = 1

## metformin-rosiglitazone
- No = 0
- Steady = 1

## metformin-pioglitazone 
- No = 0
- Steady = 1

## change 
- No = 0
- Ch = 1

## diabetesMed 
- No = 0
- Yes = 1

## readmitted
- NO = 0
- (<30) = 1
- (>30) = 5