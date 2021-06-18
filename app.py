from flask import Flask
from flask import request, make_response, jsonify

User = {
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


def verify_auth_token(auth_header):
    try:
        if auth_header:
            auth_token = auth_header.split(" ")[1]
            user = User[auth_token]
            return auth_token, user
    except:
        return None


@app.route('/user/', methods=['GET', 'POST'])
def fetch_user():
    auth_header = request.headers.get('Authorization')

    user = verify_auth_token(auth_header)

    if user is not None:
            s = list(find_role(roles, user[1][0]))
            return user_response(user[0], s)
    else:
        return 'Invalid token. Please log in again.'


def user_response(token, lis):
    balance = 1000

    if 'WalletUser' in lis[0]:
        responseObject = {
            'status': 'success',
            'data': {
                'username': User[token][1],
                'balance': balance

            }
        }
        return make_response(jsonify(responseObject)), 200

    else:
        responseObject = {
            'status': 'success',
            'data': {
                'username': User[token][1]

            }
        }
        return make_response(jsonify(responseObject)), 200


def find_role(node, kv):
   if isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in find_role(j, kv):
                yield x


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
