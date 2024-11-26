user_input = input("File name: ").strip().lower()

if "." in user_input:
    inp = user_input.split(".")[-1]
else:
    inp = ""

mime_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

mime_type = mime_types.get(inp, "application/octet-stream")
print(mime_type)