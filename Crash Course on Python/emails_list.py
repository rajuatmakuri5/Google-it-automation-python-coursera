def email_list(domains):
	emails = []
	for dn,userslist in domains.items():
		for user in userslist:
			emails.append(user+ "@" +dn)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                  "yahoo.com": ["barbara.gordon", "jean.grey"],
                  "hotmail.com": ["bruce.wayne"]}))
