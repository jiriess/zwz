"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        aHost = self.addHost( 'h1' )
        bHost = self.addHost( 'h2' )
        cHost = self.addHost( 'h3' )
        dHost = self.addHost( 'h4' )
        eHost = self.addHost( 'h5' )
        fHost = self.addHost( 'h6' )
        gHost = self.addHost( 'h7' )
        hHost = self.addHost( 'h8' )
        aSwitch = self.addSwitch( 's1' )
        bSwitch = self.addSwitch( 's2' )
        cSwitch = self.addSwitch( 's3' )
        dSwitch = self.addSwitch( 's4' )
        eSwitch = self.addSwitch( 's5' )
        fSwitch = self.addSwitch( 's6' )
        gSwitch = self.addSwitch( 's7' )

        # Add links
        self.addLink( aHost, dSwitch )
        self.addLink( dSwitch, bSwitch )
        self.addLink( dSwitch, bHost )
        self.addLink( bSwitch, eSwitch )
        self.addLink( eSwitch, cHost )
        self.addLink( eSwitch, dHost )
        self.addLink( fSwitch, eHost )
        self.addLink( fSwitch, fHost )
        self.addLink( fSwitch, cSwitch )
        self.addLink( gSwitch, gHost )
        self.addLink( gSwitch, hHost )
        self.addLink( gSwitch, cSwitch )
        self.addLink( bSwitch, aSwitch )
        self.addLink( cSwitch, aSwitch )




topos = { 'mytopo': ( lambda: MyTopo() ) }

