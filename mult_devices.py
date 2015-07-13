__author__ = 'bigzhang'

from adb import ADB

def get_devices(adb):
    devices = adb.get_devices()
    if devices[0] == 0:
        return devices[1]

def push_iozone(adb, device_name):
    local = 'iozone'
    remote = '/data'
    adb.set_target_device(device_name)
    adb.push_local_file(local, remote)
    adb.shell_command('chmod 777 /data/iozone')

def run_iozone(adb, devices_name):
    adb.set_target_device(devices_name)
    adb.shell_command('')

def do_work(adb, funcs, argv):
    for func in funcs:
        if func:
            func(adb, argv)

def main():
    # creates the ADB object
    adb = ADB()
    # IMPORTANT: You should supply the absolute path to ADB binary
    if adb.set_adb_path('/home/bigzhang/Android/Sdk/platform-tools/adb') is True:
        print "Version: %s" % adb.get_version()
    else:
        print "Check ADB binary path"

    devices_all = get_devices(adb)
    #print devices_all
    functions = []
    functions.append(push_iozone)
    functions.append(push_iozone)

    for devs in devices_all:
        do_work(adb, functions, devs)

if __name__ == "__main__":
    main()



