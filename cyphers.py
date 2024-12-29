import string

# 1. importing the file and removing all the special characters and taking only letters
def textstrip(filename):
    with open(filename, 'r') as file:
        text = file.read()
    stripped_text = ''.join(filter(lambda x: x in string.ascii_lowercase, text.lower()))
    return stripped_text

# 2. dictionary for frequency distribution of alphabets
def letter_distribution(s):
    distribution = {letter: s.count(letter) for letter in string.ascii_lowercase}
    return distribution

# 3. encrypting the text using dictionary d which comprises of the substitutions for the 26 letters
def substitution_encrypt(s, d):
    encrypted_text = ''.join(d[letter] for letter in s)
    return encrypted_text

# 4. decrypting the text using same dictionary d
def substitution_decrypt(s, d):
    reversed_d = {v: k for k, v in d.items()}
    decrypted_text = ''.join(reversed_d[letter] for letter in s)
    return decrypted_text

# 5. predicting the dictionary d
def cryptanalyse_substitution(s):
    # Frequency of letters in the English language (in decreasing order)
    english_freq = "etaoinshrdlcumwfgypbvkjxqz"
    
    # Get the distribution of letters in the encrypted string
    distribution = letter_distribution(s)
    
    # Sort the letters by frequency in the encrypted string
    sorted_letters = sorted(distribution, key=distribution.get, reverse=True)
    
    # Create the substitution dictionary based on frequency analysis
    predicted_d = {sorted_letters[i]: english_freq[i] for i in range(len(english_freq))}
    
    return predicted_d

# 6. encrypting the text from password the vigenere cipher way
def vigenere_encrypt(s,password):
    keyword_repeated = (password * (len(s) // len(password))) + password[:len(s) % len(password)]
    cipher_text = ""
    
    for i in range(len(s)):
        shift = ord(keyword_repeated[i]) - ord('a')
        cipher_text += chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
    
    return cipher_text

# 7. decrypting the text using password
def vigenere_decrypt(s,password):
    keyword_repeated = (password * (len(s) // len(password))) + password[:len(s) % len(password)]
    decrypted_text = ""
    
    for i in range(len(s)):
        shift = ord(keyword_repeated[i]) - ord('a')
        decrypted_text += chr(((ord(s[i]) - ord('a') - shift) % 26) + ord('a')) 

    return decrypted_text

# 8. rotate the string by r and return the proportion of collisions
def rotate_compare(s, k):
    coincidences = 0
    # Compare characters that are k positions apart
    for i in range(len(s) - k):
        if s[i] == s[i + k]:
            coincidences += 1
    return coincidences
 
# 9. find password from the given vigenere cipher text where length of password is given
def cryptanalyse_vigenere_afterlength(s, k):
    password = ""
    for i in range(k):
        # Extract every k-th character starting from index i
        substr = s[i::k]
        # Find the most frequent character in the substring
        most_common_char = max(set(substr), key=substr.count)
        # Deduce the corresponding character in the original text
        decrypted_char = chr((ord(most_common_char) - ord('e')) % 26 + ord('a'))
        password += decrypted_char
    return password

# 10. find the lenght of password
def cryptanalyse_vigenere_findlength(s):
    max_length = 75
    min_length = 5
    max_coincidence = 0
    best_k = min_length  # Start with the minimum length as the best candidate
    z = 0

    for k in range(min_length, max_length + 1):
        # Use rotate_compare to get total coincidences for this k
        total_coincidences = rotate_compare(s, k)

        # Normalize coincidences based on total comparisons
        total_comparisons = len(s) - k
        if total_comparisons > 0:
            average_coincidence = total_coincidences / total_comparisons
            
            # Update best_k if the current average is higher
            if average_coincidence > max_coincidence:
                max_coincidence = average_coincidence
                best_k = k

    return best_k 

# 11. finding password and decrypting the text
def cryptanalyse_vigenere(s):
    length_of_password = cryptanalyse_vigenere_findlength(s)
    password = cryptanalyse_vigenere_afterlength(s, length_of_password)
    plain_text = vigenere_decrypt(s, password)

    return password, plain_text