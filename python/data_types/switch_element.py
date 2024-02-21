# python switch - /match/ introduced python 3.10 version
# better than if elif else for multiple conditions

http_status = 201

match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Not Found')
    case 500 | 501:
        print('Server Error')
    case _:
        print('Unknown')