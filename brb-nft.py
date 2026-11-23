import hashlib, time, random
class BRBNFTMarketplace:
    def __init__(self):
        self.nfts = {}
        self.listings = {}
        self.owners = {}
        self.total_volume = 0
        self.floor_price = 100
    def mint_student_nft(self, name, cls, score):
        nft_id = f"BRB-STUDENT-{hashlib.sha256(f'{name}{time.time()}'.encode()).hexdigest()[:8].upper()}"
        tx = "0x" + hashlib.sha256(f"{name}".encode()).hexdigest()[:12]
        nft = {"id": nft_id, "owner": name, "brb": 100, "price": 100, "tx": tx, "type": "Student NFT"}
        self.nfts[nft_id] = nft
        self.owners[nft_id] = name
        return nft
    def list_nft(self, nft_id, price):
        self.listings[nft_id] = {"price": price}
        return {"listed": nft_id, "price": price}
    def buy_nft(self, nft_id, buyer):
        price = self.listings[nft_id]["price"]
        seller = self.owners.get(nft_id, "BRB")
        tx = "0x" + hashlib.sha256(f"{nft_id}{buyer}".encode()).hexdigest()[:12]
        self.owners[nft_id] = buyer
        self.total_volume += price
        del self.listings[nft_id]
        return {"bought": nft_id, "buyer": buyer, "seller": seller, "price": price, "tx": tx, "volume": self.total_volume}

m = BRBNFTMarketplace()
nft = m.mint_student_nft("Aisha", "JSS1", 95)
print(nft)
