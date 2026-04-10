def find_positive_pairs(batch_labels):
    pairs = []
    batch_size = len(batch_labels)
    
    # Comparing every label against every other label
    for i in range(batch_size):
        for j in range(i + 1, batch_size):
            if batch_labels[i] == batch_labels[j]:
                pairs.append((i, j))
                
    return pairs
