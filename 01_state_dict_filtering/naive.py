def clean_state_dict(loaded_dict, expected_keys):
    new_dict = {}
    missing_keys = []
    
    # Inefficient dictionary rebuild
    for key, value in loaded_dict.items():
        clean_key = key.replace("module.", "")
        new_dict[clean_key] = value
        
    # O(n*m) missing key check
    for key in expected_keys:
        found = False
        for current_key in new_dict.keys():
            if key == current_key:
                found = True
        if not found:
            missing_keys.append(key)
            
    return new_dict, missing_keys
