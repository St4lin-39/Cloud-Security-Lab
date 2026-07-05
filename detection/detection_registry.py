from detection.brute_force import detect_brute_force
from detection.resource_enumeration import detect_resource_enumeration
from  detection.credential_stuffing import detect_credential_stuffing

DETECTORS = [
    detect_brute_force,
    detect_resource_enumeration,
    detect_credential_stuffing
]