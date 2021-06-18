from flask import Flask

valid_tokens = {
    'Y0ZfDzTm1n': ['UserManager', 'Jenna'],
    '9uHSi2hnKD': ['AppUser', 'Robin'],
}


roles = {
    'Administrator': {
        'UserManager': {
            'KYCApprover': {},
            'SupportManager': {},
        },
        'WalletManager': {
            'FraudMonitor': {},
            'AppUser': {'WalletUser': {}},
        },
    },
}

app = Flask(__name__)


@app.route('/user/', methods=['GET', 'POST'])
def fetch_user():
    token = '9uHSi2hnKD'

    role = get_role(token)

    if role is not None:
        s = list(findkeys(roles, role))

        return check_role(token, s)
    # return "Hello World!"


def get_role(token):
    if token in valid_tokens:
        role = valid_tokens[token][0]
        return role
    else:
        return None


def get_name(token):
    if token in valid_tokens:
        name = valid_tokens[token][1]
        return name
    else:
        return None


def check_role(token, lis):
    name = get_name(token)

    if 'WalletUser' in lis[0]:

        balance = 1000
        return "User name is" + " " + name + " " + "and the balance is " + "" + "$" + str(balance)

    else:
        return "User name is" + " " + name


def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
                yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
