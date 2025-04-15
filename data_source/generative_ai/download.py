import os
import wget
import re


script_dir = os.path.dirname(os.path.abspath(__file__))

file_links = [
    {
        "title": "Deform3DGS: Flexible Deformation for Fast Surgical Scene Reconstruction with Gaussian Splatting",
        "url": "https://arxiv.org/pdf/2405.17835"
    },
    {
        "title": "Endo-4DGS: Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting",
        "url": "https://arxiv.org/pdf/2401.16416"
    }
]


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)


def is_exist(file_link):
    filename = sanitize_filename(file_link["title"]) + ".pdf"
    file_path = os.path.join(script_dir, filename)
    return os.path.exists(file_path)


for file_link in file_links:
    filename = sanitize_filename(file_link["title"]) + ".pdf"
    file_path = os.path.join(script_dir, filename)
    if not is_exist(file_link):
        wget.download(file_link["url"], out=file_path)
