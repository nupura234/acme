from flask import Flask
from flask import request
from flask_restful import Resource, Api


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
api = Api(app)


def verify_auth_token(auth_header):
    try:
        if auth_header:
            auth_token = auth_header.split(" ")[1]
            user = User[auth_token]
            return auth_token, user
    except:
        return None


class Users(Resource):

    def get(self):
        auth_header = request.headers.get('Authorization')

        user = verify_auth_token(auth_header)

        if user is not None:
            s = list(self.find_role(roles, user[1][0]))
            return self.user_response(user[0], s)
        else:
            return 'Invalid token. Please log in again.'

    def user_response(self, token, lis):
        balance = 1000

        if 'WalletUser' in lis[0]:
            responseObject = {
                'status': 'success',
                'data': {
                    'username': User[token][1],
                    'balance': balance

                }
            }
            return responseObject, 200

        else:
            responseObject = {
                'status': 'success',
                'data': {
                    'username': User[token][1]

                }
            }
            return responseObject, 200

    def find_role(self, node, kv):
        if isinstance(node, dict):
            if kv in node:
                yield node[kv]
            for j in node.values():
                for x in self.find_role(j, kv):
                    yield x



api.add_resource(Users, '/users')  # '/users' is our entry point for Users



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
