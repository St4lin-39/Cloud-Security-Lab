ALERT_METADATA = {
    "BRUTE_FORCE_ATTEMPT": {
        "severity": "MEDIUM",
        "description": "Multiple failed authentication attempts detected for the same user within a short period of time.",
        "recommendation": "Temporarily lock the account and investigate the originating IP address."
    },

    "RESOURCE_ENUMERATION": {
        "severity": "LOW",
        "description": "Multiple protected resources were accessed in a short period of time.",
        "recommendation": "Review access logs and verify whether the activity is legitimate."
    },

    "CREDENTIAL_STUFFING": {
        "severity": "HIGH",
        "description": "Multiple usernames were targeted from the same IP address using different credentials.",
        "recommendation": "Investigate the source IP and force password resets for affected accounts if necessary."
    },

    "PASSWORD_SPRAYING": {
        "severity": "HIGH",
        "description": "A single password was attempted against multiple user accounts.",
        "recommendation": "Block the source IP and investigate potential password spraying activity."
    },

    "MULTI_STAGE_ATTACK": {
        "severity": "CRITICAL",
        "description": "Multiple attack techniques were correlated from the same source IP.",
        "recommendation": "Immediately investigate the host and consider isolating the source from the network."
    }
}