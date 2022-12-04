import re

# Add any aliases/name mappings here

NAME_MAP = {
    # blender_market_name: new_local_name
    "Learn How To Rig Anything In Blender | Fundamentals Of Rigging": "Fundamentals of Rigging",
    "Blender Secrets E-Book": "Blender Secrets",
    "Faceit : Facial Expressions And Performance Capture": "FaceIt",
    "Retopoflow 3 - Retopology Toolkit For Blender": "Retopoflow 3",
    "Danny Mac Eye Designer (Eevee / Cycles)": "Eye Designer",
    "Uvpackmaster 3": "UVPackMaster"
}

def rename(input: str):
    if input in NAME_MAP.keys():
        return NAME_MAP[input]



    folder_name = re.sub(r'[|.,+!@&*:;=&^%$#]+', '', input)
    folder_name = re.sub(r'[\s\-]+', ' ', folder_name)
    folder_name = re.sub(r'^[\s\-]+', '', folder_name)
    return folder_name