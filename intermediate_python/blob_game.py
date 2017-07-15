import pygame
from Blob import Blob
import math

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
STARTING_BLUE_BLOBS = 15
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()


def is_touching(b1,b2):
    distance = math.sqrt((b2.x - b1.x)**2 + (b2.y - b1.y)**2)
    print distance
    if distance < (b1.size + b2.size):
        return True
    else:
        return False


def handle_collisions(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens


def draw_environment(blob_list):
    game_display.fill(WHITE)
    blues, reds, greens = handle_collisions(blob_list)
    for dict_blob in blob_list:
        for blob_id in dict_blob:
            blob = dict_blob[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()
    pygame.display.update()
    return blues, reds, greens


class Blueblob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size

        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0

        elif other_blob.color == (0, 0, 255):
            # for now, nothing. Maybe later it does something more.
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')


class Redblob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)


class Greenblob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)



def main():
    red_blobs = dict(enumerate([Redblob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    blue_blobs = dict(enumerate([Blueblob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    green_blobs = dict(enumerate([Greenblob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs, red_blobs, green_blobs])
        clock.tick(60)

if __name__ == '__main__':
    main()




