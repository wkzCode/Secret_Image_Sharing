import numpy as np
from .interpolate import lagrange_interpolate

def reconstruct_image(shares, xs, k, p: int = 257):
    h, w = shares[0].shape
    img_recon = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            y_s = [int(share[i, j]) for share in shares]
            s = lagrange_interpolate(0, xs, y_s, p)
            img_recon[i, j] = s if s < 256 else 0
    return img_recon
