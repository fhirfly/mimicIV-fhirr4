# Constant lookups that are used throughout the package

MIMIC_FHIR_PROFILE_URL = {
    'Condition':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-condition',
    'Encounter':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-encounter',
    'EncounterTransfers':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-encounter-transfers',
    'EncounterICU':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-encounter-icu',
    'Location':
        '',
    'Medication':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-medication',
    'MedicationAdministration':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-medication-administration',
    'MedicationAdministrationICU':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-medication-administration-icu',
    'MedicationDispense':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-medication-dispense',
    'MedicationRequest':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-medication-request',
    'ObservationChartevents':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-chartevents',
    'ObservationDatetimeevents':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-datetimeevents',
    'ObservationLabevents':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-labevents',
    'ObservationMicroTest':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-micro-test',
    'ObservationMicroOrg':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-micro-org',
    'ObservationMicroSusc':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-micro-susc',
    'ObservationOutputevents':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-observation-outputevents',
    'Organization':
        '',
    'Patient':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-patient',
    'Procedure':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-procedure',
    'ProcedureICU':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-procedure-icu',
    'Specimen':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-specimen',
    'SpecimenLab':
        'http://mimic.mit.edu/fhir/StructureDefinition/mimic-specimen'
}

MIMIC_FHIR_RESOURCES = {
    'MimicCondition': 'Condition',
    'MimicEncounter': 'Encounter',
    'MimicEncounterICU': 'Encounter',
    'Location': 'Location',
    'MimicMedication': 'Medication',
    'MimicMedicationAdministration': 'MedicationAdministration',
    'MimicMedicationAdministrationICU': 'MedicationAdministration',
    'MimicMedicationDispense': 'MedicationDispense',
    'MimicMedicationRequest': 'MedicationRequest',
    'MimicObservationChartevents': 'Observation',
    'MimicObservationDatetimeevents': 'Observation',
    'MimicObservationLabevents': 'Observation',
    'MimicObservationMicroTest': 'Observation',
    'MimicObservationMicroOrg': 'Observation',
    'MimicObservationMicroSusc': 'Observation',
    'MimicObservationOutputevents': 'Observation',
    'MimicOrganization': 'Organization',
    'MimicPatient': 'Patient',
    'MimicProcedure': 'Procedure',
    'MimicProcedureICU': 'Procedure',
    'MimicSpecimen': 'Specimen'
}

MIMIC_FHIR_PROFILE_NAMES = [
    'MimicCondition', 'MimicEncounter', 'MimicEncounterICU', 'MimicLocation',
    'MimicMedication', 'MimicMedicationAdministration',
    'MimicMedicationAdministrationICU', 'MimicMedicationDispense',
    'MimicMedicationRequest', 'MimicObservationChartevents',
    'MimicObservationDatetimeevents', 'MimicObservationLabevents',
    'MimicObservationMicroTest', 'MimicObservationMicroOrg',
    'MimicObservationMicroSusc', 'MimicObservationOutputevents',
    'MimicOrganization', 'MimicPatient', 'MimicProcedure', 'MimicProcedureICU',
    'MimicSpecimen'
]

MIMIC_CODESYSTEMS = [
    'admission_class', 'admission_type', 'admit_source', 'bodysite',
    'chartevents_d_items', 'd_items', 'd_labitems', 'diagnosis_icd9',
    'diagnosis_icd10', 'discharge_disposition', 'hcpcs_cd', 'lab_fluid',
    'lab_priority', 'medadmin_category_icu', 'medication_etc', 'medication_icu',
    'medication_formulary_drug_cd', 'medication_frequency', 'medication_gsn',
    'medication_method', 'medication_method_icu', 'medication_name',
    'medication_ndc', 'medication_poe_iv', 'medication_route',
    'medication_site', 'microbiology_antibiotic', 'microbiology_organism',
    'microbiology_test', 'observation_category', 'procedure_category',
    'procedure_icd9', 'procedure_icd10', 'services', 'spec_type_desc', 'units'
]

MIMIC_VALUESETS = [
    'admission_class', 'admission_type', 'admit_source', 'bodysite',
    'chartevents_d_items', 'd_labitems', 'datetimeevents_d_items',
    'diagnosis_icd', 'discharge_disposition', 'encounter_type', 'lab_priority',
    'medadmin_category_icu', 'medication', 'medication_etc',
    'medication_frequency', 'medication_gsn', 'medication_method',
    'medication_method_icu', 'medication_route', 'medication_site',
    'microbiology_antibiotic', 'microbiology_organism', 'microbiology_test',
    'observation_category', 'outputevents_d_items', 'procedure_category',
    'procedureevents_d_items', 'procedure_icd', 'services', 'specimen_type',
    'units'
]

VALUESETS_COMPLEX = [
    'admission_class', 'admission_type', 'datetimeevents_d_items',
    'diagnosis_icd', 'encounter_type', 'medication', 'outputevents_d_items',
    'procedureevents_d_items', 'procedure_icd', 'specimen_type'
]
# ORDER MATTERS!!
# The patient bundle must be first and the icu_encounter bundle must be before all other icu bundles
# Medication request, dispense and administration have been spaced out so one is processed before the next
# Medication bundle with all them became too big
MIMIC_BUNDLE_TABLE_LIST = {
    'patient': ['patient', 'encounter'],
    'procedure': ['procedure'],
    'condition': ['condition'],
    'specimen': ['specimen', 'specimen_lab'],
    'lab': ['observation_labevents'],
    'microbiology':
        [
            'observation_micro_test', 'observation_micro_org',
            'observation_micro_susc'
        ],
    'medication-request': ['medication_request'],
    'icu-encounter': ['encounter_icu'],
    'icu-medication': ['medication_administration_icu'],
    'medication-dispense': ['medication_dispense'],
    'icu-procedure': ['procedure_icu'],
    'icu-observation':
        [
            'observation_chartevents', 'observation_datetimeevents',
            'observation_outputevents'
        ],
    'medication-administration': ['medication_administration'],
    'ed-base': ['encounter_ed', 'procedure_ed'],
    'ed-observation': ['observation_ed', 'observation_vital_signs'],
    'ed-medication': ['medication_statement_ed', 'medication_dispense_ed']
}

MIMIC_DATA_BUNDLE_LIST = [
    'organization', 'location', 'medication', 'medication_mix'
]

MIMIC_BUNDLES_NO_SPLIT_LIST = ['microbiology', 'medication-workflow']
