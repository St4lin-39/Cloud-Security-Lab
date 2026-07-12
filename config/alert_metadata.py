ALERT_METADATA = {

    "BRUTE_FORCE_ATTEMPT": {
        "severity": "MEDIUM",
        "confidence": 90,
        "description": "Multiple failed authentication attempts detected for the same user within a short period of time.",
        "recommendation": "Temporarily lock the affected account and investigate the originating IP address.",
        "mitre_tactic": "Credential Access",
        "mitre_technique": "T1110.001"
    },

    "RESOURCE_ENUMERATION": {
        "severity": "LOW",
        "confidence": 70,
        "description": "Multiple protected resources were accessed in a short period of time, indicating possible reconnaissance activity.",
        "recommendation": "Review the accessed resources and verify whether the activity is legitimate.",
        "mitre_tactic": "Discovery",
        "mitre_technique": "T1083"
    },

    "CREDENTIAL_STUFFING": {
        "severity": "HIGH",
        "confidence": 95,
        "description": "Multiple usernames were targeted from the same IP address using different credentials.",
        "recommendation": "Investigate the source IP address and force password resets for affected accounts if necessary.",
        "mitre_tactic": "Credential Access",
        "mitre_technique": "T1110.004"
    },

    "PASSWORD_SPRAYING": {
        "severity": "HIGH",
        "confidence": 95,
        "description": "A single password was attempted against multiple user accounts.",
        "recommendation": "Block the source IP address and investigate possible password spraying activity.",
        "mitre_tactic": "Credential Access",
        "mitre_technique": "T1110.003"
    },

    "MULTI_STAGE_ATTACK": {
        "severity": "CRITICAL",
        "confidence": 100,
        "description": "Multiple attack techniques were correlated from the same source IP, indicating a coordinated multi-stage attack.",
        "recommendation": "Immediately investigate the affected host, isolate it from the network if necessary, and initiate the incident response process.",
        "mitre_tactic": "Multiple",
        "mitre_technique": "Multiple"
    }

}