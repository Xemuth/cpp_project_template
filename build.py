
import os
import subprocess
import argparse
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build options")
    parser.add_argument("-b", "--build",
                        help="Select build type", choices=["Release", "Debug"], required=False, action="store", default="Debug")
    parser.add_argument("-r", "--reconfigure",
                        help="Reconfigure cmake project", required=False, action="store_true", default=False)
    parser.add_argument("-g", "--generateur",
                        help="Select generator", choices=["Ninja", "MSVC"], required=False, action="store", default="Ninja")
    args = parser.parse_args()

    if not os.path.exists("CMakeLists.txt"):
        print("can't find MakeLists.txt")
        exit(-1)
    try:
        generate_cmd = ["cmake", "-B", "out"]
        if args.generateur == "Ninja":
            generate_cmd = generate_cmd + ["-G", "Ninja"]

        if args.build is not None:
            generate_cmd = generate_cmd + ["-DCMAKE_BUILD_TYPE=" + args.build]

        if os.path.exists("./out"):
            shutil.rmtree("./out")

        subprocess.check_call(generate_cmd)
        subprocess.check_call(["cmake", "--build", "./out"])

        exit(0)
    except Exception as e:
        print(str(e))
        exit(-1)
