from flask import Flask
app = Flask(__name__)
robots = [{"id":i, "name":f"ROBOT {i} AI TEACHER", "brb":1000} for i in range(1,11)]

@app.route('/robot/<int:id>/speak')
def robot_speak(id):
    r = robots[id-1]
    return {"robot": r["name"], "speak": f"I am {r['name']} - 1000 BRB NFT", "brb":1000}

if __name__ == '__main__':
    app.run(port=5001)
