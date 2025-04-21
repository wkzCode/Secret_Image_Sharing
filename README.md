# Simple Secret Image Sharing and Reconstruction Using Lagrange Interpolate
## Sharing
```
python main.py --mode share --input images/1.png --n 5 --k 3 --output outputs
```
## Reconstruction
```
python main.py --mode reconstruct --shares outputs/share_1.png outputs/share_3.png outputs/share_5.png --xs 1 3 5 --k 3 --output outputs
```