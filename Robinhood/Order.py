
import json
class Order:
    def __init__(self,json_str,trader,url_directly = False):
        assert trader is not None
        self.trader = trader
        if url_directly:
            self.order = json_str
        else:
            try:
                self.order = json.loads(json_str)['url']
            except:
                print(json_str)
                self.order = None
        
        
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