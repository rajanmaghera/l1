from importlib.metadata import version
import requests

print("The version is", version('requests'))

# pull script from GH

r = requests.get("https://raw.githubusercontent.com/rajanmaghera/l1/main/version.py")
print(r.text)
