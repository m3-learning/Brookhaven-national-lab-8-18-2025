from bs4 import BeautifulSoup
import base64
from pathlib import Path

svg_path = Path("/Users/joshuaagar/SSMC-CI-Madison-5-20-2025/slides/pld-dataflow/pld-dataflow.svg")
svg_content = svg_path.read_text()
soup = BeautifulSoup(svg_content, "xml")

for img in soup.find_all("image"):
    href = img.get("xlink:href") or img.get("href")
    if href and Path(href).exists():
        with open(href, "rb") as f:
            data = f.read()
            mime = "image/png" if href.endswith(".png") else "image/jpeg"
            encoded = base64.b64encode(data).decode("utf-8")
            data_uri = f"data:{mime};base64,{encoded}"
            img["xlink:href"] = data_uri
            if "href" in img.attrs:
                img["href"] = data_uri

svg_path.write_text(str(soup))
