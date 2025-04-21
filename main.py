import argparse
import cv2
import os
from sharing.share import share_image
from sharing.reconstruct import reconstruct_image

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    parser = argparse.ArgumentParser(description="Lagrange Secret Image Sharing")
    parser.add_argument("--mode", choices=["share", "reconstruct"], required=True)
    parser.add_argument("--input", type=str, default="./images/1.png", help="Path to input grayscale image")
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--shares", nargs="+", help="List of share paths for reconstruction")
    parser.add_argument("--xs", nargs="+", type=int, help="X values used in reconstruction")
    parser.add_argument("--output", type=str, default="outputs")

    args = parser.parse_args()
    ensure_dir(args.output)

    if args.mode == "share":
        img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
        shares = share_image(img, args.n, args.k)
        for i, s in enumerate(shares):
            cv2.imwrite(os.path.join(args.output, f"share_{i+1}.png"), s)
        print(f"Saved {args.n} share images to '{args.output}'.")

    elif args.mode == "reconstruct":
        if len(args.shares) != args.k or len(args.xs) != args.k:
            raise ValueError("Need exactly k share files and k x-values.")
        share_imgs = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in args.shares]
        recon = reconstruct_image(share_imgs, args.xs, args.k)
        cv2.imwrite(os.path.join(args.output, "reconstructed.png"), recon)
        print("Reconstructed image saved.")

if __name__ == "__main__":
    main()
