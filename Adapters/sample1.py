class Analytic:
    def request(self):
        return "Target: json data"
    
class StockData:
    def data(self):
        return "provide xml data" 
    
class Adapter(Analytic):
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def request(self):
        print("converting...")
        json = self.to_json(self.stock_data.data())
        print("origanizing data...")
        return f"Adapter: (Translated to json) {json}"
    
    def to_json(self, stock_data):
        return "provide json data"
    
def client_code(target):
    print(target.request())
    
if __name__ == "__main__":
    stock_data = StockData()
    adapter = Adapter(stock_data)
    client_code(adapter)