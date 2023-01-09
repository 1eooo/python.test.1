# [:n] : slice

t = "korea"

print(t)
print(t[:1])
print(t[:2])
print(t[:3])
print(t[:4])
print(t[:5])
print(t[:])

print(t is t[:])
print(t is t[:1])
print(t is t[:2])
print(t is t[:3])


# korea
# k
# ko
# kor
# kore
# korea
# korea

# True

# False
# False
# False