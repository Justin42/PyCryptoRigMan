import yaml


class LWMonCLI(object):
    def __init__(self, config_file):
        print('Unified Lightweight Monitor - CLI')
        if config_file is None:
            print('No configuration file specified. You must add rigs manually.')
        else:
            print('Reading configuration from: ' + config_file)
            with open(config_file) as file:
                self.config = yaml.safe_load(file)

            print('Configuration loaded.')

        self._running_ = True
        return

    def _load_config_(self, config):
        print('Loading configuration data...')

    def print_menu(self):
        print('1. Add rig \n2. Show hashrates \n3. Show results \n4. Dump stats')

        if self.config['auto_update']:
            print('5. Disable auto update')
        else:
            print('5. Enable auto update')

        if self.config['alarm']:
            print('6. Disable alarm')
        else:
            print('5. Enable alarm')

    def parse(self, command):
        print(command)

    def run(self):
        while self._running_:
            continue


if __name__ == '__main__':
    cli = LWMonCLI('./config.yml')
    cli.run()
