#!/usr/bin/env python3
"""Fail the build if forbidden endpoints reappear in production sources or built APK."""
import pathlib,sys,zipfile
root=pathlib.Path(__file__).resolve().parent.parent
forbidden=(b"demtv.demiralayboncuk-092.workers.dev",b"api.openai.com",b"api.groq.com",b"generativelanguage.googleapis.com",b"openrouter.ai")
paths=[root/"fermata/src",root/"modules/web/src",root/"modules/tv/src",root/"modules/radio/src",root/"modules/podcast/src"]
fail=[]
for base in paths:
 if not base.exists(): continue
 for file in base.rglob("*"):
  if file.is_file() and file.suffix in (".java",".kt",".xml",".json",".html",".js"):
   data=file.read_bytes().lower()
   if any(host in data for host in forbidden):fail.append(str(file.relative_to(root)))
for arg in sys.argv[1:]:
 with zipfile.ZipFile(arg) as z:
  for name in z.namelist():
   if name.endswith((".dex",".xml",".json",".html",".js")):
    data=z.read(name).lower()
    if any(host in data for host in forbidden):fail.append(f"{arg}:{name}")
if fail:
 print("Forbidden external endpoints found:",*fail,sep="\n - ");sys.exit(1)
print("External AI and custom Cloudflare endpoints: not found in checked production sources/artifacts")
