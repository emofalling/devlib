t1 = ["release", "debug"]
t1_verbose = [False, True]
t2 = ["default", "x86", "x64", "armv6", "armv7m", "armv7em", "armv7emsp", "armv7emdp", "xtensa", "xtensawin"]
import os
for i1, i1v in zip(t1, t1_verbose):
    print(f"Create directory: ./{i1}")
    try:
        os.mkdir(i1)
    except FileExistsError:
        print(f"Directory already exists: ./{i1}")
    for i2 in t2:
        print(f"Create directory: ./{i1}/{i2}")
        try:
            os.mkdir(f"{i1}/{i2}")
        except FileExistsError:
            print(f"Directory already exists: ./{i1}/{i2}")
        if i2 == "default":
            march_arg = ""
        else:
            march_arg = f"-march={i2}"
        command = f"mpy-cross-v5 -o ./{i1}/{i2}/devlib.mpy ../src/devlib.py {"-v" if i1v else ""} {march_arg}"
        print(f"Compile code: {command}")
        os.system(command)
        print("Compile done")
input("Press Enter or ctrl-c to exit...")