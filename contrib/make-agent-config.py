#!/usr/bin/env python
# Icinga 2
# Copyright (C) 2012-2014 Icinga Development Team (http://www.icinga.org)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

import subprocess, json

inventory_json = subprocess.check_output(["icinga2-list-agents", "--batch"])
inventory = json.loads(inventory_json)

for agent, agent_info in inventory.items():
    print "object Endpoint \"%s\" {" % (agent)
    print "  host = \"%s\"" % (agent)
    print "}"
    print ""
    print "object Zone \"%s\" {" % (agent_info["zone"])
    print "  parent = \"%s\"" % (agent_info["parent_zone"])
    print "  endpoints = [ \"%s\" ]" % (agent)
    print "}"
    print ""
    print "zone \"%s\" {" % (agent_info["zone"])

    for host, services in agent_info["repository"].items():
        print "object Host \"%s\" {" % (host)
        print "  check_command = \"dummy\""
        print "}"
        print ""

        for service in services:
            print "object Service \"%s\" {" % (service)
            print "  check_command = \"dummy\""
            print "  host_name = \"%s\"" % (host)
            print "}"
            print ""

    print "}"

