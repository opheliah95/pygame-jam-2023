# build the game with cs freeze
from cx_Freeze import setup, Executable


executables = [Executable("main.py")]
build_exe_options = {
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