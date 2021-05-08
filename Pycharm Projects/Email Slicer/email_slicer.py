your_email = input("Hey Boss.... Enter your email : ")
name, domain = your_email.split("@")

popular_domains = ("Gmail", "Aol", "Outlook", "Zoho", "Mail", "Yahoo", "ProtonMail", "iCloud")

name_final = name.split(".")[0]
domain_final = domain.split(".")[0].title()

print(name_final, domain_final)

if domain_final in popular_domains:
    print("Hey {} is a pretty popular domain indeed... good work ".format(domain_final))
else:
    print("{} is a pretty unique domain indeed... good work ".format(domain_final))

