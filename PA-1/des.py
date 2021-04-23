from DESfiddle.utils import *

# Inputs in binary setting
plaintext = "0101010101010101"
key = "01010101010101010101010101010101"

# Settings
nor = 16
halfwidth = 64
hamming_dist = 1

# Hamming the plaintext in binary mode
ref_pt_arr = preprocess_plaintext(plaintext, halfwidth)
pt_arr = preprocess_plaintext(plaintext, halfwidth, hamming_dist)
# preprocess key that to be used in each round
key = preprocess_key(key, halfwidth)
# generate round keys
rkb,rkh = generate_round_keys(key,nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(ref_pt_arr, rkb, nor, halfwidth)
# getting round cipher text
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
# calculating the difference
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)

# Hamming the key in binary mode
pt_arr = preprocess_plaintext(plaintext, halfwidth)
ref_key = preprocess_key(key,halfwidth)
key = preprocess_key(key, halfwidth, hamming_dist)
ref_rkb, ref_rkh = generate_round_keys(ref_key, nor, halfwidth)
rkb,_ = generate_round_keys(key, nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(pt_arr, ref_rkb, nor, halfwidth)
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)