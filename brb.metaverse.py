import hashlib
class BRBMetaverseWorld:
    def __init__(self):
        self.worlds = {}
        self.avatars = {}
    def create_world(self, name, houses):
        wid = f"BRB-WORLD-{hashlib.sha256(name.encode()).hexdigest()[:8].upper()}"
        brb = houses * 1000
        self.worlds[wid] = {"name": name, "brb": brb}
        return {"world_id": wid, "name": name, "houses": houses, "brb": brb, "type": "METAVERSE WORLD NFT"}
    def create_avatar(self, user, house):
        aid = f"BRB-AVATAR-{user.upper()}-{house.upper()}"
        return {"avatar_id": aid, "user": user, "house": house, "brb": 100, "type": "AVATAR NFT"}

print(BRBMetaverseWorld().create_world("BRB World - 12 Houses", 12))
