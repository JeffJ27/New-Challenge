################################################################################
# Configure a box for the custom web example challenge.
################################################################################


import sys
import os
import re
import json



def main():

    new_flag = "picoCTF{th15_15_my"+"_f1r5t_fla9}"
    

    # Create and update metadata.json =====================================

    metadata = {}
    metadata['flag'] = str(new_flag)
    json_metadata = json.dumps(metadata)
    
    with open("metadata.json", "w") as f:
        f.write(json_metadata)

    # =====================================================================


# =============================================================================


if __name__ == "__main__":
    main()