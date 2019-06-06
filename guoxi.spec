from kivy.deps import sdl2, glew
coll = COLLECT(exe, Tree('C:\\Python27\\share\\kivy-examples\\demo\\touchtracer\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='touchtracer')