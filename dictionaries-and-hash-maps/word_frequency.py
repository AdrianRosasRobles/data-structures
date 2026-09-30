def count_word_frequency(text): 
    counts = {}
    
    words = text.split()
    
    for word in words: 
        if word in counts: 
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts

text_input = "dog cat dog bird cat dog"
result = count_word_frequency(text_input)
print(result)
