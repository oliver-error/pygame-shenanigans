import pygame

valid_keys = {
    name: getattr(pygame, name)
    for name in dir(pygame)
    if name.startswith("K_")
}
print(valid_keys)