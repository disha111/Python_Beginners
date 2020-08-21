def StripPunctuation(s):
    answer=""
    for c in s:
        if c.islower() or c.isupper():
            answer=answer+c.lower()
    return answer
def Reverse(s):
    answer=""
    for c in s:
        answer=c+answer
    return answer
def IsPalindrome(s):
    s=StripPunctuation(s)
    if s==Reverse(s):
        return True
    else:
        return False
def main():
    F=open("file.txt","r")
    for line in F:
        word=line.strip("\n")
    if IsPalindrome(word):
        print (word)

main()