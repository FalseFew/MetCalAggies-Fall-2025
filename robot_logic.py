def dh_transform(a, alpha, d, theta):
    ca, sa = np.cos(alpha), np.sin(alpha)
    ct, st = np.cos(theta), np.sin(theta)
    return np.array([
        [ct, -st*ca,  st*sa, a*ct],
        [st,  ct*ca, -ct*sa, a*st],
        [0,   sa,     ca,    d],
        [0,   0,      0,     1]
    ])

class SimpleRobot:
    def __init__(self):
        self.a = [7, 6, 4, 5, 3, 2, 1.5]
        self.alpha = [np.pi/2, 0, -np.pi/2, np.pi/2, -np.pi/2, np.pi/2, 0]
        self.d = [0.0]*7
        self.dof = 7

    def fk(self, q):
        T = np.eye(4)
        pts = [(0,0,0)]
        for i in range(self.dof):
            Ti = dh_transform(self.a[i], self.alpha[i], self.d[i], q[i])
            T = T @ Ti
            pts.append(T[:3,3])
        return np.array(pts)



