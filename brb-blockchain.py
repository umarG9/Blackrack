import hashlib, time
class BlackRackBlockchain:
    def __init__(self):
        self.total_supply = 0
        self.brb_price = 0.01
        self.bullish = 78
    def mint(self, typ, name, amt):
        self.total_supply += amt
        tx = "0x" + hashlib.sha256(f"{name}{time.time()}".encode()).hexdigest()[:12]
        return {"name": name, "brb": amt, "tx": tx, "type": typ}
    def town_to_token(self):
        for i in range(1,11): self.mint("ROBOT", f"ROBOT TEACHER {i}", 1000)
        for i in range(1,31): self.mint("STUDENT", f"STUDENT {i} WEEK1", 100)
    def token_to_cash(self):
        return {"total_brb": self.total_supply, "value": self.total_supply*0.01, "fees": 45, "total": 45+self.total_supply*0.01}

brb = BlackRackBlockchain()
brb.town_to_token()
print(brb.token_to_cash())
