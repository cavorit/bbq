import re

richtig = ["2017-12-24", "2017-12-31", "1983-11-03", "2000-01-01"]
falsch = ["Jana", "2017:24-17", "2017-24-1", "2011-00-12", "1999-32-10",
        "22112-01-02", "3-0-1998"]

pattern = r"([0-9]{4})-(0[1-9]|1[0-2])-(([0-2][0-9])|(3[0|1]))"

def testMatch(pattern, text):
    
    for txt in text:
        m = re.search(pattern, txt)

        if (m == None):
            print("%s ist KEIN Match" % (txt))
        else:
            print("%s ist ein Match" % (txt))





if __name__ == "__main__":
    testMatch(pattern = pattern, text = richtig)
    testMatch(pattern = pattern, text = falsch)          




