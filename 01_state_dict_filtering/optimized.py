def clean_state_dict(loaded_dict, expected_keys):
    # O(n) Dictionary comprehension
    new_dict = {k.replace("module.", ""): v for k, v in loaded_dict.items()}
    
    # O(1) lookups using Set difference
    missing_keys = list(set(expected_keys) - set(new_dict.keys()))
            
    return new_dict, missing_keys
