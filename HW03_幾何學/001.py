import math
import matplotlib.pyplot as plt

# ==========================
# 幾何基礎類別
# ==========================

class Point:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __repr__(self):
        return f"Point({self.x:.3f}, {self.y:.3f})"

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor, center=None):
        if center is None:
            center = Point(0, 0)
        return Point(center.x + factor*(self.x - center.x),
                     center.y + factor*(self.y - center.y))

    def rotate(self, angle, center=None):
        if center is None:
            center = Point(0, 0)
        dx, dy = self.x - center.x, self.y - center.y
        cos_a, sin_a = math.cos(angle), math.sin(angle)
        return Point(center.x + dx*cos_a - dy*sin_a,
                     center.y + dx*sin_a + dy*cos_a)

class Line:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)

    def __repr__(self):
        return f"{self.a:.2f}x + {self.b:.2f}y + {self.c:.2f} = 0"

    @staticmethod
    def from_points(p1, p2):
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = -(a*p1.x + b*p1.y)
        return Line(a, b, c)

    def intersection(self, other):
        det = self.a*other.b - other.a*self.b
        if abs(det) < 1e-9:
            return None  # 平行或重合
        x = (self.b*other.c - other.b*self.c) / det
        y = (other.a*self.c - self.a*other.c) / det
        return Point(x, y)

    def foot_of_perpendicular(self, p):
        denom = self.a**2 + self.b**2
        x = (self.b*(self.b*p.x - self.a*p.y) - self.a*self.c) / denom
        y = (self.a*(-self.b*p.x + self.a*p.y) - self.b*self.c) / denom
        return Point(x, y)

class Circle:
    def __init__(self, center, r):
        self.center, self.r = center, float(r)

    def __repr__(self):
        return f"(x-{self.center.x:.2f})^2 + (y-{self.center.y:.2f})^2 = {self.r**2:.2f}"

    def intersect_line(self, line):
        # 特殊情況: line.b != 0 用公式，否則交換
        if abs(line.b) > 1e-9:
            m = -line.a / line.b
            k = -line.c / line.b
            A = 1 + m**2
            B = 2*(m*k - m*self.center.y - self.center.x)
            C = self.center.x**2 + self.center.y**2 + k**2 - 2*k*self.center.y - self.r**2
            disc = B**2 - 4*A*C
            if disc < -1e-9: return []
            elif abs(disc) < 1e-9: disc = 0
            sqrt_disc = math.sqrt(disc)
            xs = [(-B+sqrt_disc)/(2*A), (-B-sqrt_disc)/(2*A)]
            return [Point(x, m*x+k) for x in xs]
        else:
            x = -line.c / line.a
            dy = math.sqrt(max(self.r**2 - (x-self.center.x)**2, 0))
            return [Point(x, self.center.y+dy), Point(x, self.center.y-dy)]

    def intersect_circle(self, other):
        d = math.hypot(self.center.x - other.center.x, self.center.y - other.center.y)
        if d > self.r + other.r or d < abs(self.r - other.r):
            return []
        a = (self.r**2 - other.r**2 + d**2) / (2*d)
        h = math.sqrt(max(self.r**2 - a**2, 0))
        xm = self.center.x + a*(other.center.x - self.center.x)/d
        ym = self.center.y + a*(other.center.y - self.center.y)/d
        xs1 = xm + h*(other.center.y - self.center.y)/d
        ys1 = ym - h*(other.center.x - self.center.x)/d
        xs2 = xm - h*(other.center.y - self.center.y)/d
        ys2 = ym + h*(other.center.x - self.center.x)/d
        return [Point(xs1, ys1), Point(xs2, ys2)]

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1, self.p2, self.p3 = p1, p2, p3

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

    def side_lengths(self):
        def dist(a, b): return math.hypot(a.x-b.x, a.y-b.y)
        return (dist(self.p1, self.p2), dist(self.p2, self.p3), dist(self.p3, self.p1))

    def centroid(self):
        return Point((self.p1.x+self.p2.x+self.p3.x)/3,
                     (self.p1.y+self.p2.y+self.p3.y)/3)

    def translate(self, dx, dy):
        return Triangle(self.p1.translate(dx,dy), self.p2.translate(dx,dy), self.p3.translate(dx,dy))

    def scale(self, factor, center=None):
        return Triangle(self.p1.scale(factor,center), self.p2.scale(factor,center), self.p3.scale(factor,center))

    def rotate(self, angle, center=None):
        return Triangle(self.p1.rotate(angle,center), self.p2.rotate(angle,center), self.p3.rotate(angle,center))

# ==========================
# 測試與範例
# ==========================

# 兩直線相交
L1 = Line.from_points(Point(0,0), Point(1,1)) # y=x
L2 = Line.from_points(Point(0,1), Point(1,0)) # y=1-x
print("Line L1:", L1)
print("Line L2:", L2)
print("L1 ∩ L2 =", L1.intersection(L2))

# 直線與圓相交
C1 = Circle(Point(0,0), 1)
L3 = Line.from_points(Point(-2,0), Point(2,0)) # x軸
print("\nCircle:", C1)
print("Line L3:", L3)
print("C1 ∩ L3 =", C1.intersect_line(L3))

# 兩圓相交
C2 = Circle(Point(1,0), 1)
print("\nC1 ∩ C2 =", C1.intersect_circle(C2))

# 垂足
P = Point(1.2, 3.4)
foot = L3.foot_of_perpendicular(P)
print("\nFoot of perpendicular from", P, "to L3:", foot)
print("Distance =", math.hypot(P.x-foot.x, P.y-foot.y))

# 直角三角形驗證畢氏定理
A = Point(3,0)
B = P
C = foot
tri = Triangle(A,B,C)
a,b,c = tri.side_lengths()
print("\nRight Triangle Sides:", (a,b,c))
print("a^2 + b^2 =", a**2+b**2, "≈ c^2 =", c**2)

# 三角形物件變換
T = Triangle(Point(0,0), Point(2,0), Point(1,2))
print("\nOriginal Triangle:", T)
print("Side lengths:", T.side_lengths())
centroid = T.centroid()
T2 = T.translate(1,1)
T3 = T.scale(2, centroid)
T4 = T.rotate(math.pi/4, centroid)
print("Translated Triangle:", T2)
print("Scaled Triangle:", T3)
print("Rotated Triangle:", T4)

# ==========================
# 視覺化
# ==========================
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True)

# 繪製直線
xs = [-2,2]
ys = [(-L1.a*x - L1.c)/L1.b for x in xs]
ax.plot(xs, ys, 'r-', label="L1")
ys = [(-L2.a*x - L2.c)/L2.b for x in xs]
ax.plot(xs, ys, 'g-', label="L2")
ys = [(-L3.a*x - L3.c)/L3.b for x in xs]
ax.plot(xs, ys, 'b-', label="L3")

# 繪製圓
circle1 = plt.Circle((C1.center.x, C1.center.y), C1.r, fill=False, color='purple')
circle2 = plt.Circle((C2.center.x, C2.center.y), C2.r, fill=False, color='orange')
ax.add_artist(circle1)
ax.add_artist(circle2)

# 繪製點
ax.plot([P.x],[P.y],'ko',label="Point P")
ax.plot([foot.x],[foot.y],'mo',label="Foot")

# 繪製三角形
ax.plot([T.p1.x,T.p2.x,T.p3.x,T.p1.x],
        [T.p1.y,T.p2.y,T.p3.y,T.p1.y],'c-',label="Triangle")
ax.plot([T4.p1.x,T4.p2.x,T4.p3.x,T4.p1.x],
        [T4.p1.y,T4.p2.y,T4.p3.y,T4.p1.y],'y--',label="Rotated")

ax.legend()
plt.show()
