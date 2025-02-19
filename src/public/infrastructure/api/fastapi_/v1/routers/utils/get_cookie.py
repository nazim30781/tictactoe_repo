def get_cookie(data: str) -> dict:
    cookie_data = data.split("; ")
    cookie_data = [_.split("=") for _ in cookie_data]

    cookie = dict()

    for i in cookie_data:
        cookie[i[0]] = i[1]

    return cookie
