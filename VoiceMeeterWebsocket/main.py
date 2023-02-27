import voicemeeterlib


def main():
    with voicemeeterlib.api(vm_kind) as vm:
        vm.strip[1].mute = True


if __name__ == '__main__':
    vm_kind = "potato"
    main()
