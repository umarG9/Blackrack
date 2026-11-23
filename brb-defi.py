import hashlib, random
class BRBDeFiProtocol:
    def __init__(self):
        self.total_staked = 0
        self.bullish = 78
        self.stakers = {}
    def stake(self, user, amt):
        tx = "0x" + hashlib.sha256(f"{user}{amt}".encode()).hexdigest()[:12]
        reward = amt * 78/100/365
        self.stakers[user] = {"staked": amt, "rewards": reward}
        self.total_staked += amt
        return {"user": user, "staked": amt, "apy": "78% Bullish", "reward_per_day": reward, "tx": tx, "type": "STAKING NFT - DEFI"}
    def lend(self, user, amt):
        return {"user": user, "lent": amt, "apy": "22%", "interest": amt*22/100/365}
    def add_liquidity(self, user, brb, usdt):
        lp = (brb*usdt)**0.5
        return {"pool": f"BRB/USDT-{random.randint(1000,9999)}", "brb": brb, "usdt": usdt, "lp": lp, "type": "LP NFT - DEX"}
    def yield_farm(self, user, lp):
        return {"user": user, "lp": lp, "apy": "120% Super Bullish", "reward": lp*120/100/365}
    def swap(self, user, from_t, to_t, amt):
        rate = 0.01 if from_t=="BRB" else 100
        rec = amt*rate if from_t=="BRB" else amt/rate
        fee = amt*0.003
        return {"from": from_t, "to": to_t, "amount": amt, "received": rec, "fee": fee}

print(BRBDeFiProtocol().stake("Musa", 1000))
