import re
codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
            ]
match =r"[A-Z]{1,2}\w?\S.\d[A-Z]{2}"
valid = []
invalid = []
for pc in codes:
     r = re.search(match,pc)
     if r:
          valid.append(pc)
     else:
          invalid.append(pc)
print("Valid Postel Codes are : ")
for i in valid:
     print(i)

print("\nIn-Valid Postel Codes are : ")
for j in invalid:
     print(j)
