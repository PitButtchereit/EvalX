"""Module providing constants for the project."""
import os

oaik = os.environ.get(
    "OPENAI_API_KEY"
)  # Get the OpenAI API key from the environment variables
MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 1100
TEMPERATURE_SUMMARIZING = 0
TEMPERATURE_CREATION = 1
MODULES_REQUIRED = [
    ("activity_labeling", "Activity Labeler"),
]
MODULES_OPTIONAL = [
    ("preprocessing", "Preprocessor"),
    ("cohort_tagging", "Cohort Tagger"),
    ("time_extraction", "Time Extractor"),
    ("event_type_classification", "Event Type Classifier"),
    ("location_extraction", "Location Extractor"),
    ("metrics_analyzer", "Metrics Analyzer"),
]
EVENT_TYPES = [
    ("Symptom Onset", "Symptom Onset"),
    ("Symptom Offset", "Symptom Offset"),
    ("Diagnosis", "Diagnosis"),
    ("Doctor Visit", "Doctor Visit"),
    ("Treatment", "Treatment"),
    ("Hospital Admission", "Hospital Admission"),
    ("Hospital Discharge", "Hospital Discharge"),
    ("Medication", "Medication"),
    ("Lifestyle Change", "Lifestyle Change"),
    ("Feelings", "Feelings"),
    ("N/A", "N/A"),
]
LOCATIONS = [
    ("Home", "Home"),
    ("Hospital", "Hospital"),
    ("Doctors", "Doctors"),
    ("N/A", "N/A"),
]
ACTIVITY_KEYS = [
    ("event_type", "Event Type"),
    ("activity", "Activity Label"),
    ("attribute_location", "Location"),
]
THRESHOLD_FOR_MATCH = 0.5
SNOMED_CT_API_URL = (
    "https://browser.ihtsdotools.org/snowstorm/snomed-ct/browser/MAIN/descriptions"
)
SNOMED_CT_PARAMS = params = {
    "limit": 1,
    "conceptActive": "true",
    "lang": "english",
    "skipTo": 0,
    "returnLimit": 1,
}
SNOMED_CT_HEADERS = {
    "User-Agent": "browser",
}
