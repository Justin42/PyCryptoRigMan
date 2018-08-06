from unified_lwmon.api import RigMonitor, Rig
import yaml


class LWMonCLI(object):
    def __init__(self, config_file):
        print('Unified Lightweight Monitor - CLI')
        self.monitor = RigMonitor()
        if config_file is None:
            print('No configuration file specified. You must add rigs manually.')
        else:
            print('Reading configuration from: ' + config_file)
            with open(config_file) as file:
                self.config = yaml.safe_load(file)
                self._setup_rigs_()

            print('Configuration loaded.')

        self._running_ = True
        return

    def _setup_rigs_(self):
        rigs = self.config['lwmon']['rigs']
        for rig_conf in rigs:
            rig = Rig(rig_conf)
            self.monitor.add_rig(rig)

    def print_menu(self):
        print('1. Add rig \n2. Show hashrates \n3. Show results \n4. Dump stats')

        if self.config['lwmon']['cli']['auto-update']:
            print('5. Disable auto update')
        else:
            print('5. Enable auto update')

        if self.config['lwmon']['cli']['hashrate-alarm']:
            print('6. Disable alarm')
        else:
            print('5. Enable alarm')

    def print_hashrate(self, refresh=True):
        if refresh:
            self.monitor.refresh()
        hashrates = dict()
        for rig in self.monitor.rigs:
            # Combine hashrates for rigs with same name
            name = rig.config['name']
            if name not in hashrates.keys():
                hashrates[name] = 0
            hashrates[name] += rig.hashrate()
        for name in hashrates.keys():
            print("Rig '{0}': {1}H/s".format(name, hashrates[name]))
        print('Total: {0}H/s'.format(self.monitor.hashrate()))

    def parse(self, command: str):
        if command == '2':
            self.print_hashrate()

    def run(self):
        self.print_menu()
        while self._running_:
            opt = input('Selection: ')
            if opt is '':
                self.print_menu()
            else:
                self.parse(opt)
            continue


if __name__ == '__main__':
    cli = LWMonCLI('./config.yml')
    cli.run()
