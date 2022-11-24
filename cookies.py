fh = open('cookies.txt', 'r')
cookies = "".join(fh.readlines())
cookies = cookies.split(";")
cookies = map(lambda x: x.split("="), cookies)
cookies = map(lambda x: (x[0], x[1]), cookies)

cookies_list = list(cookies)
cookies = dict(cookies_list)
pass
