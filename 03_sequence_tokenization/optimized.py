def tokenize_sequences(dataset, delimiter="|"):
    processed_data = []
    for sequence in dataset:
        # Pre-allocates memory and joins in a single C-level operation
        token_string = delimiter.join(sequence)
        processed_data.append(token_string)
        
    return processed_data
