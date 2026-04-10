def tokenize_sequences(dataset, delimiter="|"):
    processed_data = []
    for sequence in dataset:
        token_string = ""
        # String immutability causes memory reallocation on every +=
        for char in sequence:
            token_string += char + delimiter
        processed_data.append(token_string[:-1])
        
    return processed_data
