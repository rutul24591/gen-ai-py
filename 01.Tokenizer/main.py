import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Rutul Amin"

encodedTokens = enc.encode(text)

# ENCODED Tokens  [25216, 1354, 0, 3673, 1308, 382, 80390, 361, 82448]
print("ENCODED Tokens ", encodedTokens)

decodedTokens = enc.decode([25216, 1354, 0, 3673, 1308, 382, 80390, 361, 82448])

# DECODED TOKENS Hey there! My name is Rutul Amin
print("DECODED TOKENS ", decodedTokens)
