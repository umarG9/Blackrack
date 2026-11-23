import hashlib, time
class BRBDAO:
    def __init__(self):
        self.proposals = {}
    def create_proposal(self, creator, title, desc):
        pid = f"BRB-DAO-PROPOSAL-{hashlib.sha256(f'{title}{time.time()}'.encode()).hexdigest()[:8].upper()}"
        self.proposals[pid] = {"title": title, "votes_yes": 0, "votes_no": 0}
        return {"proposal_id": pid, "title": title, "type": "DAO PROPOSAL NFT"}
    def vote(self, voter, pid, yes, power):
        prop = self.proposals[pid]
        if yes: prop["votes_yes"] += power
        else: prop["votes_no"] += power
        status = "PASSED - Bullish 78%" if prop["votes_yes"] > prop["votes_no"] else "REJECTED"
        return {"voter": voter, "vote": "YES" if yes else "NO", "power": power, "yes": prop["votes_yes"], "no": prop["votes_no"], "status": status}

dao = BRBDAO()
p = dao.create_proposal("Musa", "Build House13 Space Lab", "Proposal")
print(dao.vote("Aisha", p["proposal_id"], True, 1000))
