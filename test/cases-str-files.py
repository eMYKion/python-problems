lists = [
    ["run.exe", "README.md", "virus.exe"],
    ["class_slides.pdf", "id_ed25519.pub", "virus.exe"],
    [],
    ["virus.exe"],
    ["class_slides.pdf", "id_ed25519.pub", "virus.exe"],
    ["wierd.exe.pdf"]
]

cases = {
    i:((l,),list(filter(lambda s: not s.endswith(".exe"), l))) for i,l in enumerate(lists)
}
