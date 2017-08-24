import re

richtig = ["24-12-2017", "31-12-2017", "03-11-1983"]
falsch = ["Jana", "24-12:2017", "24-13-2017", "00-12-2011", "32-10-1999",
        "01-01-22112", "3-0-1998", "1-1-2019"  ]

myRegex =  r'((0[1-9])|([12][0-9])|(3[01]))-((0[1-9])|(1[0-2]))-([0-9]{4})'




def date_tester(pattern, text):
    
    for txt in text:
        m = re.search(pattern, txt)
        if m:
            print('%s is a match' % (txt))
        else:
            print('%s is NOT a match' % (txt))

if __name__ == "__main__":
    date_tester(pattern = myRegex, text=richtig)
    date_tester(pattern = myRegex, text=falsch)


