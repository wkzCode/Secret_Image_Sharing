import numpy as np

def share_image(img: np.ndarray, n: int, k: int, p: int = 257):
    h, w = img.shape
    shares = [np.zeros((h, w), dtype=np.uint8) for _ in range(n)]
    xs = list(range(1, n + 1))
    rng = np.random.default_rng()

    for i in range(h):
        for j in range(w):
            s = int(img[i, j])
            coeffs = [s] + rng.integers(0, p, size=k-1).tolist()
            for idx in range(n):
                x = xs[idx]
                fx = sum(coeffs[m] * pow(x, m, p) for m in range(k)) % p
                shares[idx][i, j] = fx if fx < 256 else 0
    return shares
