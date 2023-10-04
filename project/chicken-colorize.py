import pygame
levels = [1,2,4,8]
inp = pygame.image.load('chicken-original.png')
outp = pygame.Surface((inp.get_width() * len(levels),inp.get_height()))

for idx, level in enumerate(levels):
    print(idx, level)
    img = inp.copy()
    for y in range(img.get_height()):
        for x in range(img.get_width()):
            src = img.get_at((x,y))
            r,g,b = src.r, src.g, src.b
            r >>= (8-level)
            g >>= (8-level)
            b >>= (8-level)
            r <<= (8-level)
            g <<= (8-level)
            b <<= (8-level)
            img.set_at((x,y), (r,g,b))
    outp.blit(img, (idx * img.get_width(), 0))

pygame.image.save(outp, "chicken-colorized.png")