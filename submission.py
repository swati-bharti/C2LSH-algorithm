## import modules here

########## Question 1 ##########
# do not change the heading of the function
def count(hashes_1, hashes_2, offset):
    counter = 0
    for hash1, hash2 in zip(hashes_1, hashes_2): # (hash1 hash2)
        if abs(hash1 - hash2) <= offset:
            counter += 1




   



def c2lsh(data_hashes, query_hashes, alpha_m, beta_n):
    offset = 0
    cand = None
    while True:
        #filtering the none value
        cand = data_hashes.map(lambda hash : hash[0] if count(hash[1], query_hashes, offset) >= alpha_m else None).filter(lambda hash: hash != None) # method chaining
        #cand = cand.filter(lambda hash: hash != None)
        if cand.count() < beta_n:
            offset += 1
        else:
            break
    return cand

