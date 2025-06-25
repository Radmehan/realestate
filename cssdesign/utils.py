import re

def extract_image_id(link):
    pattern = r'/d/(.*?)/view'
    match = re.search(pattern, link)
    if match:
        return match.group(1)
    else:
        return None

def construct_new_link(image_id):
    return f"https://drive.google.com/thumbnail?id={image_id}" 