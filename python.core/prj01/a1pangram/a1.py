def isPangram(s):
    lc = "abcdefghijklmnopqrstuvwxyz"
    for ch in lc:
        if ch not in s.lower():
            return False
    return True
ip = "The QUICK brown Fox jumps Over the LAZY dog"
if isPangram(ip):
    print(f"Pangram: {ip}")
else:
    print(f"Not Pangram: {ip}")
'''
Pangram: The QUICK brown Fox jumps Over the LAZY dog      
'''