__author__ = 'bigzhang'

from adb import ADB

def get_devices(adb):
    devices = adb.get_devices()
    return devices[1:]

def main():
    # creates the ADB object
    adb = ADB()
    # IMPORTANT: You should supply the absolute path to ADB binary
    if adb.set_adb_path('/home/bigzhang/Android/Sdk/platform-tools/adb') is True:
        print "Version: %s" % adb.get_version()
    else:
        print "Check ADB binary path"

    devices_all = get_devices(adb)
    print devices_all

if __name__ == "__main__":
    main()



