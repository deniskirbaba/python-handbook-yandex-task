def secret_replace(msg, **kwargs):
    encoded_msg = ''
    freq = dict()
    for i, ch in enumerate(msg):
        if ch in kwargs.keys():
            if not isinstance(kwargs[ch], tuple):
                encoded_msg += kwargs[ch]
            else:
                encoded_msg += kwargs[ch][freq.setdefault(ch, 0) % len(kwargs[ch])]
                freq[ch] += 1
        else:
            encoded_msg += ch
    return encoded_msg


result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)
