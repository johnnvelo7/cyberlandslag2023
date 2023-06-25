from Cryptodome.Util.number import bytes_to_long

class MysteryGroup:

    state = [["U"]*9, ["R"]*9, ["F"]*9, ["D"]*9, ["L"]*9, ["B"]*9]
    gen_names = "URFDLB"

    def __str__(self):
        return "".join([l for face in self.state for l in face])

    def rotate(self, face):
        newface = [0]*9
        newface[0] = face[6]
        newface[1] = face[3]
        newface[2] = face[0]
        newface[3] = face[7]
        newface[4] = face[4]
        newface[5] = face[1]
        newface[6] = face[8]
        newface[7] = face[5]
        newface[8] = face[2]
        return newface

    def U(self):
        state = self.state.copy()
        self.state[0] = self.rotate(state[0].copy())
        self.state[1] = state[5][0:3] + state[1][3:]
        self.state[2] = state[1][0:3] + state[2][3:]
        self.state[4] = state[2][0:3] + state[4][3:]
        self.state[5] = state[4][0:3] + state[5][3:]

    def R(self):
        state = self.state.copy()
        self.state[1] = self.rotate(state[1].copy())
        self.state[0] = state[0][0:2] + [state[2][2]] + state[0][3:5] + [state[2][5]] + state[0][6:8] + [state[2][8]]
        self.state[5] = [state[0][8]] + state[5][1:3] + [state[0][5]] + state[5][4:6] + [state[0][2]] + state[5][7:]
        self.state[3] = state[3][0:2] + [state[5][6]] + state[3][3:5] + [state[5][3]] + state[3][6:8] + [state[5][0]]
        self.state[2] = state[2][0:2] + [state[3][2]] + state[2][3:5] + [state[3][5]] + state[2][6:8] + [state[3][8]]

    def F(self):
        state = self.state.copy()
        self.state[2] = self.rotate(state[2].copy())
        self.state[0] = state[0][:6] + [state[4][8], state[4][5], state[4][2]]
        self.state[1] = [state[0][6]] + state[1][1:3] + [state[0][7]] + state[1][4:6] + [state[0][8]] + state[1][7:]
        self.state[3] = [state[1][6], state[1][3], state[1][0]] + state[3][3:]
        self.state[4] = state[4][0:2] + [state[3][0]] + state[4][3:5] + [state[3][1]] + state[4][6:8] + [state[3][2]]

    def D(self):
        state = self.state.copy()
        self.state[3] = self.rotate(state[3].copy())
        self.state[1] = state[1][0:6] + state[2][6:]
        self.state[5] = state[5][0:6] + state[1][6:]
        self.state[4] = state[4][0:6] + state[5][6:]
        self.state[2] = state[2][0:6] + state[4][6:]

    def L(self):
        state = self.state.copy()
        self.state[4] = self.rotate(state[4].copy())
        self.state[0] = [state[5][8]] + state[0][1:3] + [state[5][5]] + state[0][4:6] + [state[5][2]] + state[0][7:]
        self.state[2] = [state[0][0]] + state[2][1:3] + [state[0][3]] + state[2][4:6] + [state[0][6]] + state[2][7:]
        self.state[3] = [state[2][0]] + state[3][1:3] + [state[2][3]] + state[3][4:6] + [state[2][6]] + state[3][7:]
        self.state[5] = state[5][0:2] + [state[3][6]] + state[5][3:5] + [state[3][3]] + state[5][6:8] + [state[3][0]]

    def B(self):
        state = self.state.copy()
        self.state[5] = self.rotate(state[5].copy())
        self.state[0] = [state[1][2], state[1][5], state[1][8]] + state[0][3:]
        self.state[4] = [state[0][2]] + state[4][1:3] + [state[0][1]] + state[4][4:6] + [state[0][0]] + state[4][7:]
        self.state[3] = state[3][0:6] + [state[4][0], state[4][3], state[4][6]]
        self.state[1] = state[1][0:2] + [state[3][8]] + state[1][3:5] + [state[3][7]] + state[1][6:8] + [state[3][6]]

    def action(self, element):
        for g in element:
            self.gens[self.gen_names.index(g)](self)

    gens = [U, R, F, D, L, B]



def base6(num,numerals="URFDLB"):
    return ((num == 0) and numerals[0]) or (base6(num // 6, numerals).lstrip(numerals[0]) + numerals[num % 6])

def encrypt(message, e, group):
    m = base6(bytes_to_long(message))
    for _ in range(e):
        group.action(m)

secret = b"?????"
flag = "flag{" + secret.decode() + "}"
G = MysteryGroup()
e = 65537

encrypt(secret, e, G)

print(f"ct = {G}")
print(f"Generators applied {len(base6(bytes_to_long(secret)))} times")
