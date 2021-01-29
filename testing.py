with open('smtpaccs.txt', 'r', encoding='utf-8') as smtps:
    to_dict = lambda x: {'host': x[0], 'port': x[1], 'login': x[2], 'password': x[3]}
    smtp_list = [to_dict(smtp.split(':')) for smtp in list(map(lambda x: x.replace('\n', ''), smtps.readlines()))]
print(smtp_list)
