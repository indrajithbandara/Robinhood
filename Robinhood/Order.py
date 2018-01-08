
import json
class Order:
    def __init__(self,json_str,trader,url_directly = False):
        if url_directly:
            self.order = json_str
        else:
            self.order = json.loads(json_str)['url']
        self.trader = trader
    def cancel(self):
        return json.loads(self.trader.session.post(self.order+'cancel/').text)
    def check(self):
        return json.loads(self.trader.session.get(self.order).text)
    def get_state(self):
        return self.check()['state']
    def quantity(self):
        return self.check()['quantity']
    def average_price(self):
        return self.check()['average_price']
    def executions(self):
        return self.check()['executions']
    def created_at(self):
        return self.check()["created_at"]