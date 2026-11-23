import hashlib, time
class BlackRackBlockchainFutureFinal:
    def __init__(self):
        self.total_supply = 0
    def mint(self, t, n, a):
        self.total_supply += a
        return {"name": n, "brb": a, "type": t}
    def week1_14_mint(self):
        self.total_supply = 0
        [self.mint("ROBOT", f"ROBOT {i}", 1000) for i in range(1,11)]
        [self.mint("STUDENT", f"STUDENT {i}", 100) for i in range(1,101)]
        [self.mint("DEFI STAKING", f"DEFI STAKING {i} - 78% APY", 1000) for i in range(1,101)]
        [self.mint("NFT", f"NFT MARKETPLACE {i}", 100) for i in range(1,101)]
        self.mint("BONUS", "BONUS 1M BRB - 11 HOUSES", 50000)
    def week15_20_future_mint(self):
        [self.mint("FUTURE AGI", f"AGI {i}", 1000) for i in range(1,51)]
        [self.mint("FUTURE METAVERSE", f"METAVERSE WORLD {i}", 1000) for i in range(1,51)]
        [self.mint("FUTURE QUANTUM", f"QUANTUM TX {i}", 500) for i in range(1,101)]
        [self.mint("FUTURE DAO", f"DAO PROPOSAL {i}", 1000) for i in range(1,51)]
        [self.mint("FUTURE INTERCHAIN", f"INTERCHAIN BRIDGE {i}", 1000) for i in range(1,51)]
        [self.mint("FUTURE GLOBAL", f"GLOBAL SCALE {i}", 1000) for i in range(1,101)]
        self.mint("BONUS FUTURE", "BONUS FINAL ULTIMATE - 10M BRB $100K", 200000)
    def token_to_cash(self):
        return {"total_brb": self.total_supply, "value": self.total_supply*0.01, "conservative": "$100K/month", "roi": "0.2 months"}

brb = BlackRackBlockchainFutureFinal()
brb.week1_14_mint()
brb.week15_20_future_mint()
print(brb.token_to_cash())
