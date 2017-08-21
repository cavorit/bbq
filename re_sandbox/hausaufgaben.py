import re, daten, regex

def testMatch(pattern, text):

    regex = re.compile(pattern)
    results = []

    while len(text):
        txt = text.pop()
        match = regex.match(txt)
        if match:
            print('%s is a match' % (txt))           
            results.append(True)  
        else:
            print('%s is no match' % (txt))
            results.append(False)           

    return results 

if __name__ == "__main__":
    testMatch(pattern = regex.regex, text = daten.richtig)
    testMatch(pattern = regex.regex, text = daten.falsch)          




