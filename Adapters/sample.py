class Target:
    def request(self):
        return "Target: default target's behavior"
    
class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS" 
    
class Adapter(Target, Adaptee):
    def request(self):
        return f"Adapter: (Translated) {self.specific_request()[::-1]}"
    
def client_code(target):
    print(target.request())
    
if __name__ == "__main__":
    target= Target()
    client_code(target)
    
    adapter = Adapter()
    client_code(adapter)