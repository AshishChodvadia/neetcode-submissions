class Solution:
    '''
    #strs = ["Hello", "World"]
    "5#Hello5#World"
     01234567
    i=0
    hash_index=1
    start=2
    length=5
    word=Hello
    '''
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string +  str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
           hash_index = s.find("#", i)
           length = int(s[i:hash_index])
           start = hash_index + 1
           word = s[start:start + length]
           decoded_strs.append(word)
           i = start + length
        return decoded_strs
