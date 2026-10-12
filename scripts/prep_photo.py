import io
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_image(input_path="source-photo.png", output_path="source-prepped.png"):
    print(f"[-] Processing new high-res photo {input_path}...")
    
    # 1. Load image and crop phone edge from right side
    pil_img = Image.open(input_path).convert("RGB")
    w, h = pil_img.size
    
    # Crop: keep left 88% to cut out the phone hand
    pil_img = pil_img.crop((0, 0, int(w * 0.88), h))
    
    # 2. Background removal
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    cutout_bytes = remove(buf.getvalue())
    cutout = Image.open(io.BytesIO(cutout_bytes)).convert("RGBA")
    
    # Trim transparent borders
    bbox = cutout.getbbox()
    if bbox:
        cutout = cutout.crop(bbox)
        
    np_img = np.array(cutout)
    alpha = np_img[:, :, 3] / 255.0
    rgb = np_img[:, :, :3]
    
    # 3. Grayscale and CLAHE local contrast
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    # 4. Composite onto solid white so outside space maps to spaces
    white_bg = np.ones_like(enhanced, dtype=np.uint8) * 255
    final = (enhanced * alpha + white_bg * (1.0 - alpha)).astype(np.uint8)
    
    cv2.imwrite(output_path, final)
    print(f"[+] Successfully prepared {output_path}")

if __name__ == "__main__":
    prep_image()
