from config.asset_criticality import (
    ASSET_METADATA, 
    ASSET_CRITICALITY
)
def get_asset_criticality(resource : str) -> str:
    asset = ASSET_METADATA.get(resource)
    if asset is None:
        return "MEDIUM"
    return asset["criticality"]

def get_asset_criticality_score(resource : str) -> int:
    criticality = get_asset_criticality(resource)
    return ASSET_CRITICALITY[criticality]