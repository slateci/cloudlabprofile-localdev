"""Spins up nodes for developing SLATE.

Instructions:
Wait for the profile instance to start. Then begin work.
"""

import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.emulab as emulab
import geni.rspec.igext as igext

# Define OS image
OS_IMAGE = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-BETA'

# Create a portal context, needed to define parameters
pc = portal.Context()

# Create a Request object to start building RSpec
request = pc.makeRequestRSpec()

# Create some user-configurable parameters
pc.defineParameter('public_ip_count', 'The number of additional public IPs to allocate', portal.ParameterType.INTEGER, 2)

params = pc.bindParameters()

# Validate parameters
if params.public_ip_count < 1:
    pc.reportError(portal.ParameterError('You must allocate at least 1 additional public ip.', ['public_ip_count']))
pc.verifyParameters()

# Create a node
node = request.RawPC('node1')

# Set node image
node.disk_image = OS_IMAGE

# Request a pool of dynamic publicly routable ip addresses - pool name cannot contain underscores - hidden bug
addressPool = igext.AddressPool('addressPool', int(params.public_ip_count))
request.addResource(addressPool)

# Output RSpec
pc.printRequestRSpec(request)

