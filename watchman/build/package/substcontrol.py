import sys

DEPENDENCIES_BY_UBUNTU = {
    "18.04": [],
    "20.04": [],
    "22.04": ["libgoogle-glog0v5", "libboost-context1.74.0", "libdouble-conversion3", "libevent-2.1-7", "libsnappy1v5"],
}

def main():
    filename, package_version, ubuntu_version = sys.argv[1:]
    
    with open(filename, 'r') as f:
        contents = f.read()

    contents = contents.replace('%VERSION%', package_version)
    contents = contents.replace('%DEPENDS%', ', '.join(DEPENDENCIES_BY_UBUNTU[ubuntu_version]))

    with open(filename, 'w') as f:
        f.write(contents)

if __name__ == "__main__":
    main()

