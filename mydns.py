import dns.resolver as dns_resolver

mx_records = dns_resolver.resolve('www.qq.com', 'a')

for i in mx_records:
    print(i)
