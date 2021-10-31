import ipaddress

def validate_ip_address(input1):
    try:
        ip1 = ipaddress.ip_address(input1)
        return f"IP address {ip1} is valid"
    except ValueError:
        raise ValueError(f"IP address {input1} is not valid")

def get_ip_class(input1):
    ip = input1.split(".")
    ip = [int(i) for i in ip]
    if ip[0] >= 0 and ip[0] <= 127:
        return f"The ip address {input1} belongs to class A"
    elif ip[0] >= 128 and ip[0] <= 191:
        return f"The ip address {input1} belongs to class B"
    elif ip[0] >= 192 and ip[0] <= 223:
        return f"The ip address {input1} belongs to class C"
    else:
        return f"The ip address {input1} does not belongs to class A, B or C"