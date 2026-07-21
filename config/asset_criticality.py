ASSET_CRITICALITY = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}

ASSET_METADATA = {
    "/login": {
        "criticality": "CRITICAL"
    },
    "/register": {
        "criticality": "HIGH"
    },
    "/dashboard": {
        "criticality": "HIGH"
    },
    "/users": {
        "criticality": "HIGH"
    },
    "/admin": {
        "criticality": "CRITICAL"
    },
    "/config": {
        "criticality": "CRITICAL"
    },
    "/reports": {
        "criticality": "HIGH"
    },
    "/metrics": {
        "criticality": "MEDIUM"
    },
    "/settings": {
        "criticality": "HIGH"
    },
    "/api": {
        "criticality": "CRITICAL"
    }
}