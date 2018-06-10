from Banner import Banner

regels = """test"""

for tekst in regels.splitlines():
    tekst = tekst.strip().replace("\t", " ")
    banner = Banner("img\\1.jpg", tekst)
    banner.schrijf()
    banner.save(uit=("uit/" + tekst.replace(" ", "_") + ".png"))
