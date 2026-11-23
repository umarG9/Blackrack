import hashlib
class BRBInterchainBridge:
    def bridge(self, user, from_c, to_c, amt):
        bid = f"BRB-BRIDGE-{from_c.upper()}-TO-{to_c.upper()}"
        wrapped = amt * 0.99
        fee = amt * 0.01
        return {"bridge_id": bid, "from": from_c, "to": to_c, "amount": amt, "wrapped": wrapped, "fee": fee, "type": f"INTERCHAIN BRIDGE NFT - {from_c}→{to_c}"}

print(BRBInterchainBridge().bridge("Musa", "BRB", "ETH", 10000))
