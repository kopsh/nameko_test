# coding=utf-8
'''
BEGIN
function:
    Push Service
END
'''

from nameko.rpc import RpcProxy, rpc


class PushService(object):

    name = "push"

    register_rpc = RpcProxy("register")

    @rpc
    def push(self, u_id, content):
        user_data = self.register_rpc.check_registered(u_id)
        if not user_data:
            print("User {} not existed".format(u_id))
            return False, "not register"

        language, country = user_data["language"], user_data["country"]

        # get language push content
        print("Push Progress: u_id: {} language: {}, country: {}, content: {}".
              format(u_id, language, country, content))

        return True, "push success."
