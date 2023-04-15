# build the game with cs freeze
from cx_Freeze import setup, Executable


executables = [Executable(script = "main.py", target_name="PygameEasterJam")]
build_exe_options = {
    "build_exe": "PyGame_Easter_Jam",
    "packages" : ['pygame'],
    "include_files" : ["lib/"]
}

setup(
    name="pygame-easter-jam-particle-drawing",
    version="0.0",
    description="PyGame Easter 2023!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)