import re
import sys

import pygame

ROBOT_SURFACE = None

class Robot(pygame.sprite.Sprite):
    def __init__(self, p, v, *groups):
        super().__init__(*groups)
        self._pos = pygame.math.Vector2(p)
        self._vel = pygame.math.Vector2(v)
    @property
    def image(self):
        return ROBOT_SURFACE
    @property
    def rect(self):
        return self.image.get_rect(topleft=tuple(self._pos))
    def update(self, w, h):
        self._pos += self._vel
        if self._pos[0] >= w:
            self._pos[0] = self._pos[0] - w
        elif self._pos[0] < 0:
            self._pos[0] = w + self._pos[0]
        if self._pos[1] >= h:
            self._pos[1] = self._pos[1] - h
        elif self._pos[1] < 0:
            self._pos[1] = h + self._pos[1]

def main(initial_pos, vel, height, width):
    global ROBOT_SURFACE
    pygame.init()
    display_flags = pygame.SCALED
    display = pygame.display.set_mode((width, height), display_flags)

    ROBOT_SURFACE = pygame.Surface((1, 1)).convert_alpha()
    ROBOT_SURFACE.fill((25, 150, 0, 50))

    robots = pygame.sprite.Group()
    for p, v in zip(initial_pos, vel):
        Robot(p, v, robots)

    try:
        clock = pygame.time.Clock()
        frame = 0
        paused = False
        while True:
            #clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
            if not paused:
                robots.update(width, height)
                display.fill((255, 255, 255))
                robots.draw(display)
                pygame.display.flip()
                frame += 1
                sf = safety_factor([r._pos for r in robots], width, height)
                if frame != 100:
                    print(frame, sf)
                else:
                    print(frame, sf, "Part 1 Answer")
                    paused = True
                if sf <= 60_000_000:
                    paused = True
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()

def count(p, xr, yr):
    c = 0
    for _p in p:
        if _p[0] >= xr[0] and _p[0] < xr[1] and _p[1] >= yr[0] and _p[1] < yr[1]:
            c += 1
    return c

def safety_factor(p, w, h):
    qh, qw = h//2, w//2
    q1 = count(p, (0, qw), (0, qh))
    q2 = count(p, (qw+1, w), (0, qh))
    q3 = count(p, (0, qw), (qh+1, h))
    q4 = count(p, (qw+1, w), (qh+1, h))
    return q1*q2*q3*q4

if __name__ == "__main__":
    filepath = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    p, v = [], []
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            p.append([int(m[1]), int(m[2])])
            v.append([int(m[3]), int(m[4])])
    main(p, v, height, width)

