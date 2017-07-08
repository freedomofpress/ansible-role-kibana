import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_listening_kibana_port(host):
    # Netstat is not installed on the docker image so socket module wont work
    kibana = "http://localhost:5601"
    assert host.check_output("curl -s -I {} | head -n 1 | cut -f 2 -d' '"
                             .format(kibana)) == "200"
