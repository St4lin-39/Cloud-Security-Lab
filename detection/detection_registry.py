from detection.brute_force import detect_brute_force
from detection.resource_enumeration import detect_resource_enumeration
from  detection.credential_stuffing import detect_credential_stuffing
from detection.password_spraying import detect_password_spraying

DETECTORS = [
    detect_brute_force,
    detect_resource_enumeration,
    detect_credential_stuffing,
    detect_password_spraying

]