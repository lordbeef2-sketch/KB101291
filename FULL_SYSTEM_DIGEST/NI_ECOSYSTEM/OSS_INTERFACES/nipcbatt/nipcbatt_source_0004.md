# NI OSS SOURCE SNAPSHOT: nipcbatt

<!--NI_OSS_SNAPSHOT repo=ni/nipcbatt commit=a26fcd38af55e0286aacff6cdc44bf53b2041111 -->

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/test_integration_static_digital_path_generation.py sha256=281651702ee79d267e7743a56922c7cceac33a3dbc9caf6660a40a57897454d0 bytes=30820 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/test_integration_static_digital_path_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/test_integration_static_digital_path_generation.py`
- sha256: `281651702ee79d267e7743a56922c7cceac33a3dbc9caf6660a40a57897454d0`
- bytes: 30820

````python
"""This module provide test of integration of StaticDigitalPathGeneration"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from niswitch import errors as niswitch_errors
from nipcbatt import switch


class TestIntegrationStaticDigitalPathGeneration(unittest.TestCase):
    """Definte a test fixture that chceck the integration of 
    'StaticDigitalPathGneration'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_niswitch_version = importlib.metadata.version("niswitch")
        logging.debug("%s = %s", nameof(used_niswitch_version), used_niswitch_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_static_digital_path_initialize_generate_close(self):
        
        """Checks happy path -- initialize/close are called without incident"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, com0 = "ch0", "com0"
        max_wait_debounce = 100

        # Connect
        connect = True 
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, com0)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(configuration)

        #Disconnect
        connect = False 
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)
        generation.close()

        return status.path_status
    
    def test_bank1_ch20_to_com1_connect_disconnect(self):
        """Bank 1 happy path: ch20 <-> com1 connect, then disconnect."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch20", "com1"
        max_wait_debounce = 100

        # Connect
        connect = True
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(configuration)

        # Disconnect
        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)

        generation.close()
        return status.path_status
    
    def test_reject_channel_to_channel(self):
        """Mux cannot short two inputs: ch0 <-> ch1 should result in PATH_UNSUPPORTED."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, ch1 = "ch0", "ch1"
        connect = True
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, ch1)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(configuration)
        
        self.assertEqual(status.path_status.name, 'PATH_UNSUPPORTED')

        generation.close()

    def test_reject_cross_bank_common_mismatch(self):
        """Channel must route to its bank common: ch3 <-> com1 should be unsupported."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, wrong_com = "ch3", "com1"
        connect = True
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, wrong_com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        status = generation.configure_and_generate(configuration)
        
        self.assertEqual(status.path_status.name, 'PATH_UNSUPPORTED')

        generation.close()

    def test_topology_change_requires_reset_then_succeeds(self):
        """
        If the device is on a different topology, reset_device=False should fail.
        Then reset_device=True should succeed. If already matching, skip the first part.
        """
        # Attempt without reset; if it succeeds, device is already on the requested topology.
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch0", "com0"
        connect = True
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        try:
            generation.initialize(resource_name, topology, reset_device=False, simulate=True)
            generation.configure_and_generate(configuration)
        except niswitch_errors.DriverError:
            # Expected when current topology differs.
            generation.close()
        else:
            # Already matching topology; skip the "requires reset" assertion.
            generation.close()
            self.skipTest("Device already on requested topology; reset not required in this environment.")

        # Now with reset=True it should succeed deterministically.
        generation = switch.StaticDigitalPathGeneration()
        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(configuration)

        # Disconnect to leave the session clean
        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)
        generation.close()
        return status.path_status

    def test_idempotent_connect_disconnect(self):
        """Calling connect/disconnect for the same pair repeatedly should be harmless."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch5", "com0"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        # Connect and disconnect twice
        connect = True
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)

        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)

        connect = True
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)

        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        status = generation.configure_and_generate(configuration)

        generation.close()
        return status.path_status
    
    
    def test_multiple_sequential_routes_single_session(self):
        """Connect/disconnect several valid pairs sequentially in one session."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        for ch, com in [("ch1", "com0"), ("ch10", "com0"), ("ch25", "com1")]:
            connect = True
            channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
            state = switch.StaticDigitalPathGenerationStateParameters(connect)
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
            timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
            configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
            status = generation.configure_and_generate(configuration)

            connect = False
            state = switch.StaticDigitalPathGenerationStateParameters(connect)
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
            configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
            status = generation.configure_and_generate(configuration)

        generation.close()
        return status.path_status
    

    def test_zero_debounce_is_accepted(self):
        """Zero debounce should be accepted (as 'no wait' or driver default)."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch8", "com0"
        connect = True
        max_wait_debounce = 0  # zero

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(configuration)

        # Disconnect
        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
        generation.close()

        return status.path_status
    
    def test_disconnect_without_prior_connect(self):
        """Disconnecting a non-existent path throw an error."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch2", "com0"
        connect = False
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        try:
            generation.configure_and_generate(configuration)
        except niswitch_errors.DriverError:
            # Expected when current topology differs.
            generation.close()

        return 
    
    def test_error_on_repeated_close(self):
        """Calling close twice without initialize should throw an error."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, com0 = "ch0", "com0"
        max_wait_debounce = 100

        # Connect
        connect = True 
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, com0)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        generation.configure_and_generate(configuration)

        generation.close()

        with self.assertRaises(niswitch_errors.DriverError):
            generation.close()

        return
    
    def test_sdpg_case1(self):
        """Executes the first test defined in the SDPG Cases Individual Test Plan"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        #ch2 to com0 connection
        channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("ch2", "com0")
        state1 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
        timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)
    
        path_status1 = generation.configure_and_generate(configuration1)

        #ch16 to com1 connection
        channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch16", "com1")
        state2 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
        timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)

        path_status2 = generation.configure_and_generate(configuration2)

        #ch2 to com0 connection
        channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch2", "com0")
        state3 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
        timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

        path_status3 = generation.configure_and_generate(configuration3)
        self.assertEqual(path_status3.path_status.name, 'PATH_EXISTS')

        generation.close()

    def test_sdpg_case2(self):
        """Executes the second test defined in the SDPG Cases Individual Test Plan"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        #ch2 to com0 connection
        channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
        state1 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
        timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)

        path_status1 = generation.configure_and_generate(configuration1)

        #ch16 to com1 connection
        channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch16", "com1")
        state2 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
        timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)
        
        path_status2 = generation.configure_and_generate(configuration2)

        #ch2 to com0 connection
        channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch2", "com0")
        state3 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
        timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)
        
        path_status3 = generation.configure_and_generate(configuration3)
        self.assertEqual(path_status3.path_status.name, 'RESOURCE_IN_USE')

        generation.close()

    
    def test_sdpg_case3(self):
        """Executes the third test defined in the SDPG Cases Individual Test Plan"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        #ch2 to com0 connection
        channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
        state1 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
        timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)
        
        path_status1 = generation.configure_and_generate(configuration1)

        #ch16 to com1 connection
        channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "ch2")
        state2 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
        timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)
        
        path_status2 = generation.configure_and_generate(configuration2)
        self.assertEqual(path_status2.path_status.name, 'PATH_UNSUPPORTED')

        #ch2 to com0 connection
        channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch0", "com0")
        state3 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
        timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

        path_status3 = generation.configure_and_generate(configuration3)
        self.assertEqual(path_status3.path_status.name, 'RESOURCE_IN_USE')

        generation.close()


    def test_sdpg_case4(self):
        """Executes the fourth test defined in the SDPG Cases Individual Test Plan"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        #ch2 to com0 connection
        channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
        state1 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
        timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)
        
        path_status1 = generation.configure_and_generate(configuration1)

        #ch16 to com1 connection
        channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
        state2 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
        timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)

        path_status2 = generation.configure_and_generate(configuration2)
        self.assertEqual(path_status2.path_status.name, 'PATH_EXISTS')

        #ch2 to com0 connection
        channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch0", "com0")
        state3 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
        timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

        path_status3 = generation.configure_and_generate(configuration3)
        self.assertEqual(path_status3.path_status.name, 'RESOURCE_IN_USE')

        generation.close()


    
    def test_sdpg_case5(self):
        """Executes the fifth test defined in the SDPG Cases Individual Test Plan"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        #ch2 to com0 connection
        channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("com0", "ch1")
        state1 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
        timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)

        path_status1 = generation.configure_and_generate(configuration1)

        #ch16 to com1 connection
        channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com1")
        state2 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
        timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)

        path_status2 = generation.configure_and_generate(configuration2)
        self.assertEqual(path_status2.path_status.name, 'PATH_UNSUPPORTED')

        #ch2 to com0 connection
        channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
        state3 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
        timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

        path_status3 = generation.configure_and_generate(configuration3)
        self.assertEqual(path_status3.path_status.name, 'PATH_EXISTS')

        generation.close()


    def test_sdpg_case6(self):
        """Executes the sixth test defined in the SDPG Cases Individual Test Plan"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        #ch2 to com0 connection
        channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("com0", "ch16")
        state1 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
        timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        
        path_status1 = generation.configure_and_generate(configuration1)

        self.assertEqual(path_status1.path_status.name, 'PATH_UNSUPPORTED')

        #ch16 to com1 connection
        channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch16", "com1")
        state2 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
        timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        path_status2 = generation.configure_and_generate(configuration2)

        #ch2 to com0 connection
        channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch16", "com3")
        state3 = switch.StaticDigitalPathGenerationStateParameters(True)
        ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
        timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        #path_status3 = generation.configure_and_generate(configuration3)

        with self.assertRaises(niswitch_errors.DriverError) as error:
            #unknown channel or repeated capability name
            path_status3 = generation.configure_and_generate(configuration3)

        self.assertEqual(error.exception.code, -1074135008)

        generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/__init__.py sha256=db9d1551553d0f87fb736fbb578a73c58acd209eb1091d9070fa0ab7f7ec134e bytes=480 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/__init__.py`
- sha256: `db9d1551553d0f87fb736fbb578a73c58acd209eb1091d9070fa0ab7f7ec134e`
- bytes: 480

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.static_digital_state_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/test_integration_static_digital_state_generation.py sha256=e626b69091e74820bf725e630b3b5546db6f2681e2e986f92f1338a57f66d006 bytes=7879 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/test_integration_static_digital_state_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/test_integration_static_digital_state_generation.py`
- sha256: `e626b69091e74820bf725e630b3b5546db6f2681e2e986f92f1338a57f66d006`
- bytes: 7879

````python
"""This module provides test of integration of StaticDigitalStateGeneration."""

import importlib
import logging
import random
import sys
import unittest

from nidaqmx.errors import DaqError
from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationStaticDigitalStateGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'StaticDigitalStateGeneration' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx_if_not_installed(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_num_channels_8(self):
        """Integration test ensuring the module creates the correct output
        when given 8 channels of data to write
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # create configuration object
        num_channels = 8
        test_data_to_write = [random.choice([True, False]) for item in range(num_channels)]
        cfg = daq.StaticDigitalStateGenerationConfiguration(data_to_write=test_data_to_write)

        with daq.StaticDigitalStateGeneration() as gen:
            test_channel_expression = (
                "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:7"
            )

            gen.initialize(channel_expression=test_channel_expression)
            generated_data = gen.configure_and_generate(cfg)

            expected_generated_data = []
            for i in range(len(generated_data.channel_identifiers)):
                n = test_channel_expression.find("line") + len("line")
                expected_generated_data.append(test_channel_expression[0:n] + str(i))

        self.assertTrue(generated_data.channel_identifiers == expected_generated_data)

    def test_integration_num_channels_23(self):
        """Integration test ensuring the module creates the correct output
        when given 23 channels of data to write
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # create configuration object
        num_channels = 23
        test_data_to_write = [random.choice([True, False]) for item in range(num_channels)]
        cfg = daq.StaticDigitalStateGenerationConfiguration(data_to_write=test_data_to_write)

        with daq.StaticDigitalStateGeneration() as gen:
            test_channel_expression = (
                "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:22"
            )

            gen.initialize(channel_expression=test_channel_expression)
            generated_data = gen.configure_and_generate(cfg)

            expected_generated_data = []
            for i in range(len(generated_data.channel_identifiers)):
                n = test_channel_expression.find("line") + len("line")
                expected_generated_data.append(test_channel_expression[0:n] + str(i))

        self.assertTrue(generated_data.channel_identifiers == expected_generated_data)

    def test_integration_channel_expression_is_empty(self):
        """Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression="")

            gen.close()

    def test_integration_channel_expression_is_none(self):
        """Integration test ensuring that is channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=None)

            gen.close()

    def test_integration_channel_expression_port(self):
        """Integration test ensuring that the channel expression
        value consisting of only 'port' with channel
        designated will throw an error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(DaqError) as ctx:
                gen.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0"
                )

            print(ctx.exception)

            gen.close()

    def test_integration_channel_expression_only_instrument(self):
        """Integration test that channel expression value of only 'port'
        without channels designated throws an error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(DaqError):
                gen.initialize(channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4")
            gen.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/__init__.py sha256=caa834dd38270e67ba2c52a457d7a345824b440a72cfbab59177e2ce6f2072b9 bytes=481 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/__init__.py`
- sha256: `caa834dd38270e67ba2c52a457d7a345824b440a72cfbab59177e2ce6f2072b9`
- bytes: 481

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.static_digital_state_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/test_integration_static_digital_state_measurement.py sha256=b21663fe54d38025686ad0a378e7c7bcdc9845e27c9b97745793f5a6d3d4ac8d bytes=7233 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/test_integration_static_digital_state_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/test_integration_static_digital_state_measurement.py`
- sha256: `b21663fe54d38025686ad0a378e7c7bcdc9845e27c9b97745793f5a6d3d4ac8d`
- bytes: 7233

````python
"""This module provides test of integration of StaticDigitalStateMeasurement."""

import importlib
import logging
import sys
import unittest

from nidaqmx.errors import DaqError
from varname import nameof


from nipcbatt import daq


class TestIntegrationStaticDigitalStateMeasurement(unittest.TestCase):
    """Defines a test fixture that check the integration of the
       'StaticDigitalStateMeasurement' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_num_channels_and_num_data_len_9(self):
        """Integration test ensuring that the module creates
        the correct output object in terms of numbers of
        channels and the associated data, both of length 8
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateMeasurement() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:8"
            )
            result_data = measurement.configure_and_measure()

            print("result_data.channel_identifiers: ", result_data.channel_identifiers)
            print("result_data.digital_states: ", result_data.digital_states)

            self.assertEqual(len(result_data.digital_states), 9)
            self.assertEqual(len(result_data.channel_identifiers), len(result_data.digital_states))

            measurement.close()

    def test_integration_num_channels_and_num_data_len_5(self):
        """Integration test ensuring that the module creates
        the correct output object in terms of numbers of
        channels and the associated data, both of length 5
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateMeasurement() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line1:5"
            )
            result_data = measurement.configure_and_measure()

            print("result_data.channel_identifiers: ", result_data.channel_identifiers)
            print("result_data.digital_states: ", result_data.digital_states)

            self.assertEqual(len(result_data.digital_states), 5)
            self.assertEqual(len(result_data.channel_identifiers), len(result_data.digital_states))

            measurement.close()

    def test_integration_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression is None
        then initialize() properly catches this error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(channel_expression=None)

            measurement.close()

    def test_integration_channel_expression_is_empty(self):
        """Integration test ensuring that if channel expression is empty
        then initialize() properly catches this error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(channel_expression="")

            measurement.close()

    def test_integration_channel_expression_port(self):
        """Integration test ensuring that channel expression value
        of only 'port' without channels designated throws the proper error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0"
                )
            measurement.close()

    def test_integration_channel_expression_only_instrument(self):
        """Integration test ensuring that channel expression value
        of only 'port' without channels designated throws the proper error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4"
                )

            measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/__init__.py sha256=66bf0c67e16a37136f5a1015ac35bd267b36e8db79b7539b3383b87f9784ed89 bytes=472 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/__init__.py`
- sha256: `66bf0c67e16a37136f5a1015ac35bd267b36e8db79b7539b3383b87f9784ed89`
- bytes: 472

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.temperature_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_rtd.py sha256=5af1c9ee8740e0d35f185fcb540be946f22db0ad2daff1f629d756f7ed083422 bytes=11443 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_rtd.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_rtd.py`
- sha256: `5af1c9ee8740e0d35f185fcb540be946f22db0ad2daff1f629d756f7ed083422`
- bytes: 11443

````python
"""This module provides test of integration of TemperatureMeasurementUsingRtd."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq


'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationTemperatureMeasurementUsingRtd(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingRtd` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_temperature_measurement_using_rtd_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with daq.TemperatureMeasurementUsingRtd() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = daq.TemperatureRtdMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_temperature_measurement_using_rtd_configure_and_measure(self):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with daq.TemperatureMeasurementUsingRtd() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            print(f"parameters = {daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION}")
            results = measurement.configure_and_measure(
                configuration=daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, daq.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_rtd_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.TemperatureMeasurementUsingRtd() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = daq.TemperatureRtdMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.TemperatureRtdMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                sample_clock_timing_parameters=(
                    daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_rtd_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0,"
            + " NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with daq.TemperatureMeasurementUsingRtd() as measurement:
                measurement.initialize(channel_expression=channel_expression)

                configuration = daq.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")
                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
                )
                self.assertIs(None, results)

                configuration = daq.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
                )
                self.assertIsInstance(results, daq.TemperatureMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermistor.py sha256=bc350dc3b04ad2d009c0256885433d2e75c36c21e63146b490c6a421be54eb4f bytes=19895 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermistor.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermistor.py`
- sha256: `bc350dc3b04ad2d009c0256885433d2e75c36c21e63146b490c6a421be54eb4f`
- bytes: 19895

````python
"""This module provides test of integration of TemperatureMeasurementUsingThermistor."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)

TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_BETA_COEFFICIENT = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    temperature_minimum_value_celsius_degrees=0.0,
    temperature_maximum_value_celsius_degrees=100.0,
    voltage_excitation_value_volts=6.0,
    thermistor_resistor_ohms=9980,
    steinhart_hart_equation_option=(
        nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE
    ),
    coefficients_steinhart_hart_parameters=nipcbatt.DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS,
    beta_coefficient_and_sensor_resistance_parameters=(
        nipcbatt.BetaCoefficientAndSensorResistanceParameters(
            coefficient_steinhart_hart_beta_kelvins=3720.0,
            sensor_resistance_ohms=10000.0,
        )
    ),
)

TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_COEFFICIENTS = (
    nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        temperature_minimum_value_celsius_degrees=0.0,
        temperature_maximum_value_celsius_degrees=100.0,
        voltage_excitation_value_volts=6.0,
        thermistor_resistor_ohms=9980,
        steinhart_hart_equation_option=(
            nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
        ),
        coefficients_steinhart_hart_parameters=nipcbatt.CoefficientsSteinhartHartParameters(
            coefficient_steinhart_hart_a=0.001295361,
            coefficient_steinhart_hart_b=0.0002343159,
            coefficient_steinhart_hart_c=1.018703e-7,
        ),
        beta_coefficient_and_sensor_resistance_parameters=(
            nipcbatt.DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS
        ),
    )
)


class TestIntegrationTemperatureMeasurementUsingRtd(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingRtd` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_temperature_measurement_using_thermistor_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermistor() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_temperature_measurement_using_thermistor_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermistor() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            print(
                f"parameters = {nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION}"
            )
            results = measurement.configure_and_measure(
                configuration=nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermistor() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only_with_beta_coefficient(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermistor() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_BETA_COEFFICIENT
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_BETA_COEFFICIENT
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only_with_coefficients(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermistor() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_COEFFICIENTS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=(
                    TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_COEFFICIENTS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0,"
            + " NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with nipcbatt.TemperatureMeasurementUsingThermistor() as measurement:
                measurement.initialize(channel_expression=channel_expression)

                configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")
                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
                )
                self.assertIs(None, results)

                configuration = nipcbatt.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
                )
                self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermocouple.py sha256=2ad550839664d7b529bee25c4d54585ddf7ac396f59b8d6f03e69b8805fc76fb bytes=22068 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermocouple.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermocouple.py`
- sha256: `2ad550839664d7b529bee25c4d54585ddf7ac396f59b8d6f03e69b8805fc76fb`
- bytes: 22068

````python
"""This module provides test of integration of TemperatureMeasurementUsingThermocouple."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.errors
from varname import nameof

import nipcbatt


class TestIntegrationTemperatureMeasurementUsingThermocouple(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingThermocouple` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_temperature_measurement_using_thermocouple_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(nidaqmx.errors.DaqError):
                measurement.initialize(
                    channel_expression="",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(AttributeError):
                measurement.initialize(
                    channel_expression=None,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_source_is_none(
        self,
    ):
        """Integration test ensuring that if cjc source
        is None then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(AttributeError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=None,
                    cold_junction_compensation_channel="",
                )

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_channel_is_none(
        self,
    ):
        """Integration test ensuring that if cjc_channel is null when cjc_source is set to SCANNABLE_CHANNEL,
        then initialize() catches the error
        """  # noqa: W505, D202, D205, D415 - doc line too long (109 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")

            with self.assertRaises(nidaqmx.errors.DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL,
                    cold_junction_compensation_channel=None,
                )
                results = measurement.configure_and_measure(configuration=configuration)
                print(f"results = {results}")

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_channel_is_empty(
        self,
    ):
        """Integration test ensuring that if cjc_channel is empty when cjc_source is set to SCANNABLE_CHANNEL,
        then configure_and_measure() catches the error
        """  # noqa: W505, D202, D205, D415 - doc line too long (110 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")

            with self.assertRaises(nidaqmx.errors.DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL,
                    cold_junction_compensation_channel="",
                )
                results = measurement.configure_and_measure(configuration=configuration)
                print(f"results = {results}")

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_value_is_none(
        self,
    ):
        """Integration test ensuring that if cjc_value is None when cjc_source is set to CONSTANT_USER_VALUE,
        then configure_and_measure() catches the error
        """  # noqa: W505, D202, D205, D415 - doc line too long (109 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(ValueError):
                channel_parameters = nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=0.0,
                    temperature_maximum_value_celsius_degrees=100.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=None,  # cjc_value is None
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )

                configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=channel_parameters,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")

                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )
                results = measurement.configure_and_measure(configuration=configuration)
                print(f"results = {results}")

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_configure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                cold_junction_compensation_channel="",
            )

            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_temperature_measurement_using_thermocouple_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                cold_junction_compensation_channel="",
            )

            print(
                f"parameters = {nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION}"
            )
            results = measurement.configure_and_measure(
                configuration=nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_thermocouple_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                cold_junction_compensation_channel="",
            )

            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_thermocouple_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0,"
            + " NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
                measurement.initialize(
                    channel_expression=channel_expression,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )

                configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")
                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
                )
                self.assertIs(None, results)

                configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
                )
                self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/__init__.py sha256=f33952766bfed33625df356be18fe85dc03ff6c192634d3a3a2afa81ab5c5bf0 bytes=472 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/__init__.py`
- sha256: `f33952766bfed33625df356be18fe85dc03ff6c192634d3a3a2afa81ab5c5bf0`
- bytes: 472

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.time_domain_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/test_integration_time_domain_measurement.py sha256=c6654fc34c7a7b5ddd529b18dee49080223c44f214f1af977de682ebfffb29af bytes=12627 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/test_integration_time_domain_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/test_integration_time_domain_measurement.py`
- sha256: `c6654fc34c7a7b5ddd529b18dee49080223c44f214f1af977de682ebfffb29af`
- bytes: 12627

````python
"""This module provides test of integration of TimeDomainMeasurement."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationTimeDomainMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `TimeDomainMeasurement` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_time_domain_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with daq.TimeDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.TimeDomainMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_time_domain_measurement_configure_and_measure(self):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with daq.TimeDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            print(f"parameters = {daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION}")
            results = measurement.configure_and_measure(
                configuration=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, daq.TimeDomainMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.TimeDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.TimeDomainMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.TimeDomainMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.TimeDomainMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0, NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with daq.TimeDomainMeasurement() as measurement:
                measurement.initialize(analog_input_channel_expression=channel_expression)

                configuration = daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.MeasurementOptions(
                        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                        measurement_analysis_requirement=(
                            nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                        ),
                    ),
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")
                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
                )
                self.assertIs(None, results)

                configuration = daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.MeasurementOptions(
                        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                        measurement_analysis_requirement=(
                            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                        ),
                    ),
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
                )
                self.assertIsInstance(results, daq.TimeDomainMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/__init__.py sha256=09ffcf3f30f516c0b91e84aff140fae8efeb36d25ad97f4f8cffafd04227e759 bytes=253 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/__init__.py`
- sha256: `09ffcf3f30f516c0b91e84aff140fae8efeb36d25ad97f4f8cffafd04227e759`
- bytes: 253

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/__init__.py sha256=7908b92373742834bde8e3eb1ebbddd51e51cb8db073f985dc17d170079534cf bytes=260 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/common/__init__.py`
- sha256: `7908b92373742834bde8e3eb1ebbddd51e51cb8db073f985dc17d170079534cf`
- bytes: 260

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.common package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_common_data_types.py sha256=10ecd3cfab56245e351ffd14a3eab72d50b32dc50257923274309288e24ab3db bytes=36804 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_common_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/common/test_common_data_types.py`
- sha256: `10ecd3cfab56245e351ffd14a3eab72d50b32dc50257923274309288e24ab3db`
- bytes: 36804

````python
"""This module provides common data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class TestMeasurementOptions(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementOptions` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_measurement_options(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementOptions."""
        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        instance = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        actual_execution_option = instance.execution_option
        actual_measurement_analysis_requirement = instance.measurement_analysis_requirement
        self.assertEqual(expected_execution_option, actual_execution_option)
        self.assertEqual(
            expected_measurement_analysis_requirement,
            actual_measurement_analysis_requirement,
        )


class TestSampleClockTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SampleClockTimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source=None,
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source="",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source=" ",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters_init_fails_when_sampling_rate_hertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        expected_sample_clock_source = "OnboardClock"
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source=expected_sample_clock_source,
                    sampling_rate_hertz=-6,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The value sampling_rate_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        instance = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        actual_sample_clock_source = instance.sample_clock_source
        actual_sampling_rate_hertz = instance.sampling_rate_hertz
        actual_number_of_samples_per_channel = instance.number_of_samples_per_channel
        actual_sample_timing_engine = instance.sample_timing_engine
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_number_of_samples_per_channel, actual_number_of_samples_per_channel
        )
        self.assertEqual(
            expected_sample_timing_engine,
            actual_sample_timing_engine,
        )


class TestDigitalStartTriggerParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DigitalStartTriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_start_trigger_parameters_init_should_not_fail_if_trigger_select_is_no_trigger(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_trigger_select = nipcbatt.StartTriggerType.NO_TRIGGER
        expected_digital_start_trigger_source = ""
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        instance = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        actual_trigger_select = instance.trigger_select
        actual_digital_start_trigger_source = instance.digital_start_trigger_source
        actual_digital_start_trigger_edge = instance.digital_start_trigger_edge
        self.assertEqual(expected_trigger_select, actual_trigger_select)
        self.assertEqual(expected_digital_start_trigger_source, actual_digital_start_trigger_source)
        self.assertEqual(expected_digital_start_trigger_edge, actual_digital_start_trigger_edge)

    def test_digital_start_trigger_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        instance = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        actual_trigger_select = instance.trigger_select
        actual_digital_start_trigger_source = instance.digital_start_trigger_source
        actual_digital_start_trigger_edge = instance.digital_start_trigger_edge
        self.assertEqual(expected_trigger_select, actual_trigger_select)
        self.assertEqual(expected_digital_start_trigger_source, actual_digital_start_trigger_source)
        self.assertEqual(expected_digital_start_trigger_edge, actual_digital_start_trigger_edge)


class TestMeasurementData(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_measurement_data_init_fails_when_samples_is_none(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MeasurementData(
                    data_samples=None,
                )
            )

        self.assertEqual(
            "The object data_samples is None.",
            str(ctx.exception),
        )

    def test_measurement_data_init_fails_when_samples_is_empty(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MeasurementData(
                    data_samples=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable data_samples of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_measurement_data_fails_if_the_array_has_more_than_two_dimensions(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        data_samples = numpy.zeros(shape=(10, 10, 10))
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MeasurementData(
                    data_samples=data_samples,
                )
            )

        self.assertEqual(
            "The size of shape must less than or equal to 2.",
            str(ctx.exception),
        )

    def test_measurement_data(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        instance = nipcbatt.MeasurementData(
            data_samples=expected_samples_numpy_array,
        )

        for sample_array in instance.samples_per_channel:
            actual_array_count = len(sample_array)

            self.assertEqual(expected_array_count, actual_array_count)
            for index in range(0, expected_array_count):
                self.assertAlmostEqual(
                    first=expected_samples_numpy_array[index],
                    second=sample_array[index],
                    delta=0.0001,
                )


class TestAnalogWaveform(unittest.TestCase):
    """Defines a test fixture that checks
    `AnalogWaveform` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_analog_waveform_init_fails_when_channel_name_is_none(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_delta_time_seconds = invert_value(10000)
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=None,
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_channel_name_is_empty(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_delta_time_seconds = invert_value(10000)
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name="",
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_channel_name_is_whitespace(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_delta_time_seconds = invert_value(10000)
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=" ",
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_delta_time_seconds_is_less_than_or_equal_to_zero(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=expected_channel_name,
                    delta_time_seconds=-0.0001,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The value delta_time_seconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_samples_is_none(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_delta_time_seconds = invert_value(10000)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=expected_channel_name,
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=None,
                )
            )

        self.assertEqual(
            "The object samples is None.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_samples_is_empty(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_delta_time_seconds = invert_value(10000)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=expected_channel_name,
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable samples of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_analog_waveform(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_delta_time_seconds = 1.0 / 10000
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        instance = nipcbatt.AnalogWaveform(
            channel_name=expected_channel_name,
            delta_time_seconds=expected_delta_time_seconds,
            samples=expected_samples_numpy_array,
        )

        actual_channel_name = instance.channel_name
        actual_delta_time_seconds = instance.delta_time_seconds
        actual_samples_numpy_array = instance.samples
        actual_array_count = actual_samples_numpy_array.size

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(expected_delta_time_seconds, actual_delta_time_seconds)
        self.assertEqual(expected_array_count, actual_array_count)
        for index in range(0, expected_array_count):
            self.assertAlmostEqual(
                first=expected_samples_numpy_array[index],
                second=actual_samples_numpy_array[index],
                delta=0.0001,
            )


class TestAmplitudeSpectrum(unittest.TestCase):
    """Defines a test fixture that checks
    `AmplitudeSpectrum` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_amplitude_spectrum_init_fails_when_channel_name_is_none(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=None,
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_channel_name_is_empty(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name="",
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_channel_name_is_whitespace(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=" ",
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_spectrum_frequency_resolution_hertz_is_less_than_or_equal_to_zero(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=expected_channel_name,
                    spectrum_start_frequency_hertz=(expected_spectrum_start_frequency_hertz),
                    spectrum_frequency_resolution_hertz=-1.0,
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The value spectrum_frequency_resolution_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_amplitudes_is_none(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=expected_channel_name,
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=None,
                )
            )

        self.assertEqual(
            "The object amplitudes is None.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_amplitudes_is_empty(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=expected_channel_name,
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable amplitudes of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        instance = nipcbatt.AmplitudeSpectrum(
            channel_name=expected_channel_name,
            spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
            spectrum_frequency_resolution_hertz=(expected_spectrum_frequency_resolution_hertz),
            amplitudes=expected_samples_numpy_array,
        )

        actual_channel_name = instance.channel_name
        actual_spectrum_start_frequency_hertz = instance.spectrum_start_frequency_hertz
        actual_spectrum_frequency_resolution_hertz = instance.spectrum_frequency_resolution_hertz
        actual_samples_numpy_array = instance.amplitudes
        actual_array_count = actual_samples_numpy_array.size

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(
            expected_spectrum_start_frequency_hertz,
            actual_spectrum_start_frequency_hertz,
        )
        self.assertEqual(
            expected_spectrum_frequency_resolution_hertz,
            actual_spectrum_frequency_resolution_hertz,
        )
        self.assertEqual(expected_array_count, actual_array_count)

        for index in range(0, expected_array_count):
            self.assertAlmostEqual(
                first=expected_samples_numpy_array[index],
                second=actual_samples_numpy_array[index],
                delta=0.0001,
            )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_data_types.py sha256=2e75691a90dac43a35e01ff5339c5b9066e0858760195fcb1dcabe111ed30d81 bytes=2700 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_data_types.py`
- sha256: `2e75691a90dac43a35e01ff5339c5b9066e0858760195fcb1dcabe111ed30d81`
- bytes: 2700

````python
"""This module provides communication data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt


class TestMemoryAddressParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `MemoryAddressParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_memory_address_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.communication_data_types.MemoryAddressParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_memory_address = 7
        expected_address_type = nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE
        expected_address_endianness = nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN

        instance = nipcbatt.communications.MemoryAddressParameters(
            memory_address=expected_memory_address,
            address_type=expected_address_type,
            address_endianness=expected_address_endianness,
        )

        actual_memory_address = instance.memory_address
        actual_address_type = instance.address_type
        actual_address_endianness = instance.address_endianness

        self.assertEqual(expected_memory_address, actual_memory_address)
        self.assertEqual(
            expected_address_type,
            actual_address_type,
        )
        self.assertEqual(expected_address_endianness, actual_address_endianness)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_functions.py sha256=f6670634ae42b321bd6682eb7f32e78ceb6568da388d6af5166b95b127b39d90 bytes=11184 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_functions.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_functions.py`
- sha256: `f6670634ae42b321bd6682eb7f32e78ceb6568da388d6af5166b95b127b39d90`
- bytes: 11184

````python
"""This module provides communication functions check."""

import importlib.metadata
import logging
import sys
import unittest
from typing import List

from parameterized import parameterized
from varname import nameof

import nipcbatt
from nipcbatt import communications
from nipcbatt.pcbatt_library.communications.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_spi_read_communication,
    create_command_for_spi_write_communication,
)


class TestComputePagesCharacteristics(unittest.TestCase):
    """Defines a test fixture that checks
    function `compute_pages_characteristics` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "one page",
                0,
                48,
                128,
                [
                    communications.MemoryPageCharacteristics(0, 48, 0),
                ],
            ),
            (
                "three pages starting at 12",
                12,
                340,
                128,
                [
                    communications.MemoryPageCharacteristics(0, 116, 12),
                    communications.MemoryPageCharacteristics(116, 128, 128),
                    communications.MemoryPageCharacteristics(244, 96, 256),
                ],
            ),
            (
                "three pages starting at 56",
                56,
                159,
                96,
                [
                    communications.MemoryPageCharacteristics(0, 40, 56),
                    communications.MemoryPageCharacteristics(40, 96, 96),
                    communications.MemoryPageCharacteristics(136, 23, 192),
                ],
            ),
        ]
    )
    def test_compute_pages_characteristics(
        self,
        test_case_name: str,
        memory_start_address: int,
        number_of_bytes_to_write: int,
        number_of_bytes_per_page: int,
        expected_pages_characteristics: List[communications.MemoryPageCharacteristics],
    ):
        """unit test of compute_pages_characteristics."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (155 > 100 characters) (auto-generated noqa)
        logging.debug("running %s.", test_case_name)

        actual_pages_characteristics = compute_pages_characteristics(
            data_memory_start_address=memory_start_address,
            number_of_bytes_to_write=number_of_bytes_to_write,
            number_of_bytes_per_page=number_of_bytes_per_page,
        )
        self.assertListEqual(expected_pages_characteristics, actual_pages_characteristics)


class TestCreateArrayForSpiReadInstruction(unittest.TestCase):
    """Defines a test fixture that checks
    function `create_array_for_spi_read_instruction` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "one byte little endian 5 data bytes",
                12,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                [0x3, 12, 0, 0, 0, 0, 0],
            ),
            (
                "one byte little endian with 4th bit set 5 data bytes",
                268,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                # 0x3 | 0x8 => 11
                [11, 12, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes little endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                7,
                [0x3, 15, 12, 0, 0, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes big endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                7,
                [0x3, 12, 15, 0, 0, 0, 0, 0, 0, 0],
            ),
        ]
    )
    def test_create_array_for_spi_read_instruction(
        self,
        test_case_name: str,
        memory_address: int,
        address_type: nipcbatt.DataMemoryAddressType,
        address_endianness: nipcbatt.DataMemoryAddressEndianness,
        number_of_byte_to_read: int,
        expected_bytes_array: List[int],
    ):
        """unit test of create_array_for_spi_read_instruction."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (240 > 100 characters) (auto-generated noqa)

        logging.debug("running %s.", test_case_name)

        actual_bytes_array = create_command_for_spi_read_communication(
            address_parameters=communications.MemoryAddressParameters(
                memory_address=memory_address,
                address_type=address_type,
                address_endianness=address_endianness,
            ),
            number_of_bytes_to_read=number_of_byte_to_read,
        ).tolist()

        self.assertListEqual(expected_bytes_array, actual_bytes_array)


class TestCreateArrayForSpiWriteInstruction(unittest.TestCase):
    """Defines a test fixture that checks
    function `create_array_for_spi_write_instruction` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "one byte little endian 5 data bytes",
                12,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                [0x2, 12, 0, 0, 0, 0, 0],
            ),
            (
                "one byte little endian with 4th bit set 5 data bytes",
                268,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                # 0x2 | 0x8 => 11
                [10, 12, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes little endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                7,
                [0x2, 15, 12, 0, 0, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes big endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                7,
                [0x2, 12, 15, 0, 0, 0, 0, 0, 0, 0],
            ),
        ]
    )
    def test_create_array_for_spi_write_instruction(
        self,
        test_case_name: str,
        memory_address: int,
        address_type: nipcbatt.DataMemoryAddressType,
        address_endianness: nipcbatt.DataMemoryAddressEndianness,
        number_of_bytes_to_write: int,
        expected_bytes_array: List[int],
    ):
        """unit test of create_array_for_spi_write_instruction."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (241 > 100 characters) (auto-generated noqa)

        logging.debug("running %s.", test_case_name)

        actual_bytes_array = create_command_for_spi_write_communication(
            address_parameters=communications.MemoryAddressParameters(
                memory_address=memory_address,
                address_type=address_type,
                address_endianness=address_endianness,
            ),
            number_of_bytes_to_write=number_of_bytes_to_write,
        ).tolist()

        self.assertListEqual(expected_bytes_array, actual_bytes_array)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_voltage_data_types.py sha256=92e6533cc9ff1ce6dbd4e9a053b0dc5d55e1bcc5abcbbe3d3ac3dc7776a77d57 bytes=7506 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/common/test_voltage_data_types.py`
- sha256: `92e6533cc9ff1ce6dbd4e9a053b0dc5d55e1bcc5abcbbe3d3ac3dc7776a77d57`
- bytes: 7506

````python
# pylint: disable=C0116
"""This module provides voltage data types check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestVoltageRangeAndTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageRangeAndTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_voltage_range_and_terminal_parameters(self):
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3

        instance = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        actual_terminal_configuration = instance.terminal_configuration
        actual_range_min_volts = instance.range_min_volts
        actual_range_max_volts = instance.range_max_volts

        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)


class TestVoltageMeasurementChannelAndTerminalRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageMeasurementChannelAndTerminalRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_voltage_measurement_channel_and_terminal_range_parameters(self):
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_channel_name = "Dev/ai0"

        channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        instance = daq.VoltageMeasurementChannelAndTerminalRangeParameters(
            channel_name=expected_channel_name,
            channel_parameters=channel_parameters,
        )

        actual_channel_name = instance.channel_name
        actual_terminal_configuration = instance.channel_parameters.terminal_configuration
        actual_range_min_volts = instance.channel_parameters.range_min_volts
        actual_range_max_volts = instance.channel_parameters.range_max_volts

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)


class TestVoltageGenerationChannelParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageGenerationChannelParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_voltage_generation_channel_parameters(self):
        expected_range_min_volts = -3.5
        expected_range_max_volts = 4.0

        instance = daq.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        self.assertEqual(expected_range_min_volts, instance.range_min_volts)
        self.assertEqual(expected_range_max_volts, instance.range_max_volts)

    def test_voltage_generation_channel_parameters_with_invalid_inputs(self):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (285 > 100 characters) (auto-generated noqa)

        # Test if Valus error is raised when range Max = Min value
        self.assertRaises(
            ValueError,
            lambda: daq.VoltageGenerationChannelParameters(
                range_min_volts=3.0, range_max_volts=3.0
            ),
        )

        # Test if value error is raised when Min is greater than Max
        self.assertRaises(
            ValueError,
            lambda: daq.VoltageGenerationChannelParameters(
                range_min_volts=4.0,
                range_max_volts=3.5,
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/__init__.py sha256=0a4012fdf6242380b3f4a03ece0247fe2582e39591cd661ee64f3bc131fc6998 bytes=281 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/__init__.py`
- sha256: `0a4012fdf6242380b3f4a03ece0247fe2582e39591cd661ee64f3bc131fc6998`
- bytes: 281

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.dc_rms_current_measurements package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (209 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_data_types.py sha256=b229c94f2b8636fa1a51e1f6ead8f9001b3fc4078f7c525d351e22108789d7a4 bytes=46146 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_data_types.py`
- sha256: `b229c94f2b8636fa1a51e1f6ead8f9001b3fc4078f7c525d351e22108789d7a4`
- bytes: 46146

````python
"""This module provides DC-RMS current datatypes check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestDcRmsCurrentMeasurementTerminalRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementTerminalRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_current_measurement_terminal_range_parameters(self):
        """Tests if an instance of `DcRmsCurrentMeasurementTerminalRangeParameters`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.RSE
        expexted_range_min_amperes = -0.01
        expecte_range_max_amperes = 0.01
        expected_shunt_resistor_ohms = 0.02

        instance = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_amperes=expexted_range_min_amperes,
            range_max_amperes=expecte_range_max_amperes,
            shunt_resistor_ohms=expected_shunt_resistor_ohms,
        )
        actual_terminal_configuration = instance.terminal_configuration
        actual_range_min_amperes = instance.range_min_amperes
        actual_range_max_amperes = instance.range_max_amperes
        actual_shunt_resistor_ohms = instance.shunt_resistor_ohms

        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expexted_range_min_amperes, actual_range_min_amperes)
        self.assertEqual(expecte_range_max_amperes, actual_range_max_amperes)
        self.assertEqual(expected_shunt_resistor_ohms, actual_shunt_resistor_ohms)

    def test_dc_rms_current_measurement_terminal_range_invalid_parameters(self):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (285 > 100 characters) (auto-generated noqa)

        # Test if Valus error is raised when range max = min value
        self.assertRaises(
            ValueError,
            lambda: daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                range_min_amperes=0.02,
                range_max_amperes=0.02,
                shunt_resistor_ohms=0.001,
            ),
        )

        # Test if value error is raised when Min is greater than Max
        self.assertRaises(
            ValueError,
            lambda: daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                range_min_amperes=0.03,
                range_max_amperes=0.02,
                shunt_resistor_ohms=0.001,
            ),
        )

        # Test if value error is raised when shunt_resistor_ohms value is 0
        self.assertRaises(
            ValueError,
            lambda: daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                range_min_amperes=0.03,
                range_max_amperes=0.05,
                shunt_resistor_ohms=0.0,
            ),
        )

        # Test if Valus error is raised when terminal_configuration is None
        self.assertRaises(
            ValueError,
            lambda: daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=None,
                range_min_amperes=0.02,
                range_max_amperes=0.2,
                shunt_resistor_ohms=100.0,
            ),
        )


class TestDcRmsCurrentMeasurementChannelAndTerminalRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters(self):
        """Tests if an instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_channel_name = "dev1/ai1"
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expexted_range_min_amperes = 0.02
        expecte_range_max_amperes = 0.05
        expected_shunt_resistor_ohms = 0.1

        expected_channel_parameters = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_amperes=expexted_range_min_amperes,
            range_max_amperes=expecte_range_max_amperes,
            shunt_resistor_ohms=expected_shunt_resistor_ohms,
        )

        instance = daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
            channel_name=expected_channel_name,
            channel_parameters=expected_channel_parameters,
        )

        actual_channel_name = instance.channel_name
        actual_terminal_configuration = instance.channel_parameters.terminal_configuration
        actual_range_min_amperes = instance.channel_parameters.range_min_amperes
        actual_range_max_amperes = instance.channel_parameters.range_max_amperes
        actual_shunt_resistor_ohms = instance.channel_parameters.shunt_resistor_ohms

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expexted_range_min_amperes, actual_range_min_amperes)
        self.assertEqual(expecte_range_max_amperes, actual_range_max_amperes)
        self.assertEqual(expected_shunt_resistor_ohms, actual_shunt_resistor_ohms)

    def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters_with_invalid_channel_name(
        self,
    ):
        """Tests if the expected value or type error is thrown when creating an instance of
        `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` with invalid values
        for channel_name string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Check if value error is thrown when channel_name string is empty
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                    channel_name="",
                    channel_parameters=(
                        daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                    ),
                )
            )
        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

        # Check if value error is thrown when channel_name string is None
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                    channel_name=None,
                    channel_parameters=(
                        daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                    ),
                )
            )
        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters_when_channel_parameters_is_none(
        self,
    ):
        """Tests if the expected value or type error is thrown when creating an instance of
        `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` when channel_parameters is none.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Check if value error is thrown when channel_name string is empty
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                    channel_name="dev1/ch0",
                    channel_parameters=None,
                )
            )
        # Assert
        self.assertEqual(
            "The object channel_parameters is None.",
            str(ctx.exception),
        )


class TestDcRmsCurrentMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        # Create expected values constants for global_channel_parameters
        # of type DcRmsCurrentMeasurementTerminalRangeParameters
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expexted_range_min_amperes = -0.01
        expected_range_max_amperes = 0.01
        expected_shunt_resistor_ohms = 0.02

        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expexted_specific_range_min_amperes = -0.05
        expecte_specific_range_max_amperes = 0.05
        expected_specific_shunt_resistor_ohms = 0.1

        self._expected_global_channel_parameters = (
            daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=expected_terminal_configuration,
                range_min_amperes=expexted_range_min_amperes,
                range_max_amperes=expected_range_max_amperes,
                shunt_resistor_ohms=expected_shunt_resistor_ohms,
            )
        )
        # Log the class name with the values of the instance created for global_channel_parameters.
        logging.debug(
            "%s = %s",
            nameof(self._expected_global_channel_parameters),
            self._expected_global_channel_parameters,
        )

        # Create constants to test the measurement options
        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        self._expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )
        logging.debug(
            "%s = %s",
            nameof(self._expected_measurement_options),
            self._expected_measurement_options,
        )

        # Craete few constants to test the Specific_channel_parameters list
        self._expected_specific_channel_parameters = []
        self._expected_specific_channel_parameters.append(
            daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai0",
                channel_parameters=daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        self._expected_specific_channel_parameters.append(
            daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai1",
                channel_parameters=daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        self._expected_specific_channel_parameters.append(
            daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai2",
                channel_parameters=daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )

        # Log the class name with the values of the instance created
        # for specific channel parameters.
        logging.debug(
            "%s = %s",
            nameof(self._expected_specific_channel_parameters),
            self._expected_specific_channel_parameters,
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        self._expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )
        # Log the class name with the values of the instance
        # created for _expected_sample_clock_timing_parameters
        logging.debug(
            "%s = %s",
            nameof(self._expected_sample_clock_timing_parameters),
            self._expected_sample_clock_timing_parameters,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        self._expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )
        logging.debug(
            "%s = %s",
            nameof(self._expected_digital_start_trigger_parameters),
            self._expected_digital_start_trigger_parameters,
        )

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_current_measurement_configuration(self):
        """Tests if an instance of `DcRmsCurrentMeasurementConfiguration`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Create expected values constants for global_channel_parameters
        # of type DcRmsCurrentMeasurementTerminalRangeParameters
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expexted_range_min_amperes = -0.01
        expected_range_max_amperes = 0.01
        expected_shunt_resistor_ohms = 0.02

        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expexted_specific_range_min_amperes = -0.05
        expecte_specific_range_max_amperes = 0.05
        expected_specific_shunt_resistor_ohms = 0.1

        expected_global_channel_parameters = (
            daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=expected_terminal_configuration,
                range_min_amperes=expexted_range_min_amperes,
                range_max_amperes=expected_range_max_amperes,
                shunt_resistor_ohms=expected_shunt_resistor_ohms,
            )
        )

        # Create constants to test the measurement options
        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        # Craete few constants to test the Specific_channel_parameters list
        expected_specific_channel_parameters = []
        expected_specific_channel_parameters.append(
            daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai0",
                channel_parameters=daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        expected_specific_channel_parameters.append(
            daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai1",
                channel_parameters=daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        expected_specific_channel_parameters.append(
            daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai2",
                channel_parameters=daq.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Log the class name with the values of the instance created
        # for specific channel parameters.
        logging.debug(
            "%s = %s",
            nameof(expected_specific_channel_parameters),
            expected_specific_channel_parameters,
        )

        dc_rms_current_configuration_instance = daq.DcRmsCurrentMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=expected_specific_channel_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        # Log the class name with the values of the instance
        # created for DcRMSCurentMeasurementConfiguration
        logging.debug(
            "%s = %s",
            nameof(dc_rms_current_configuration_instance),
            dc_rms_current_configuration_instance,
        )

        # Check if all the elements in specific channel parameters list are as expected.
        self.assertListEqual(
            expected_specific_channel_parameters,
            dc_rms_current_configuration_instance.specific_channels_parameters,
        )

        # Get the actual parameters from the instance created
        actual_global_parameters = dc_rms_current_configuration_instance.global_channel_parameters

        actual_measurement_options = dc_rms_current_configuration_instance.measurement_options

        actual_sample_clock_timing_parameters = (
            dc_rms_current_configuration_instance.sample_clock_timing_parameters
        )

        # Test if all the actual parameters of the instance are as expected
        self.assertEqual(expected_global_channel_parameters, actual_global_parameters)

        self.assertEqual(expected_measurement_options, actual_measurement_options)
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            actual_sample_clock_timing_parameters,
        )

    def test_dc_rms_current_measurement_configuration_with_invalid_values_for_specific_channel_parameters(
        self,
    ):
        """Test if expected error is thrown when creating an instance
        of `DcRmsCurrentMeasurementConfiguration`
        with invalid values for specific_channel_parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=None,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

        self._expected_specific_channel_parameters.append("invalid channel parameter")

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters).",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_configuration_when_global_channel_parameters_is_none(
        self,
    ):
        """Test if expected error is thrown when creating an instance
        of `DcRmsCurrentMeasurementConfiguration`
        with global_channel_parameters is set to None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (426 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_configuration_when_measurement_options_is_none(
        self,
    ):
        """Test if expected error is thrown
        when creating an instance of `DcRmsCurrentMeasurementConfiguration`
        when measurement_options is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (413 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=None,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_configuration_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """Test if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementConfiguration`
        when sample_clock_timing_parameters is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (424 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_configuration_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """Test if expected error is thrown
        when creating an instance of `DcRmsCurrentMeasurementConfiguration`
        when digital_start_trigger_parameters is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (426 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=None,
                )
            )
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))


class TestDcRmsCurrentMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self._expected_waveforms = []
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )

        self._expected_acquisition_duration_seconds = 0.25

        self._expected_dc_values_amperes = [0.12, 0.012, 0.12]
        self._expected_rms_values_amperes = [0.15, 0.14, 0.15]

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_current_measurement_result_data(self):
        """Tests if an instance of `DcRmsCurrentMeasurementResultData`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = daq.DcRmsCurrentMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
            dc_values_amperes=self._expected_dc_values_amperes,
            rms_values_amperes=self._expected_rms_values_amperes,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_waveforms = instance.waveforms
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds
        actual_dc_values_amperes = instance.dc_values_amperes
        actual_rms_values_amperes = instance.rms_values_amperes

        self.assertListEqual(self._expected_waveforms, actual_waveforms)
        self.assertEqual(
            self._expected_acquisition_duration_seconds,
            actual_acquisition_duration_seconds,
        )
        self.assertListEqual(self._expected_dc_values_amperes, actual_dc_values_amperes)
        self.assertListEqual(self._expected_rms_values_amperes, actual_rms_values_amperes)

    def test_dc_rms_current_measurement_result_data_when_waveforms_is_none(self):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` with waveform as none.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_result_data_when_waveforms_has_item_not_of_type_analogwaveform(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveform has an item
        that is not of type `AnalogWaveform`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_waveforms.append([0.5, 1.2])

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_result_data_when_dc_values_amperes_has_item_not_of_type_float(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when dc_values_amperes
        has an item that is not of type float.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_dc_values_amperes.append("two")

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_result_data_when_rms_values_amperes_has_item_not_of_type_float(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when rms_values_amperes
        has an item that is not of type float.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_rms_values_amperes.append([1.0])

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )
        # "The iterables ({} and {}) do not have same size."

    def test_dc_rms_current_measurement_result_data_when_waveforms_and_rms_values_amperes_have_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveforms list and
        rms_values_amperes have list have different lengths
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_rms_values_amperes.append(1.0)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )

            
        self.assertEqual(
            "The iterables (waveforms and rms_values_amperes) do not have same size.",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_result_data_when_waveforms_and_dc_values_amperes_have_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveforms list and
        dc_values_amperes have list have different lengths
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_dc_values_amperes.append(1.0)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and dc_values_amperes) do not have same size.",
            str(ctx.exception),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_measurement.py sha256=cf00cf8baf24ff04475241ba7eb0dd0e01dfb8b27a89ec690a26df8104ef1f92 bytes=3068 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_measurement.py`
- sha256: `cf00cf8baf24ff04475241ba7eb0dd0e01dfb8b27a89ec690a26df8104ef1f92`
- bytes: 3068

````python
"""This module provides DcRmsCurrentMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_analysis import analysis_library_info


class TestDcRmsCurrentMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx(_InterpreterDcRmsCurrentMeasurement)

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_dc_rms_current_measurement(self):
        """Tests for the proper flow of DC-RMS Current Measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
        measurement = daq.DcRmsCurrentMeasurement()
        measurement.initialize(analog_input_channel_expression="Sim_PXIeDAQ/ai0:2")
        measurement.configure_and_measure(
            configuration=daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION
        )
        measurement.close()

    def test_dc_rms_current_measurement_analysis_with_empty_data(self):
        """Tests if calling analyze_measurement_data
        with None as measure_data input raises Attribute error as expected."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (371 > 100 characters) (auto-generated noqa)
        measurement = daq.DcRmsCurrentMeasurement()
        self.assertRaises(
            TypeError,
            lambda: measurement.analyze_measurement_data(measurement_data=None),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dmm_dc_rms_current_data_types.py sha256=d71374e78276243a97d14b16a137e18b2b1083bf1e285bab6d293cfafd2d7f70 bytes=5916 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dmm_dc_rms_current_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dmm_dc_rms_current_data_types.py`
- sha256: `d71374e78276243a97d14b16a137e18b2b1083bf1e285bab6d293cfafd2d7f70`
- bytes: 5916

````python
""" Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based DC-RMS measurements """

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import dmm

class TestDMMDcRmsCurrent(unittest.TestCase):
    """Defines a test fixture that ensures the data types of the 
        dmm.DcRmsCurrentMeasurement class are created correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidmm_version = importlib.metadata.version("nidmm")
        logging.debug("%s = %s", nameof(used_nidmm_version), used_nidmm_version)
        
    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")


    def test_enum_members_shape_and_types(self):
        "Tests the creation of different type and shapes of enums"

        range_values = [member.value for member in dmm.CurrentRangeAndFunctions]

        for value in range_values:
            data = dmm.CurrentRangeAndFunctions(value)
            self.assertEqual(value, data.value)

    
    def test_function_params_basic_construction_and_properties(self):
        """Create a DcRmsCurrentMeasurementFunctionParameters and verify properties."""

        RESOLUTION = 6.5

        target_member = dmm.CurrentRangeAndFunctions.DC_10mA
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=target_member,
            resolution_in_digits=resolution,
        )

        # Verify properties return exactly what we passed in
        self.assertIs(params.measurement_function, target_member)
        self.assertIs(params.resolution_in_digits, resolution)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    
    def test_properties_are_effectively_read_only(self):
        """Attempting to assign to properties should raise AttributeError."""
        RESOLUTION = 5.5

        initial_member = dmm.CurrentRangeAndFunctions.AC_100mA
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=initial_member,
            resolution_in_digits=resolution,
        )

        # The class exposes read-only properties (no setters). Direct assignment should fail.
        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.CurrentRangeAndFunctions.DC_1mA)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        # Confirm original values unchanged
        self.assertIs(params.measurement_function, initial_member)
        self.assertIs(params.resolution_in_digits, resolution)


    def test_basic_construction_and_properties(self):
        """Create params and verify properties return the same objects."""

        RESOLUTION = 6.5

        member = dmm.CurrentRangeAndFunctions.DC_10mA
        res = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)

    
    def test_construct_for_every_current_range_enum_value(self):
        """Iterate all CurrentRangeAndFunctions, instantiate params, and verify."""
       
        res = dmm.ResolutionInDigits(5.5)

        for member in dmm.CurrentRangeAndFunctions:
            params = dmm.DcRmsCurrentMeasurementFunctionParameters(
                measurement_function=member,
                resolution_in_digits=res,
            )
            self.assertIs(params.measurement_function, member)
            self.assertIs(params.resolution_in_digits, res)

    
    def test_dcrms_meas_config_properties_are_read_only(self):

        "Ensure all function properties are read only"

        member = dmm.CurrentRangeAndFunctions.AC_100mA
        res = dmm.ResolutionInDigits(6.5)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.CurrentRangeAndFunctions.DC_1mA)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)

    
    def test_identity_of_references(self):

        "Make sure the same object is returned, not a copy"

        member = dmm.CurrentRangeAndFunctions.DC_1A
        res = dmm.ResolutionInDigits(7.5)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)






            
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/__init__.py sha256=7d42b8b670a5dce01bfd2cf138587cc91af97ee934ff710f86bf1b7f7e5292e9 bytes=281 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/__init__.py`
- sha256: `7d42b8b670a5dce01bfd2cf138587cc91af97ee934ff710f86bf1b7f7e5292e9`
- bytes: 281

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.dc_rms_voltage_measurements package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (209 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_data_types.py sha256=e826a58aba93a85a9d78c90251f6ea2bef08f6470cdab40c40b2d5d0c0a49533 bytes=27775 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_data_types.py`
- sha256: `e826a58aba93a85a9d78c90251f6ea2bef08f6470cdab40c40b2d5d0c0a49533`
- bytes: 27775

````python
"""This module provides DC-RMS voltage datatypes check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestDcRmsVoltageMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsVoltageMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_options=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_specific_channels_parameters_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[1.2, "4"],
                    measurement_options=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (VoltageMeasurementChannelAndTerminalRangeParameters).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_measurement_options_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=None,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration(self):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expected_specific_range_min_volts = -5.0
        expected_specific_range_max_volts = 7.5

        expected_global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        specific_channels_parameters = []
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai0",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai1",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai2",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )

        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        logging.debug(
            "%s = %s",
            nameof(specific_channels_parameters),
            specific_channels_parameters,
        )

        dc_rms_configuration_instance = daq.DcRmsVoltageMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=specific_channels_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(dc_rms_configuration_instance),
            dc_rms_configuration_instance,
        )

        self.assertListEqual(
            specific_channels_parameters,
            dc_rms_configuration_instance.specific_channels_parameters,
        )

        actual_global_channel_parameters = dc_rms_configuration_instance.global_channel_parameters
        actual_measurement_options = dc_rms_configuration_instance.measurement_options
        actual_sample_clock_timing_parameters = (
            dc_rms_configuration_instance.sample_clock_timing_parameters
        )

        self.assertEqual(expected_global_channel_parameters, actual_global_channel_parameters)
        self.assertEqual(expected_measurement_options, actual_measurement_options)
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            actual_sample_clock_timing_parameters,
        )


class TestDcRmsVoltageMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsVoltageMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=[],
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=[0.0, "2"],
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=None,
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The object dc_values_volts is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_is_empty(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The iterable dc_values_volts of type list is empty.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=["0.0", 2.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=None,
                )
            )

        # Assert
        self.assertEqual("The object rms_values_volts is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_is_empty(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[],
                )
            )

        # Assert
        self.assertEqual("The iterable rms_values_volts of type list is empty.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=["0.0", 2.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_result_data(self):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        expected_waveforms = []
        expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        )
        expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )
        expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )

        expected_acquisition_duration_seconds = 0.3

        expected_dc_values_volts = [1.0, 1.0, 1.0]
        expected_rms_values_volts = [2.0, 2.0, 0.0]
        instance = daq.DcRmsVoltageMeasurementResultData(
            waveforms=expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            dc_values_volts=expected_dc_values_volts,
            rms_values_volts=expected_rms_values_volts,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_waveforms = instance.waveforms
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds
        actual_dc_values_volts = instance.dc_values_volts
        actual_rms_values_volts = instance.rms_values_volts

        self.assertListEqual(expected_waveforms, actual_waveforms)
        self.assertEqual(expected_acquisition_duration_seconds, actual_acquisition_duration_seconds)
        self.assertListEqual(expected_dc_values_volts, actual_dc_values_volts)
        self.assertListEqual(expected_rms_values_volts, actual_rms_values_volts)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_measurement.py sha256=605534f81886070f5cf266229ecdbed089fe7b95c96f7e97624c22ec8c47fba0 bytes=2334 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_measurement.py`
- sha256: `605534f81886070f5cf266229ecdbed089fe7b95c96f7e97624c22ec8c47fba0`
- bytes: 2334

````python
# pylint: disable=C0301
"""This module provides DcRmsVoltageMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq
'''from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)'''


class TestDcRmsVoltageMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsVoltageMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_rms_voltage_measurement(self):
        """Checks if class DcRmsVoltageMeasurement is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
        with daq.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression="Sim_PXIeDAQ/ai0"
            )

            measurement.configure_and_measure(
                configuration=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
            )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dmm_dc_rms_voltage_data_types.py sha256=dd54a83a4cc7cb470167d5ca4d7566996bff812e80a979bd62590d3a0d151953 bytes=5079 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dmm_dc_rms_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dmm_dc_rms_voltage_data_types.py`
- sha256: `dd54a83a4cc7cb470167d5ca4d7566996bff812e80a979bd62590d3a0d151953`
- bytes: 5079

````python
""" Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based DC-RMS voltage measurements """

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import dmm

class TestDMMDcRmsVoltage(unittest.TestCase):
    """Defines a test fixture that ensures the enums are created 
        correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        """
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidmm_version = importlib.metadata.version("nidmm")
        logging.debug("%s = %s", nameof(used_nidmm_version), used_nidmm_version)
        
    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    
    def test_enum_members_shape_and_types(self):
        "Tests the creation of different type and shapes of enums"

        range_values = [member.value for member in dmm.VoltageRangeAndFunctions]

        for value in range_values:
            data = dmm.VoltageRangeAndFunctions(value)
            self.assertEqual(value, data.value)


    def test_properties_are_effectively_read_only(self):
        """Attempting to assign to properties should raise AttributeError."""
        RESOLUTION = 5.5

        initial_member = dmm.VoltageRangeAndFunctions.AC_200mV
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=initial_member,
            resolution_in_digits=resolution,
        )

        # The class exposes read-only properties (no setters). Direct assignment should fail.
        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.VoltageRangeAndFunctions.AC_50mV)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        # Confirm original values unchanged
        self.assertIs(params.measurement_function, initial_member)
        self.assertIs(params.resolution_in_digits, resolution)


    def test_basic_construction_and_properties(self):
        """Create params and verify properties return the same objects."""

        RESOLUTION = 6.5

        member = dmm.VoltageRangeAndFunctions.DC_100mV
        res = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    def test_construct_for_every_voltage_range_enum_value(self):
        """Iterate all VoltageRangeAndFunctions, instantiate params, and verify."""
       
        res = dmm.ResolutionInDigits(5.5)

        for member in dmm.VoltageRangeAndFunctions:
            params = dmm.DcRmsVoltageMeasurementFunctionParameters(
                measurement_function=member,
                resolution_in_digits=res,
            )
            self.assertIs(params.measurement_function, member)
            self.assertIs(params.resolution_in_digits, res)


    def test_dcrms_meas_config_properties_are_read_only(self):

        "Ensure all function properties are read only"

        member = dmm.VoltageRangeAndFunctions.AC_200mV
        res = dmm.ResolutionInDigits(6.5)

        params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.VoltageRangeAndFunctions.DC_1V)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)


    def test_identity_of_references(self):

        "Make sure the same object is returned, not a copy"

        member = dmm.VoltageRangeAndFunctions.DC_1V
        res = dmm.ResolutionInDigits(7.5)

        params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/__init__.py sha256=7ec79c5a347ddf5d599962354d6f4978195e3ea266321992bd1cd4f2b9d7a783 bytes=276 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/__init__.py`
- sha256: `7ec79c5a347ddf5d599962354d6f4978195e3ea266321992bd1cd4f2b9d7a783`
- bytes: 276

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.dc_voltage_generations package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (204 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_data_types.py sha256=98558554fad23ed4ed6524f2cd958e7b575981456b624ae95c463690292b523b bytes=4484 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_data_types.py`
- sha256: `98558554fad23ed4ed6524f2cd958e7b575981456b624ae95c463690292b523b`
- bytes: 4484

````python
"""This module provides DC Voltage data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestDcVoltageGenerationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    'DcVoltageGenerationConfiguration' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_voltage_generation_configuration(self):
        """Tests if the instance of `DcVoltageGenerationConfiguration` is created as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (207 > 100 characters) (auto-generated noqa)
        expected_range_min_volts = -5.0
        expected_range_max_volts = 5.0
        expected_output_voltages = [1.2, 2.8, 3.2]
        expected_voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        instance = daq.DcVoltageGenerationConfiguration(
            voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
            output_voltages=expected_output_voltages,
        )

        actual_range_min_volts = instance.voltage_generation_range_parameters.range_min_volts
        actual_range_max_volts = instance.voltage_generation_range_parameters.range_max_volts
        actual_output_voltages = instance.output_voltages

        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)

        self.assertListEqual(expected_output_voltages, actual_output_voltages)

    def test_dc_voltage_generation_configuration_with_empty_channel_parameters(self):
        """Tests if the Value error is raised when tried to create an
        instance of `DcVoltageGenerationConfiguration` with empty channel parameters"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (380 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.DcVoltageGenerationConfiguration(
                voltage_generation_range_parameters=None,
                output_voltages=[],
            ),
        )

    def test_dc_voltage_generation_configuration_with_empty_output_voltages(self):
        """Tests if the Value error is raised when tried to create an
        instance of `DcVoltageGenerationConfiguration` with empty output_voltages array
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.DcVoltageGenerationConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS
                ),
                output_voltages=[],
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_generation.py sha256=f54f4800ea0fba3670e39c43a1b1dccb40a32c471ab9fe822900038d43e07da1 bytes=2296 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_generation.py`
- sha256: `f54f4800ea0fba3670e39c43a1b1dccb40a32c471ab9fe822900038d43e07da1`
- bytes: 2296

````python
"""This module provides DcVoltageGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof


from nipcbatt import daq
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestDcVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks
    `DcVoltageGeneration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_voltage_generation(self):
        """Checks if class `DcVoltageGeneration' is ready for use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (256 > 100 characters) (auto-generated noqa)

        generation = daq.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="Sim_PXIeDAQ/ao0"
        )
        generation.configure_and_generate(
            configuration=daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
        )
        generation.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/__init__.py sha256=d61d0d71e2b4b895f44a8ee7b22c1baa07b9ab7b3b1a0d20041ccd702995c92a bytes=279 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/__init__.py`
- sha256: `d61d0d71e2b4b895f44a8ee7b22c1baa07b9ab7b3b1a0d20041ccd702995c92a`
- bytes: 279

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.digital_clock_generations package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (207 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_data_types.py sha256=33742588c58d00efffc755dfbdf4f8c7d21419727aaaa3ccf84687b6a4b741ec bytes=12623 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_data_types.py`
- sha256: `33742588c58d00efffc755dfbdf4f8c7d21419727aaaa3ccf84687b6a4b741ec`
- bytes: 12623

````python
"""This module provides digital clock data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof
from nipcbatt import daq


class TestDigitalClockGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to unsure the data types class used for digital clock
       generation are ready to use.

    Args:
        unittest.testCase: Parent class of the unittest framework
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_clock_generation_timing_parameters(self):
        """Tests if an instance of DigitalClockGenerationTimingParameters is
        created with specific values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (409 > 100 characters) (auto-generated noqa)

        expected_duration = 1.0
        instance = daq.DigitalClockGenerationTimingParameters(expected_duration)
        actual_duration = instance.clock_duration_seconds

        self.assertEqual(expected_duration, actual_duration)

    def test_digital_clock_generation_timing_parameters_with_invalid_data(self):
        """Tests if an instance of DigitalClockGenerationTimingParameters throws
        an error if given invalid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        expected_duration = 0.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationTimingParameters(expected_duration),
        )

        self.assertRaises(ValueError, lambda: daq.DigitalClockGenerationTimingParameters(None))

    def test_digital_clock_generation_counter_channel_parameters(self):
        """Tests if an instance of DigitalClockGenerationCounterChannelParameters
        is produced with specfic values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (412 > 100 characters) (auto-generated noqa)

        expected_frequency = 1000.0
        expected_duty_cycle = 0.95

        instance = daq.DigitalClockGenerationCounterChannelParameters(
            expected_frequency, expected_duty_cycle
        )

        self.assertEqual(expected_frequency, instance.frequency_hertz)
        self.assertEqual(expected_duty_cycle, instance.duty_cycle_ratio)

    def test_digital_clock_generation_counter_channel_parameters_with_invalid_data(
        self,
    ):
        """Tests if an attempted instance of DigitalClockGenerationCounterChannelParameters
        throws an error when given incorrect values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (424 > 100 characters) (auto-generated noqa)

        frequency = -0.1  # frequency can't be less than 0
        duty_cycle = 0.5

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationCounterChannelParameters(frequency, duty_cycle),
        )

        frequency = 10
        duty_cycle = 1.1  # duty cycle can't be greater than 1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationCounterChannelParameters(frequency, duty_cycle),
        )

        frequency = 10
        duty_cycle = -0.1  # duty cycle can't be less than 0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationCounterChannelParameters(frequency, duty_cycle),
        )

    def test_digital_clock_generation_configuration(self):
        """Tests if an instance of DigitalClockGenerationConfiguration is
        successfully created when given the proper arugments"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (433 > 100 characters) (auto-generated noqa)

        freq = 100.0
        duty_cycle = 0.5
        duration = 1.0

        counter_channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
            freq, duty_cycle
        )
        timing_parameters = daq.DigitalClockGenerationTimingParameters(duration)

        expected_channel_parameters = counter_channel_parameters
        expected_timing_parameters = timing_parameters

        instance = daq.DigitalClockGenerationConfiguration(
            expected_channel_parameters, expected_timing_parameters
        )

        actual_channel_parameters = instance.counter_channel_parameters
        actual_timing_parameters = instance.timing_parameters

        self.assertEqual(expected_channel_parameters, actual_channel_parameters)
        self.assertEqual(expected_timing_parameters, actual_timing_parameters)

    def test_digital_clock_generation_configuration_with_invalid_data(self):
        """Tests if instantiaion of DigitalClockGenerationConfiguration fails
        when given invalid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (404 > 100 characters) (auto-generated noqa)

        freq = 100.0
        duty_cycle = 0.5
        duration = 1.0

        counter_channel_parameters = None
        timing_parameters = daq.DigitalClockGenerationTimingParameters(duration)

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationConfiguration(
                counter_channel_parameters, timing_parameters
            ),
        )

        counter_channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
            freq, duty_cycle
        )
        timing_parameters = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationConfiguration(
                counter_channel_parameters, timing_parameters
            ),
        )

    def test_digital_clock_generation_data(self):
        """Test if an instance of DigitalClockGenerationData is created
        successfully when given the proper values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = 1.0

        instance = daq.DigitalClockGenerationData(
            expected_timebase_freq,
            expected_actual_clock_freq,
            expected_actual_clock_duty_cycle,
            expected_actual_clock_duration,
        )

        self.assertEqual(expected_timebase_freq, instance.timebase_frequency_hertz)
        self.assertEqual(expected_actual_clock_freq, instance.actual_clock_frequency_hertz)
        self.assertEqual(expected_actual_clock_duty_cycle, instance.actual_clock_duty_cycle_ratio)
        self.assertEqual(expected_actual_clock_duration, instance.actual_clock_duration_seconds)

    def test_digital_clock_generation_with_invalid_data(self):
        """Ensures that the attempted creation of an instance of
        DigitalClockGenerationData with invalid data throws an error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (441 > 100 characters) (auto-generated noqa)

        expected_timebase_freq = -1
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = 1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = -100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = 1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = -0.5
        expected_actual_clock_duration = 1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = -1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_generation.py sha256=eb62a93ad702eeefac86935c5608542d2a1206e5c365339bf5e2a72371d67453 bytes=2287 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_generation.py`
- sha256: `eb62a93ad702eeefac86935c5608542d2a1206e5c365339bf5e2a72371d67453`
- bytes: 2287

````python
"""This module provides DigitalClockGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof
from nipcbatt import daq


class TestDigitalClockGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DigitalClockGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class for unit tests which is inherited
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_clock_generation(self):
        """Checks if class 'DigitalClockGeneration' is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (258 > 100 characters) (auto-generated noqa)

        physical_channel = "Sim_PXIeDAQ/ctr0"
        output_terminal = "/Sim_PXIeDAQ/PFI12"
        timing_parameters = daq.DigitalClockGenerationTimingParameters(1.0)
        counter_parameters = daq.DigitalClockGenerationCounterChannelParameters(1000.0, 0.5)
        config = daq.DigitalClockGenerationConfiguration(counter_parameters, timing_parameters)

        gen = daq.DigitalClockGeneration()
        gen.initialize(physical_channel, output_terminal)
        gen.configure_and_generate(config)
        gen.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/__init__.py sha256=c5e8ef90d78b1ef1211ee597d5eb368851699f2e059bade5281cc98e8df74e1f bytes=285 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/__init__.py`
- sha256: `c5e8ef90d78b1ef1211ee597d5eb368851699f2e059bade5281cc98e8df74e1f`
- bytes: 285

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.digital_edge_count_measurements package"""  # noqa: W505, D415 - doc line too long (102 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_data_types.py sha256=469eabf3dd4f116c2439e94915df615c8f82c242f614c3f3dd0a44bcfe34b081 bytes=20215 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_data_types.py`
- sha256: `469eabf3dd4f116c2439e94915df615c8f82c242f614c3f3dd0a44bcfe34b081`
- bytes: 20215

````python
"""This module provides DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer Datatypes check."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (365 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx
import nidaqmx.constants
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestDynamicDigitalEdgeCountMeasuremntDataTypes(unittest.TestCase):
    """Defines a test fixture that checks
    `DigitalEdgeCountMeasuremntDataTypes` class is ready to use.

    Args:
         unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_edge_count_measurement_counter_channel_parameter_init_fails_when_edge_type_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementCounterChannelParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=None,
                )
            )

        self.assertEqual(
            "The object edge_type is None.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_counter_channel_parameter(self):
        """Tests if the instance of `DigitalEdgeCountMeasurementCounterChannelParameters`
        is created as expected"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)
        instance = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=nidaqmx.constants.Edge.FALLING
        )

        actual_edge_type = instance.edge_type

        self.assertEqual(nidaqmx.constants.Edge.FALLING, actual_edge_type)

    def test_digital_edge_count_measurement_timing_parameter_init_fails_when_edge_counting_duration_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementTimingParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=None,
                )
            )

        self.assertEqual(
            "The object edge_counting_duration is None.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_timing_parameter_init_fails_when_edge_counting_duration_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementTimingParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=-0.01,
                )
            )

        self.assertEqual(
            "The value edge_counting_duration must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_timing_parameter(self):
        """Tests if the instance of `DigitalEdgeCountMeasurementTimingParameters`
        is created as expected"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)
        instance = daq.DigitalEdgeCountMeasurementTimingParameters(edge_counting_duration=0.005)

        actual_edge_counting_duration = instance._edge_counting_duration

        self.assertEqual(0.005, actual_edge_counting_duration)

    def test__digital_edge_count_hardware_timer_configuration(self):
        """Tests if the instance of `DigitalEdgeCountHardwareTimerConfiguration`
        is created as expected"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        # Create test values for the Counter Channel Parameter
        expected_edge_type = nidaqmx.constants.Edge.FALLING

        expected_counter_channel_parameter = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=expected_edge_type,
        )

        # Create test values for the Timing Parameter
        expected_edge_counting_duration = 0.005

        expected_timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=expected_edge_counting_duration,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.RISING

        expected_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for measurement options
        expected_measurement_options = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE

        instance = daq.DigitalEdgeCountHardwareTimerConfiguration(
            measurement_options=expected_measurement_options,
            counter_channel_parameters=expected_counter_channel_parameter,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        # Log the class name with the values of the instance created for
        # DigitalEdgeCountHardwareTimerConfiguration
        logging.debug(
            "%s = %s",
            nameof(daq.DigitalEdgeCountHardwareTimerConfiguration),
            instance,
        )

        self.assertEqual(expected_measurement_options, instance.measurement_options)
        self.assertEqual(expected_counter_channel_parameter, instance.counter_channel_parameters)
        self.assertEqual(expected_timing_parameters, instance.timing_parameters)
        self.assertEqual(expected_trigger_parameters, instance.trigger_parameters)

    def test__digital_edge_count_software_timer_configuration(self):
        """Tests if the instance of `DigitalEdgeCountSoftwareTimerConfiguration`
        is created as expected"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        # Create test values for the Counter Channel Parameter
        expected_edge_type = nidaqmx.constants.Edge.FALLING

        expected_counter_channel_parameter = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=expected_edge_type,
        )

        # Create test values for the Timing Parameter
        expected_edge_counting_duration = 0.005

        expected_timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=expected_edge_counting_duration,
        )

        # Create test values for measurement options
        expected_measurement_options = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE

        instance = daq.DigitalEdgeCountSoftwareTimerConfiguration(
            measurement_options=expected_measurement_options,
            counter_channel_parameters=expected_counter_channel_parameter,
            timing_parameters=expected_timing_parameters,
        )

        # Log the class name with the values of the instance created for
        # DigitalEdgeCountSoftwareTimerConfiguration
        logging.debug(
            "%s = %s",
            nameof(daq.DigitalEdgeCountSoftwareTimerConfiguration),
            instance,
        )

        self.assertEqual(expected_measurement_options, instance.measurement_options)
        self.assertEqual(expected_counter_channel_parameter, instance.counter_channel_parameters)
        self.assertEqual(expected_timing_parameters, instance.timing_parameters)

    def test_digital_edge_count_hardware_timer_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (208 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=None,
                counter_channel_parameters= daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters= daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                    digital_start_trigger_source="triggersource",
                    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=None,
                timing_parameters= daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                    digital_start_trigger_source="triggersource",
                    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters= daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=None,
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                    digital_start_trigger_source="triggersource",
                    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters= daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters= daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
                trigger_parameters=None,
            ),
        )

    def test_digital_edge_count_software_timer_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (208 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=None,
                counter_channel_parameters= daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters= daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=None,
                timing_parameters= daq.DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters= daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=None,
            ),
        )

    def test_digital_edge_count_measurement_result_data_init_fails_when_edge_count_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DigitalEdgeCountMeasurementResultData(
                    edge_count=None,
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )

        self.assertEqual(
            "The object edge_count is None.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_result_data_init_fails_when_edge_count_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DigitalEdgeCountMeasurementResultData(
                    edge_count=-1,
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )

        self.assertEqual(
            "The value edge_count must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_result_data_init_fails_when_edge_type_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DigitalEdgeCountMeasurementResultData(
                    edge_count=5,
                    edge_type=None,
                )
            )

        self.assertEqual(
            "The object edge_type is None.",
            str(ctx.exception),
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_measurement.py sha256=7d769c6c73da68146b6f2385b2aa1b2f21357dd3c32015c4cefa4df39e3f9647 bytes=6875 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_measurement.py`
- sha256: `7d769c6c73da68146b6f2385b2aa1b2f21357dd3c32015c4cefa4df39e3f9647`
- bytes: 6875

````python
"""This module provides DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer check."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx
import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_constants import (  # noqa: F401 - 'nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants.ConstantsForDigitalEdgeCountMeasurement' imported but unused (auto-generated noqa)
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData' imported but unused (auto-generated noqa)
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_measurement_using_hardware_timer import (
    DigitalEdgeCountMeasurementUsingHardwareTimer,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_measurement_using_software_timer import (
    DigitalEdgeCountMeasurementUsingSoftwareTimer,
)

# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
#    _MockInterpreter,
# )
# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
#    _replace_daqmx,
# )


class TestDigitalEdgeCountMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class'DigitalEdgeCountMeasurementUsingHardwareTimer'  or
    'DigitalEdgeCountMeasurementUsingHardwareTimer' is correct and ready to use,

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: W505, D205, D415 - doc line too long (103 > 100 characters) (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        # _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_edge_count_measurement_using_hardware_timer(self):
        """Checks if class 'DigitalEdgeCountMeasurementUsingHardwareTimer' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (205 > 100 characters) (auto-generated noqa)
        meas = DigitalEdgeCountMeasurementUsingHardwareTimer()
        meas.initialize(
            measurement_channel_expression="Simulated_TS1_Core/ctr1",
            measurement_input_terminal_name="/Simulated_TS1_Core/PFI6",
            timer_channel_expression="Simulated_TS1_Core/ctr2",
        )

        counter_channel_parameters = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=nidaqmx.constants.Edge.FALLING,
        )
        timing_parameters = DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=0.005,
        )
        trigger_parameters = DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="/Simulated_TS1_Core/PFI0",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )
        configuration = DigitalEdgeCountHardwareTimerConfiguration(
            measurement_options=nipcbatt.MeasurementOptions(
                execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
            ),
            counter_channel_parameters=counter_channel_parameters,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )
        meas.configure_and_measure(
            configuration=configuration,
        )
        meas.close()

    def test_digital_edge_count_measurement_using_software_timer(self):
        """Checks if class 'DigitalEdgeCountMeasurementUsingSoftwareTimer' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (205 > 100 characters) (auto-generated noqa)
        meas = DigitalEdgeCountMeasurementUsingSoftwareTimer()
        meas.initialize(
            measurement_channel_expression="Simulated_TS1_Core/ctr3",
            measurement_input_terminal_name="/Simulated_TS1_Core/PFI7",
        )
        counter_channel_parameters = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=nidaqmx.constants.Edge.FALLING,
        )
        timing_parameters = DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=0.005,
        )
        configuration = DigitalEdgeCountSoftwareTimerConfiguration(
            measurement_options=nipcbatt.MeasurementOptions(
                execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
            ),
            timing_parameters=timing_parameters,
            counter_channel_parameters=counter_channel_parameters,
        )
        meas.configure_and_measure(
            configuration=configuration,
        )
        meas.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/__init__.py sha256=11d852c6ca34796b4563bf4b6e59933d57b39eefcced247076151db68cb230f2 bytes=284 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/__init__.py`
- sha256: `11d852c6ca34796b4563bf4b6e59933d57b39eefcced247076151db68cb230f2`
- bytes: 284

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.digital_frequency_measurements package"""  # noqa: W505, D415 - doc line too long (101 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_data_types.py sha256=0461ae5357d22bb25b9d0ee674b748489b9864597f8ee69c9b6b336d7f31af97 bytes=12333 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_data_types.py`
- sha256: `0461ae5357d22bb25b9d0ee674b748489b9864597f8ee69c9b6b336d7f31af97`
- bytes: 12333

````python
"""This module provides digital frequency data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import daq


class TestDigitalFrequencyRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DigitalFrequencyRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_frequency_range_parameters(self):
        """Tests if an instance of `DigitalFrequencyRangeParameters`
        is created with the specific values.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        expected_minimum_frequency = 1.0
        expected_maximum_frequency = 999999999.0

        instance = daq.DigitalFrequencyRangeParameters(
            frequency_minimum_value_hertz=expected_minimum_frequency,
            frequency_maximum_value_hertz=expected_maximum_frequency,
        )

        actual_minimum_frequency = instance.frequency_minimum_value_hertz
        actual_maximum_frequency = instance.frequency_maximum_value_hertz

        self.assertEqual(expected_minimum_frequency, actual_minimum_frequency)
        self.assertEqual(expected_maximum_frequency, actual_maximum_frequency)

    def test_digital_frequency_range_parameters_with_invalid_data(self):
        """Tests if an instance of `DigitalFrequencyRangeParameters`
        is created with the invalid values.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        expected_minimum_frequency = None
        expected_maximum_frequency = 999999999.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = -0.01
        expected_maximum_frequency = 999999999.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = 1.0
        expected_maximum_frequency = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = 1.0
        expected_maximum_frequency = -0.01

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = 10.0
        expected_maximum_frequency = 5.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

    def test_digital_frequency_measurement_configuration(self):
        """Tests if an instance of DigitalFrequencyMeasurementConfiguration
        is created successfully when given correct input
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_freq = 1.0
        max_freq = 999999999.0

        expected_range_param = daq.DigitalFrequencyRangeParameters(min_freq, max_freq)
        expected_input_divisor = 100.0
        expected_duration = 1.0

        expected_config = daq.DigitalFrequencyMeasurementCounterChannelParameters(
            expected_range_param, expected_input_divisor, expected_duration
        )

        instance = daq.DigitalFrequencyMeasurementConfiguration(expected_config)

        actual_config = instance.counter_channel_configuration_parameters

        self.assertEqual(expected_config, actual_config)

    def test_digital_frequency_measurement_configuration_with_invalid_data(self):
        """Tests if an instance of DigitalFrequencyMeasurementConfiguration
        throws errors during instantiation when given incorrect input
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # DigitalFrequencyMeasurementCounterChannelParameters is None
        self.assertRaises(ValueError, lambda: daq.DigitalFrequencyMeasurementConfiguration(None))

    def test_digital_frequency_measurement_counter_channel_parameters(self):
        """Tests if an instance of DigitalFrequencyMeasurementCounterChannelParameters
        is created successfully when given correct input
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        expected_min_freq = 0.0
        expected_max_freq = 999999999.0
        expected_range_param = daq.DigitalFrequencyRangeParameters(expected_min_freq, expected_max_freq)
        expected_input_divisor = 100.0
        expected_duration = 1.0

        instance = daq.DigitalFrequencyMeasurementCounterChannelParameters(
            expected_range_param, expected_input_divisor, expected_duration
        )

        actual_min_frequency = instance.range_parameters.frequency_minimum_value_hertz
        actual_max_frequency = instance.range_parameters.frequency_maximum_value_hertz
        actual_input_divisor = instance.input_divisor_for_frequency_measurement
        actual_measurement_duration = instance.measurement_duration_seconds

        self.assertEqual(actual_min_frequency, expected_min_freq)
        self.assertEqual(actual_max_frequency, expected_max_freq)
        self.assertEqual(actual_input_divisor, expected_input_divisor)
        self.assertEqual(actual_measurement_duration, expected_duration)

    def test_digital_frequency_measurement_counter_channel_parameters_with_invalid_data(
        self,
    ):
        """Tests if an instance of DigitalFrequencyMeasurementCounterChannelParameters
        throws errors when given incorrect input
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_frequency = 0.0
        max_frequency = 999999999.0
        range_parameters = daq.DigitalFrequencyRangeParameters(min_frequency, max_frequency)
        input_divisor = 10.0
        measurement_duration = 1.0

        # range_parameters is None
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementCounterChannelParameters(
                None, input_divisor, measurement_duration
            ),
        )

        # input_divisor is None
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, None, measurement_duration
            ),
        )

        # input_divisor is 0
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, 0, measurement_duration
            ),
        )

        # measurement_duration is None
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, None
            ),
        )

        # measurment_duration is 0
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, 0
            ),
        )

    def test_digital_frequency_measurement_result_data(self):
        """Tests if an instance of DigitalFrequencyMeasurementResultData
        is generated correctly when given correct data
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        expected_frequency = 10000000
        instance = daq.DigitalFrequencyMeasurementResultData(expected_frequency)
        self.assertEqual(expected_frequency, instance.frequency)

    def test_digital_frequency_measurement_result_data_with_invalid_data(self):
        """Tests if an instance of DigitalFrequencyMeasurementResultData
        throws an error when given incorrect data
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        expected_frequency = None
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementResultData(expected_frequency),
        )

        expected_frequency = -0.1
        self.assertRaises(
            ValueError,
            lambda: daq.DigitalFrequencyMeasurementResultData(expected_frequency),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_measurement.py sha256=882008ccf79e4cb691e705da226bd362bb91513dc127caac10e06d8a20b7153d bytes=2728 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_measurement.py`
- sha256: `882008ccf79e4cb691e705da226bd362bb91513dc127caac10e06d8a20b7153d`
- bytes: 2728

````python
"""This module provides DigitalFrequencyMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_data_types import (  # DigitalFrequencyMeasurementResultData,
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyRangeParameters,
)
from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_measurement import (
    DigitalFrequencyMeasurement,
)


class TestDigitalFrequencyMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'DigitalFrequencyMeasurement' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_frequency_measurement(self):
        """Checks if class 'DigitalFrequencyMeasurement' is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (263 > 100 characters) (auto-generated noqa)

        min_freq, max_freq, divisor, dur = 1.0, 1000.0, 4, 1.0
        test_params = DigitalFrequencyRangeParameters(min_freq, max_freq)
        test_ccp = DigitalFrequencyMeasurementCounterChannelParameters(test_params, divisor, dur)
        test_config = DigitalFrequencyMeasurementConfiguration(test_ccp)

        meas = DigitalFrequencyMeasurement()
        meas.initialize(
            "Sim_PXIeDAQ/ctr0",
            "/Sim_PXIeDAQ/PFI0",
        )
        meas.configure_and_measure(test_config)
        meas.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/__init__.py sha256=3814aba47c378c7a047c1334692a0c82d49764871b7fed60da9a95b6b108a6a4 bytes=279 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/__init__.py`
- sha256: `3814aba47c378c7a047c1334692a0c82d49764871b7fed60da9a95b6b108a6a4`
- bytes: 279

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.digital_pulse_generations package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (207 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_data_types.py sha256=f132e25bdabcd20e354453d0e033ea7e5d761c8e07885309f424d1270689fe2a bytes=14309 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_data_types.py`
- sha256: `f132e25bdabcd20e354453d0e033ea7e5d761c8e07885309f424d1270689fe2a`
- bytes: 14309

````python
"""This module provides Digital pulse data types check."""

import importlib.metadata  # noqa: F401 - 'importlib.metadata' imported but unused (auto-generated noqa)
import logging  # noqa: F401 - 'logging' imported but unused (auto-generated noqa)
import sys  # noqa: F401 - 'sys' imported but unused (auto-generated noqa)
import unittest

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
from varname import (  # noqa: F401 - 'varname.nameof' imported but unused (auto-generated noqa)
    nameof,
)

from nipcbatt import daq



class TestDigitalPulseGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to test the data types used in
       digital pulse generation

    Args:
        unittest.TestCase: Base class from which this class inherits
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def test_digital_pulse_counter_channel_parameters(self):
        """Tests if an instance of 'DigitalPulseGenerationCounterChannelParameters
        is created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (417 > 100 characters) (auto-generated noqa)

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = 0.5

        instance = daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)

        self.assertEqual(idle_state, instance.pulse_idle_state)
        self.assertEqual(t_low, instance.low_time_seconds)
        self.assertEqual(t_high, instance.high_time_seconds)
        self.assertIsInstance(instance, daq.DigitalPulseGenerationCounterChannelParameters)

    def test_digital_pulse_generation_counter_channel_parameters_invalid(self):
        """Ensures an instance of DigitalPulseGenerationCounterChannel parameters
        is not generated when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (423 > 100 characters) (auto-generated noqa)

        idle_state = None
        t_low = 0.5
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = None
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = -0.1
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = int(1)
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = -0.1

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = int(1)

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

    def test_digital_pulse_generation_timing_parameters(self):
        """Tests if an instance of DigitalPulseGenerationTimingParameters
        is created successfully when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        count = 10
        instance = daq.DigitalPulseGenerationTimingParameters(count)
        self.assertEqual(count, instance.pulses_count)
        self.assertIsInstance(instance, daq.DigitalPulseGenerationTimingParameters)

    def test_digital_pulse_generation_timing_parameters_invalid(self):
        """Ensures an instance of DigitalPulseGenerationTimingParameters
        is not created when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        count = None
        self.assertRaises(ValueError, lambda: daq.DigitalPulseGenerationTimingParameters(count))

        count = float(1.99)
        self.assertRaises(ValueError, lambda: daq.DigitalPulseGenerationTimingParameters(count))

        count = -1
        self.assertRaises(ValueError, lambda: daq.DigitalPulseGenerationTimingParameters(count))

    def test_digital_pulse_generation_configuration(self):
        """Ensures an instance of DigitalPulseGenerationConfiguration is
        created when given correct parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = 0.5
        count = 10
        cc_params = daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)
        t_params = daq.DigitalPulseGenerationTimingParameters(count)

        instance = daq.DigitalPulseGenerationConfiguration(cc_params, t_params)

        self.assertEqual(cc_params, instance.counter_channel_parameters)
        self.assertEqual(t_params, instance.timing_parameters)
        self.assertIsInstance(instance, daq.DigitalPulseGenerationConfiguration)

    def test_digital_pulse_generation_configuration_invalid_params(self):
        """Ensures that the creation of an instance of
        DigitalPusleGenerationConfiguration fails when given
        invalid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (393 > 100 characters) (auto-generated noqa)

        idle_state = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = 0.5
        count = 10
        cc_params = None
        t_params = daq.DigitalPulseGenerationTimingParameters(count)

        self.assertRaises(
            ValueError, lambda: daq.DigitalPulseGenerationConfiguration(cc_params, t_params)
        )

        cc_params = daq.DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)
        t_params = None

        self.assertRaises(
            ValueError, lambda: daq.DigitalPulseGenerationConfiguration(cc_params, t_params)
        )

    def test_digital_pulse_generation_data(self):
        """Tests if an instance of DigitalPulseGenerationData is correctly
        created when given correct input"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (413 > 100 characters) (auto-generated noqa)

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        instance = daq.DigitalPulseGenerationData(freq, duration, low_time, high_time)

        self.assertEqual(freq, instance.timebase_frequency_hertz)
        self.assertEqual(duration, instance.actual_pulse_train_duration_seconds)
        self.assertEqual(low_time, instance.actual_pulse_low_time_seconds)
        self.assertEqual(high_time, instance.actual_pulse_high_time_seconds)

    def test_digital_pulse_generation_data_invalid(self):
        """Ensures an instance of DigitalPulseGenerationData is not created
        when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (410 > 100 characters) (auto-generated noqa)

        freq = None
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = int(10)
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = -10.0
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = None
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = int(10)
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = -10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = None
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = int(10)
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = -10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = int(10)

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = -10.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_generation.py sha256=df0c811c41f74698d47a87123c3961504ae900f4955e0b775588868841f57260 bytes=3028 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_generation.py`
- sha256: `df0c811c41f74698d47a87123c3961504ae900f4955e0b775588868841f57260`
- bytes: 3028

````python
"""This module provides DigitalPulseGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_data_types.DigitalPulseGenerationData' imported but unused (auto-generated noqa)
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_generation import (
    DigitalPulseGeneration,
)

CHANNEL = "Sim_PXIeDAQ/ctr0"
TERMINAL = "/Sim_PXIeDAQ/PFI0"


class TestDigitalPulseGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DigitalPulseGeneration' is
       correct and readhy to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_pulse_generation(self):
        """Checks if class DigitalPulseGneration is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        t_low = 1.0
        t_high = 1.0
        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10
        cc_params = DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)
        t_params = DigitalPulseGenerationTimingParameters(p_count)
        config = DigitalPulseGenerationConfiguration(cc_params, t_params)

        gen = DigitalPulseGeneration()
        gen.initialize(CHANNEL, TERMINAL)
        gen.configure_and_generate(config)
        gen.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/__init__.py sha256=babeee4c2638eabe10c478e005a6e06c43a89cbbe38beb381d117056e7a6ed4a bytes=278 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/__init__.py`
- sha256: `babeee4c2638eabe10c478e005a6e06c43a89cbbe38beb381d117056e7a6ed4a`
- bytes: 278

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_library.digital_pwm_measurements package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_data_types.py sha256=c617d86a60e2678f1659cfeb90f1e031ae790efbaecb932a82c1edeb7ad7b735 bytes=20161 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_data_types.py`
- sha256: `c617d86a60e2678f1659cfeb90f1e031ae790efbaecb932a82c1edeb7ad7b735`
- bytes: 20161

````python
"""This module provides digital PWM data types check."""

import importlib.metadata
import logging
import sys
import unittest

import numpy as np

# import numpy as np
from varname import (  # noqa: I202 - Additional newline in a group of imports. 'from varname import nameof' is identified as Third Party and 'import numpy' is identified as Third Party. (auto-generated noqa)
    nameof,
)

from nipcbatt import daq


class TestDigitalPwmMeasurementDataTypes(unittest.TestCase):
    """Defines a test fixture to unsure the data types class used for digital PWM
       measurement are ready to use.

    Args:
        unittest.testCase: Parent class of the unittest framework"""  # noqa: D205, D209, D414, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Section has no content (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (413 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dpwmm_range_parameters(self):
        """Tests if an instance of DigitalPwmMeasurementRangeParameters is
        created when given correct values"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (337 > 100 characters) (auto-generated noqa)
        ex_min_value_seconds = 0.005
        ex_max_value_seconds = 0.5

        instance = daq.DigitalPwmMeasurementRangeParameters(ex_min_value_seconds, ex_max_value_seconds)

        self.assertIsInstance(instance, daq.DigitalPwmMeasurementRangeParameters)

        self.assertEqual(ex_min_value_seconds, instance.semi_period_minimum_value_seconds)
        self.assertEqual(ex_max_value_seconds, instance.semi_period_maximum_value_seconds)

    def test_dpwmm_range_parameters_invalid_input(self):
        """Ensures an instance of DigitalPwmMeasurementRangeParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        min_val_seconds = -0.1
        max_value_seconds = 1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        min_val_seconds = None
        max_value_seconds = 1.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        min_val_seconds = 0.05
        max_value_seconds = 0.01

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        min_val_seconds = 0.05
        max_value_seconds = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        # min_val > max_val
        min_val_seconds = 5.0
        max_value_seconds = 4.0

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

    def test_dpwmm_timing_parameters(self):
        """Tests if an instance of DigitalPwmMeasurementTimingParameters is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        cycles_count = 42
        instance = daq.DigitalPwmMeasurementTimingParameters(cycles_count)

        self.assertIsInstance(instance, daq.DigitalPwmMeasurementTimingParameters)
        self.assertEqual(cycles_count, instance.semi_period_counter_wanted_cycles_count)

    def test_dpwmm_timing_parameters_invalid_input(self):
        """Ensures an instance of DigitalPwmMeasurementTimingParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        cycles_count = -0.1
        self.assertRaises(ValueError, lambda: daq.DigitalPwmMeasurementTimingParameters(cycles_count))

        cycles_count = 2147483648
        self.assertRaises(ValueError, lambda: daq.DigitalPwmMeasurementTimingParameters(cycles_count))

        cycles_count = None
        self.assertRaises(ValueError, lambda: daq.DigitalPwmMeasurementTimingParameters(cycles_count))

    def test_dpwmm_counter_channel_parameters(self):
        """Tests if an instance of DigitalPwmMeasurementCounterChannelParameters is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        range_params = daq.DigitalPwmMeasurementRangeParameters(1.0, 10.0)
        timing = daq.DigitalPwmMeasurementTimingParameters(10.0)
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        instance = daq.DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge)

        self.assertIsInstance(instance, daq.DigitalPwmMeasurementCounterChannelParameters)
        self.assertEqual(range_params, instance.range_parameters)
        self.assertEqual(timing, instance.timing_parameters)
        self.assertEqual(edge, instance.semi_period_counter_starting_edge)

    def test_dpwmm_counter_channel_parameters_invalid_data(self):
        """Ensures an instance of DigitalPwmMeasurementCounterChannelParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        range_params = None
        timing = daq.DigitalPwmMeasurementTimingParameters(10.0)
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge),
        )

        range_params = daq.DigitalPwmMeasurementRangeParameters(1.0, 10.0)
        timing = None
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge),
        )

        range_params = daq.DigitalPwmMeasurementRangeParameters(1.0, 10.0)
        timing = daq.DigitalPwmMeasurementTimingParameters(10.0)
        edge = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge),
        )

    def test_dpwmm_data(self):
        """Tests if an instance of DigitalPwmMeasurementData is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        data = np.array([1, 2, 3, 4, 5])
        instance = daq.DigitalPwmMeasurementData(data)

        self.assertIsInstance(instance, daq.DigitalPwmMeasurementData)
        self.assertEqual(data.all(), instance.data.all())

    def test_dpwmm_data_invalid_input(self):
        """Ensures an instance of DigitalPwmMeasurementCounterChannelParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        data = None
        self.assertRaises(ValueError, lambda: daq.DigitalPwmMeasurementData(data))

        data = np.array([])
        self.assertRaises(ValueError, lambda: daq.DigitalPwmMeasurementData(data))

    def test_dpwmm_result_data(self):
        """Tests if an instance of DigitalPwmMeasurementResultData is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        instance = daq.DigitalPwmMeasurementResultData(
            actual_cycles_count,
            duty_cycle,
            period_duration,
            frequency,
            high_state_duration,
            low_state_duration,
        )

        self.assertIsInstance(instance, daq.DigitalPwmMeasurementResultData)
        self.assertEqual(actual_cycles_count, instance.actual_cycles_count)
        self.assertEqual(duty_cycle, instance.duty_cycle)
        self.assertEqual(period_duration, instance.period_duration)
        self.assertEqual(frequency, instance.frequency)
        self.assertEqual(high_state_duration, instance.high_state_duration)
        self.assertEqual(low_state_duration, instance.low_state_duration)

    def test_dpwmm_result_data_invalid_input(self):
        """Tests if an instance of DigitalPwmMeasurementResultData is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        actual_cycles_count = None
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = -1
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = None
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = -0.1
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 1.1
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = None
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = -0.1
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = None
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = -0.1
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = None
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = -0.1
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = None

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = -0.1

        self.assertRaises(
            ValueError,
            lambda: daq.DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_measurement.py sha256=d2f2ee2df4b8d22f1ba7d9e41158369a5bee813cfd1becfbbb07799df0142478 bytes=3270 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_measurement.py`
- sha256: `d2f2ee2df4b8d22f1ba7d9e41158369a5bee813cfd1becfbbb07799df0142478`
- bytes: 3270

````python
"""This module provides DigitalPwmMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_data_types.DigitalPwmMeasurementData' imported but unused (auto-generated noqa)
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_measurement import (
    DigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestDigitalPwmMeasurement(unittest.TestCase):
    """Defines a test fixutre that ensure the class 'DigitalPwmMeasurement'
       is correct and ready to use

    Args:
        unittest.TestCase: Base class of the Python unittest framework
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_pwm_measurement(self):
        """Checks if class 'DigitalPwmMeasurement' is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (257 > 100 characters) (auto-generated noqa)

        channel = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
        terminal = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        range_params = DigitalPwmMeasurementCounterChannelParameters(1.0, 10.0, 42)
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        cfg = DigitalPwmMeasurementConfiguration(range_params, edge)

        meas = DigitalPwmMeasurement()
        meas.initialize(channel_expression=channel, input_terminal_name=terminal)
        meas.configure_and_measure(cfg)
        meas.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/__init__.py sha256=fbded1f6b5e749ca29260abc36dc58b2a64790c6cb7dee9f1b737c1b0e95977f bytes=55 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/__init__.py`
- sha256: `fbded1f6b5e749ca29260abc36dc58b2a64790c6cb7dee9f1b737c1b0e95977f`
- bytes: 55

````python
"""Provides unit tests for DMM Scan functionality."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/test_dmm_scan_pmps_16V_15C.py sha256=422d6f42a96f2f4dd6086fd13f83da87904b23b3e0816fa423057055a3eb4247 bytes=13655 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/test_dmm_scan_pmps_16V_15C.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/test_dmm_scan_pmps_16V_15C.py`
- sha256: `422d6f42a96f2f4dd6086fd13f83da87904b23b3e0816fa423057055a3eb4247`
- bytes: 13655

````python
# pylint: disable=C0301
"""This module provides comprehensive unit tests for DmmScanPMPS class and data types."""

import importlib.metadata
import logging
import sys
import unittest
from typing import NamedTuple
from unittest.mock import MagicMock, patch

from varname import nameof

from nipcbatt.pcbatt_library.dmm_scan.dmm_scan_pmps_16V_15C import (
    DmmScanPMPS,
    ScanResources,
    MeasurementResult,
)


class TestScanResources(unittest.TestCase):
    """Defines a test fixture that checks `ScanResources` NamedTuple is correctly structured.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        pass

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestScanResources")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestScanResources")

    def test_scan_resources_is_named_tuple(self):
        """Unit test verifying that ScanResources is a NamedTuple."""
        self.assertTrue(issubclass(ScanResources, tuple))

    def test_scan_resources_has_required_fields(self):
        """Unit test verifying that ScanResources has all required fields."""
        expected_fields = ("mux_generation", "shunt_generation", "dmm_generation")
        self.assertEqual(ScanResources._fields, expected_fields)

    def test_scan_resources_field_access(self):
        """Unit test verifying that ScanResources fields can be accessed correctly."""
        scan_resources = ScanResources(
            mux_generation=None,
            shunt_generation=None,
            dmm_generation=None
        )

        self.assertIsNone(scan_resources.mux_generation)
        self.assertIsNone(scan_resources.shunt_generation)
        self.assertIsNone(scan_resources.dmm_generation)


class TestMeasurementResult(unittest.TestCase):
    """Defines a test fixture that checks `MeasurementResult` NamedTuple is correctly structured.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        pass

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestMeasurementResult")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestMeasurementResult")

    def test_measurement_result_is_named_tuple(self):
        """Unit test verifying that MeasurementResult is a NamedTuple."""
        self.assertTrue(issubclass(MeasurementResult, tuple))

    def test_measurement_result_has_required_fields(self):
        """Unit test verifying that MeasurementResult has all required fields."""
        expected_fields = (
            "sessions",
            "scan_time",
            "formatted_measurements",
            "execution_settings",
            "raw_measurements",
        )
        self.assertEqual(MeasurementResult._fields, expected_fields)

    def test_measurement_result_field_access(self):
        """Unit test verifying that MeasurementResult fields can be accessed correctly."""
        scan_resources = ScanResources(
            mux_generation=None,
            shunt_generation=None,
            dmm_generation=None
        )

        measurement_result = MeasurementResult(
            sessions=scan_resources,
            scan_time=0.5,
            formatted_measurements=[],
            execution_settings=[],
            raw_measurements=[]
        )

        self.assertEqual(measurement_result.sessions, scan_resources)
        self.assertEqual(measurement_result.scan_time, 0.5)
        self.assertEqual(measurement_result.formatted_measurements, [])
        self.assertEqual(measurement_result.execution_settings, [])
        self.assertEqual(measurement_result.raw_measurements, [])

    def test_measurement_result_with_sample_data(self):
        """Unit test verifying MeasurementResult with realistic sample data."""
        scan_resources = ScanResources(
            mux_generation=None,
            shunt_generation=None,
            dmm_generation=None
        )

        formatted_measurements = [
            ("ch0", "5.125V (dc)", 0.015),
            ("ch1", "10.25V (dc)", 0.018),
        ]
        execution_settings = [
            {"Function": "DC_VOLTS", "Range": 10, "Digits_Resolution": 5.5},
            {"Function": "DC_VOLTS", "Range": 10, "Digits_Resolution": 5.5},
        ]
        raw_measurements = [
            ("ch0", {"Measured_Value": 5.125, "Unit": "V (dc)"}, "DC_VOLTS"),
            ("ch1", {"Measured_Value": 10.25, "Unit": "V (dc)"}, "DC_VOLTS"),
        ]

        measurement_result = MeasurementResult(
            sessions=scan_resources,
            scan_time=0.045,
            formatted_measurements=formatted_measurements,
            execution_settings=execution_settings,
            raw_measurements=raw_measurements
        )

        self.assertEqual(len(measurement_result.formatted_measurements), 2)
        self.assertEqual(len(measurement_result.execution_settings), 2)
        self.assertEqual(len(measurement_result.raw_measurements), 2)
        self.assertEqual(measurement_result.scan_time, 0.045)


class TestDmmScanPMPSInitialization(unittest.TestCase):
    """Defines a test fixture that checks DmmScanPMPS initialization.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestDmmScanPMPSInitialization")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestDmmScanPMPSInitialization")

    def test_dmm_scan_pmps_can_be_instantiated(self):
        """Unit test verifying that DmmScanPMPS can be instantiated."""
        self.assertIsNotNone(self.dmm_scan)

    def test_dmm_scan_pmps_is_instance_of_building_blocks(self):
        """Unit test verifying that DmmScanPMPS inherits from building block classes."""
        from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
            BuildingBlockUsingNIDMM,
            BuildingBlockUsingNISWITCH,
        )
        self.assertIsInstance(self.dmm_scan, BuildingBlockUsingNIDMM)
        self.assertIsInstance(self.dmm_scan, BuildingBlockUsingNISWITCH)

    def test_dmm_scan_pmps_has_initialize_method(self):
        """Unit test verifying that DmmScanPMPS has initialize method."""
        self.assertTrue(hasattr(self.dmm_scan, "initialize"))
        self.assertTrue(callable(getattr(self.dmm_scan, "initialize")))

    def test_dmm_scan_pmps_has_configure_and_measure_method(self):
        """Unit test verifying that DmmScanPMPS has configure_and_measure method."""
        self.assertTrue(hasattr(self.dmm_scan, "configure_and_measure"))
        self.assertTrue(callable(getattr(self.dmm_scan, "configure_and_measure")))

    def test_dmm_scan_pmps_has_close_method(self):
        """Unit test verifying that DmmScanPMPS has close method."""
        self.assertTrue(hasattr(self.dmm_scan, "close"))
        self.assertTrue(callable(getattr(self.dmm_scan, "close")))


class TestDmmScanPMPSInitializeMethod(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS.initialize() method.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestDmmScanPMPSInitializeMethod")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestDmmScanPMPSInitializeMethod")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_initialize_returns_scan_resources(self, mock_dmm, mock_switch):
        """Unit test verifying that initialize() returns ScanResources."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm.return_value = mock_dmm_instance

        result = self.dmm_scan.initialize(
            mux_resource_name="Sim_MUX",
            mux_topology_name="2527/2-Wire Dual 16x1 Mux",
            shunt_resource_name="Sim_SHUNT",
            shunt_topology_name="2568/31-SPST",
            dmm_resource_name="Sim_DMM",
            powerline_freq=50,
            close_all_shunts=True
        )

        self.assertIsInstance(result, ScanResources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_initialize_with_default_parameters(self, mock_dmm, mock_switch):
        """Unit test verifying initialize() works with default parameters."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm.return_value = mock_dmm_instance

        result = self.dmm_scan.initialize()

        self.assertIsInstance(result, ScanResources)
        self.assertIsNotNone(result.mux_generation)
        self.assertIsNotNone(result.shunt_generation)
        self.assertIsNotNone(result.dmm_generation)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_initialize_with_close_all_shunts_false(self, mock_dmm, mock_switch):
        """Unit test verifying initialize() with close_all_shunts=False."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm.return_value = mock_dmm_instance

        result = self.dmm_scan.initialize(close_all_shunts=False)

        self.assertIsInstance(result, ScanResources)


class TestDmmScanPMPSCloseMethod(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS.close() method.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestDmmScanPMPSCloseMethod")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestDmmScanPMPSCloseMethod")

    def test_close_method_calls_close_on_all_resources(self):
        """Unit test verifying close() calls close on all resource handles."""
        mock_mux = MagicMock()
        mock_shunt = MagicMock()
        mock_dmm = MagicMock()

        scan_resources = ScanResources(
            mux_generation=mock_mux,
            shunt_generation=mock_shunt,
            dmm_generation=mock_dmm
        )

        self.dmm_scan.close(scan_resources)

        mock_mux.close.assert_called_once()
        mock_shunt.close.assert_called_once()
        mock_dmm.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/__init__.py sha256=0e3137193921f7679b07851e830f436c825fe90f2c0201da28e539d081c30b2f bytes=476 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/__init__.py`
- sha256: `0e3137193921f7679b07851e830f436c825fe90f2c0201da28e539d081c30b2f`
- bytes: 476

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (366 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_data_types.py sha256=ac5bdd9e2068f8d44b3a89fb31ab0e0c46572bed9b9612b0180d4d41657e096b bytes=8594 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_data_types.py`
- sha256: `ac5bdd9e2068f8d44b3a89fb31ab0e0c46572bed9b9612b0180d4d41657e096b`
- bytes: 8594

````python
"""This module provides Dynamic digital pattern data types check."""

import importlib.metadata  # noqa: F401 - 'importlib.metadata' imported but unused (auto-generated noqa)
import logging  # noqa: F401 - 'logging' imported but unused (auto-generated noqa)
import sys  # noqa: F401 - 'sys' imported but unused (auto-generated noqa)
import unittest
import numpy as np

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
from varname import (  # noqa: F401 - 'varname.nameof' imported but unused (auto-generated noqa)
    nameof,
)

from nipcbatt import daq

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)

CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/port0/line0"
CLOCK_SOURCE = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
TRIGGER_SOURCE = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestDynamicDigitalPatternGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to test the datatypes used in dynamic digital
       pulse generation

    Args:
        unittest: The unittest class from which all tests inherit
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def test_dynamic_digital_start_trigger_parameters(self):
        """Ensures a valid instance of DynamicDigitalStartTriggerParameters
        is created when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (419 > 100 characters) (auto-generated noqa)

        trig_source = TRIGGER_SOURCE
        trig_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        instance = daq.DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type)

        self.assertIsInstance(instance, daq.DynamicDigitalStartTriggerParameters)
        self.assertEqual(trig_source, instance.digital_start_trigger_source)
        self.assertEqual(trig_edge, instance.digital_start_trigger_edge)
        self.assertEqual(trig_type, instance.trigger_type)

    def test_dynamic_digital_start_trigger_parameters_invalid(self):
        """Ensures an instance of DynamicDigitalStartTriggerParameters is not
        created when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        trig_source = None
        trig_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        self.assertRaises(
            ValueError,
            lambda: daq.DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type),
        )

        trig_source = TRIGGER_SOURCE
        trig_edge = None
        trig_type = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        self.assertRaises(
            ValueError,
            lambda: daq.DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type),
        )

        trig_source = TRIGGER_SOURCE
        trig_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = None

        self.assertRaises(
            ValueError,
            lambda: daq.DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type),
        )

    def test_dynamic_digital_pattern_generation_data(self):
        """Ensures that a valid instance of DynamicDigitalPatternGenerationData
        is created when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (419 > 100 characters) (auto-generated noqa)

        gen_time = 1.0
        instance = daq.DynamicDigitalPatternGenerationData(gen_time)
        self.assertIsInstance(instance, daq.DynamicDigitalPatternGenerationData)
        self.assertEqual(gen_time, instance.generation_time_seconds)

    def test_dynamic_digital_pattern_generation_data_invalid(self):
        """Ensures that an instance of DynamicDigitalPatternGenerationData is
        not created when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        gen_time = None

        self.assertRaises(ValueError, lambda: daq.DynamicDigitalPatternGenerationData(gen_time))

        gen_time = -1.0

        self.assertRaises(ValueError, lambda: daq.DynamicDigitalPatternGenerationData(gen_time))

    def test_dynamic_digital_pattern_generation_configuration(self):
        """Ensures an instance of DynamicDigitalPatternGenerationConfiguration
        is created when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (419 > 100 characters) (auto-generated noqa)

        clock_source = CLOCK_SOURCE
        num_samples = 100
        edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        sample_rate = 10000.0
        trig_source = TRIGGER_SOURCE
        trig_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        time_parameters = DynamicDigitalPatternTimingParameters(
            clock_source,
            sample_rate,
            num_samples,
            edge,
        )

        trig_parameters = daq.DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type)
        pulse_signal_parameters = np.array([0.0, 0.0, 0.0, 100.0, 100.0, 100.0])

        instance = daq.DynamicDigitalPatternGenerationConfiguration(time_parameters, trig_parameters, pulse_signal_parameters)

        self.assertIsInstance(instance, daq.DynamicDigitalPatternGenerationConfiguration)

        self.assertEqual(clock_source, instance.timing_parameters.sample_clock_source)
        self.assertEqual(num_samples, instance.timing_parameters.number_of_samples_per_channel)
        self.assertEqual(edge, instance.timing_parameters.active_edge)
        self.assertEqual(sample_rate, instance.timing_parameters.sampling_rate_hertz)

        self.assertEqual(
            trig_source,
            instance.digital_start_trigger_parameters.digital_start_trigger_source,
        )
        self.assertEqual(
            trig_edge,
            instance.digital_start_trigger_parameters.digital_start_trigger_edge,
        )
        self.assertEqual(trig_type, instance.digital_start_trigger_parameters.trigger_type)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_generation.py sha256=3cbea154da5cb1e9a02879fea070a1af6ebee895a28805f781c84c9cef9ed409 bytes=3371 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_generation.py`
- sha256: `3cbea154da5cb1e9a02879fea070a1af6ebee895a28805f781c84c9cef9ed409`
- bytes: 3371

````python
"""This module provides DynamicDigitalPatternGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
import numpy as np
from varname import nameof

from nipcbatt import daq

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)

CHANNEL = "Sim_PXIeDAQ/port0/line0:7"
CLOCK_SOURCE = "OnboardClock"
TRIGGER_SOURCE = "/Sim_PXIeDAQ/PFI0"


class TestDynamicDigitalPatternGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DynamicDigitalPatternGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dynamic_digital_pattern_generation(self):
        """Checks if class DynamicDigitalPatternGeneration is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (265 > 100 characters) (auto-generated noqa)

        clock_source = CLOCK_SOURCE
        num_samples = 100
        edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        sample_rate = 10000.0
        trig_source = TRIGGER_SOURCE
        trig_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        time_parameters = DynamicDigitalPatternTimingParameters(
            clock_source,
            sample_rate,
            num_samples,
            edge,
        )

        trig_parameters = daq.DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type)
        pulse_signal_parameters = np.array([[0]], dtype=np.uint32)

        config = daq.DynamicDigitalPatternGenerationConfiguration(time_parameters, trig_parameters, pulse_signal_parameters)

        gen = daq.DynamicDigitalPatternGeneration()

        gen.initialize(CHANNEL)
        gen.task.stop()

        if gen.task.channel_names:
            n = len(gen.task.channel_names)
        else:
            n = 1
        pattern = np.zeros((n, 1), dtype="uint32")

        gen.configure_and_generate(config)
        gen.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/__init__.py sha256=b293bba454d768a2af4dfa85bbd90cb6b4548e56f2e7509efa610da3fcc3df63 bytes=477 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/__init__.py`
- sha256: `b293bba454d768a2af4dfa85bbd90cb6b4548e56f2e7509efa610da3fcc3df63`
- bytes: 477

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_data_types.py sha256=c66567532e0a0c2185d23bdaa5df4733d7a8cae6c9c32c5a7c7476832af3500e bytes=10929 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_data_types.py`
- sha256: `c66567532e0a0c2185d23bdaa5df4733d7a8cae6c9c32c5a7c7476832af3500e`
- bytes: 10929

````python
"""This module provides Dynamic digital pattern data types check."""

import importlib.metadata
import logging
import sys
import unittest

import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

from nipcbatt import daq
import nipcbatt


class TestDynamicDigitalPatternMeasurementDataTypes(unittest.TestCase):
    """Defines a test fixture that checks
    `DynamicDigitalPatternMeasurementDataTypes` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dynamic_digital_pattern_measurement_configuration(self):
        """Tests if the instance of `DynamicDigitalPatternMeasurementConfiguration`
        is created as expected"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        # Create test values for the Timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000.0
        expected_number_of_samples_per_channel = 1000
        expected_active_edge = daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE

        expected_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            active_edge=expected_active_edge,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = (
            daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE
        )

        expected_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for measurement options
        expected_measurement_options = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE

        instance = daq.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=expected_measurement_options,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        # Log the class name with the values of the instance created for
        # SignalVoltageGenerationSineWaveConfiguration
        logging.debug(
            "%s = %s",
            nameof(daq.DynamicDigitalPatternMeasurementConfiguration),
            instance,
        )

        self.assertEqual(
            expected_measurement_options,
            instance.measurement_options,
        )
        self.assertEqual(expected_trigger_parameters, instance.trigger_parameters)
        self.assertEqual(expected_timing_parameters, instance.timing_parameters)

    def test_dynamic_digital_pattern_measurement_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (208 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=None,
                timing_parameters=nipcbatt.DynamicDigitalPatternTimingParameters(
                    sample_clock_source=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
                    sampling_rate_hertz=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
                    number_of_samples_per_channel=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
                    active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
                ),
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                    digital_start_trigger_source=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
                    digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                timing_parameters=None,
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                    digital_start_trigger_source=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
                    digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                timing_parameters=nipcbatt.DynamicDigitalPatternTimingParameters(
                    sample_clock_source=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
                    sampling_rate_hertz=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
                    number_of_samples_per_channel=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
                    active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
                ),
                trigger_parameters=None,
            ),
        )

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DynamicDigitalPatternMeasurementResultData(
                    waveforms=None, daq_digital_waveform_from_port=[[1, 2, 3], [4, 5, 6]]
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DynamicDigitalPatternMeasurementResultData(
                    waveforms=[], daq_digital_waveform_from_port=[[1, 2, 3], [4, 5, 6]]
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_daq_digital_waveform_from_port_is_none(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DynamicDigitalPatternMeasurementResultData(
                    daq_digital_waveform_from_port=None,
                    waveforms=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
                )
            )

        # Assert
        self.assertEqual("The object daq_digital_waveform_from_port is None.", str(ctx.exception))

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_daq_digital_waveform_from_port_is_empty(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.DynamicDigitalPatternMeasurementResultData(
                    daq_digital_waveform_from_port=[], waveforms=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
                )
            )

        # Assert
        self.assertEqual(
            "The iterable daq_digital_waveform_from_port of type list is empty.", str(ctx.exception)
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_measurement.py sha256=23210bef45b85fae0772d03feb4e5740bbf02f89587977dca4b9b1cbb80871b6 bytes=3328 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_measurement.py`
- sha256: `23210bef45b85fae0772d03feb4e5740bbf02f89587977dca4b9b1cbb80871b6`
- bytes: 3328

````python
"""This module provides DynamicDigitalPatternMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
)

# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
#    _MockInterpreter,
# )
# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
#    _replace_daqmx,
# )


class TestDynamicDigitalPatternMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class'DynamicDigitalPatternMeasurement' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        # _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dynamic_digital_pattern_measurement(self):
        """Checks if class 'DynamicDigitalPatternMeasurement' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)
        meas = daq.DynamicDigitalPatternMeasurement()
        meas.initialize("Sim_PXIeDAQ/port0/line0:7")
        timing_parameters = DynamicDigitalPatternTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000.0,
            number_of_samples_per_channel=50,
            active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
        )
        trigger_parameters = DigitalStartTriggerParameters(
            trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
            digital_start_trigger_source="/Sim_PXIeDAQ/PFI0",
            digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
        )
        configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )
        meas.configure_and_measure(
            configuration=configuration,
        )
        meas.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/__init__.py sha256=2c482f7f09d3d752406815d7127305c16b39e060dcacd27c533dbeb7f4a0e79d bytes=470 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/__init__.py`
- sha256: `2c482f7f09d3d752406815d7127305c16b39e060dcacd27c533dbeb7f4a0e79d`
- bytes: 470

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.frequency_domain_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (360 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_data_types.py sha256=f001a2c0b63bb636933273ad139dbe1f638f4778f3436380427de743d6062da3 bytes=41267 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_data_types.py`
- sha256: `f001a2c0b63bb636933273ad139dbe1f638f4778f3436380427de743d6062da3`
- bytes: 41267

````python
"""This module provides Frequency domain data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt import daq

class TestFrequencyDomainMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TimeDomainMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_frequency_domain_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_measurement_options_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=None,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration(self):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expected_specific_range_min_volts = -5.0
        expected_specific_range_max_volts = 7.5

        expected_global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        specific_channels_parameters = []
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai0",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai1",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai2",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )

        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        logging.debug(
            "%s = %s",
            nameof(specific_channels_parameters),
            specific_channels_parameters,
        )

        # Act
        measurement_configuration_instance = daq.FrequencyDomainMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=specific_channels_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(measurement_configuration_instance),
            measurement_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            specific_channels_parameters,
            measurement_configuration_instance.specific_channels_parameters,
        )

        actual_global_channel_parameters = (
            measurement_configuration_instance.global_channel_parameters
        )

        actual_measurement_options = measurement_configuration_instance.measurement_options
        actual_sample_clock_timing_parameters = (
            measurement_configuration_instance.sample_clock_timing_parameters
        )

        self.assertEqual(expected_global_channel_parameters, actual_global_channel_parameters)

        self.assertEqual(expected_measurement_options, actual_measurement_options)

        self.assertEqual(
            expected_sample_clock_timing_parameters,
            actual_sample_clock_timing_parameters,
        )


class TestMultipleTonesMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `MultipleTonesMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        methodName: str = "runTest",  # noqa: N803 - argument name 'methodName' should be lowercase (auto-generated noqa)
    ) -> None:
        super().__init__(methodName)
        self._expected_waveforms = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_multiple_tones_measurement_result_data_for_value_error(self):
        """Tests if expected ValueError in thrown when inputs are None"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (261 > 100 characters) (auto-generated noqa)

        # Test for tones_amplitudes_volts set to None
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=None,
                    tones_frequencies_hertz=[1000],
                )
            )

        self.assertEqual("The object tones_amplitudes_volts is None.", str(ctx.exception))

        # Test for tones_frequencies_hertz set to None
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0],
                    tones_frequencies_hertz=None,
                )
            )

        self.assertEqual("The object tones_frequencies_hertz is None.", str(ctx.exception))

    def test_multiple_tones_measurement_result_data_for_type_error(self):
        """Tests if expected TypeError in thrown when inputs are None"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (260 > 100 characters) (auto-generated noqa)

        # Test for tones_amplitudes_volts with values that are not float
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0, "1.5", 2.0],
                    tones_frequencies_hertz=[100, 1000, 250],
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (float).", str(ctx.exception)
        )

        # Test for tones_frequencies_hertz with values that are not float
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0, 1.5, 2.0],
                    tones_frequencies_hertz=[100, 1000, True],
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (float).", str(ctx.exception)
        )

    def test_multiple_tones_measurement_result_data_with_input_lists_of_different_lengths(
        self,
    ):
        """Tests if expected ValueError in thrown when the two input lists have different length."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)

        # Test for tones_amplitudes_volts and tones_frequencies_hertz lists
        # with different number of element
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0, 2.0, 3.0],
                    tones_frequencies_hertz=[100.0, 200.0],
                )
            )

        self.assertEqual(
            "The iterables (tones_amplitudes_volts and tones_frequencies_hertz)"
            + " do not have same size.",
            str(ctx.exception),
        )

    def test_multiple_tones_measurement_result_data(self):
        """Test for proper functioning of TestMultipleTonesMeasurementResultData"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)
        expected_tones_amplitude = [1.2, 1.6, 1.8, 1.0]
        expected_tones_frequencies = [100.05, 200.0, 500.0, 1000.1]

        instance = daq.MultipleTonesMeasurementResultData(
            tones_frequencies_hertz=expected_tones_frequencies,
            tones_amplitudes_volts=expected_tones_amplitude,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_tones_amplitude = instance.tones_amplitudes_volts
        actual_tones_frequencies = instance.tones_frequencies_hertz

        self.assertListEqual(expected_tones_amplitude, actual_tones_amplitude)
        self.assertListEqual(expected_tones_frequencies, actual_tones_frequencies)


class TestFrequencyDomainMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `FrequencyDomainMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        methodName: str = "runTest",  # noqa: N803 - argument name 'methodName' should be lowercase (auto-generated noqa)
    ) -> None:
        super().__init__(methodName)
        self._expected_waveforms = None

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def setUp(self):
        """Creates some common test data to be used in different test methods."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)

        # Create test data for waveforms.
        self._expected_waveforms = []
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )

        array_count1 = 1500
        array_count2 = 2000

        # Create test data for magnitude peak.
        self._expected_magnitude_peak = []

        samples_array1 = list(4.95 + random.random() * 0.1 for i in range(0, array_count1))
        samples_numpy_array1 = numpy.array(samples_array1, dtype=numpy.float64)

        self._expected_magnitude_peak.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel1",
                spectrum_start_frequency_hertz=13500,
                spectrum_frequency_resolution_hertz=1.0,
                amplitudes=samples_numpy_array1,
            )
        )

        samples_array2 = list(5.08 + random.random() * 0.1 for i in range(0, array_count2))
        samples_numpy_array2 = numpy.array(samples_array2, dtype=numpy.float64)

        self._expected_magnitude_peak.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel2",
                spectrum_start_frequency_hertz=20000,
                spectrum_frequency_resolution_hertz=10.0,
                amplitudes=samples_numpy_array2,
            )
        )

        # Create test data for magnitude rms.
        self._expected_magnitude_rms = []
        samples_array3 = list(2.95 + random.random() * 0.1 for i in range(0, array_count1))
        samples_numpy_array3 = numpy.array(samples_array3, dtype=numpy.float64)

        self._expected_magnitude_rms.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel1",
                spectrum_start_frequency_hertz=25431,
                spectrum_frequency_resolution_hertz=5.0,
                amplitudes=samples_numpy_array3,
            )
        )

        samples_array4 = list(3.08 + random.random() * 0.1 for i in range(0, array_count2))
        samples_numpy_array4 = numpy.array(samples_array4, dtype=numpy.float64)

        self._expected_magnitude_rms.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel2",
                spectrum_start_frequency_hertz=15684,
                spectrum_frequency_resolution_hertz=11.0,
                amplitudes=samples_numpy_array4,
            )
        )

        # Create test data for detected tones.
        self._expected_detected_tones = []
        self._expected_detected_tones.append(
            daq.MultipleTonesMeasurementResultData(
                tones_frequencies_hertz=[100.05, 200.0, 500.0, 1000.1],
                tones_amplitudes_volts=[1.2, 1.6, 1.8, 1.0],
            )
        )
        self._expected_detected_tones.append(
            daq.MultipleTonesMeasurementResultData(
                tones_frequencies_hertz=[1000.5, 2000.15, 1500.0, 10000.89, 200000.0],
                tones_amplitudes_volts=[1.02, 2.76, 3.2, 5.15, 4.87],
            )
        )

    def tearDown(self):
        pass

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_waveforms(
        self,
    ):
        """Unit test to check if `FrequencyDomainMeasurementResultData` throws Value Error
        for invalid values for `waveforms` input."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        # Test if expected error is thrown if waveforms is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=None,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The object waveforms is None.", str(ctx.exception))

        # Test if expected error is thrown if waveforms is set to an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=[],
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if magnitude_rms contains elements
        # that are not of type AnalogWaveform.
        self._expected_waveforms.append(5.67)
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_detected_tones(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `detected_tones`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Test if expected error is thrown if detected_tones is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_peak,
                    detected_tones=None,
                )
            )

        self.assertEqual("The object detected_tones is None.", str(ctx.exception))

        # Test if expected Value error is thrown if magnitude_peak is an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=[],
                )
            )

        self.assertEqual("The iterable detected_tones of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if detected_tones contains elements
        # that are not of type MultipleTonesMeasurementResultData.
        self._expected_detected_tones.append([5.67])

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (MultipleTonesMeasurementResultData).",
            str(ctx.exception),
        )    

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_magnitude_rms(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `magnitude_rms`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Test if expected error is thrown if magnitude_rms is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=None,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The object magnitude_rms is None.", str(ctx.exception))

        # Test if expected Value error is thrown if magnitude_rms is an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=[],
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The iterable magnitude_rms of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if magnitude_rms contains elements
        # that are not of type AmplitudeSpectrum.

        self._expected_magnitude_rms.append(5.67)

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (AmplitudeSpectrum).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_magnitude_peak(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `magnitude_peak`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Test if expected error is thrown if magnitude_peak is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=None,
                    magnitude_rms=self._expected_magnitude_peak,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The object magnitude_peak is None.", str(ctx.exception))

        # Test if expected Value error is thrown if magnitude_peak is an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=[],
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The iterable magnitude_peak of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if magnitude_peak contains elements
        # that are not of type AmplitudeSpectrum.
        self._expected_magnitude_peak.append(5.67)

        with self.assertRaises(TypeError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (AmplitudeSpectrum).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_with_waveforms_and_magnitude_rms_are_of_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `magnitude_rms`
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        samples_array = list(3.08 + random.random() * 0.1 for i in range(0, 200))
        samples_numpy_array = numpy.array(samples_array, dtype=numpy.float64)

        self._expected_magnitude_rms.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel3",
                spectrum_start_frequency_hertz=15684,
                spectrum_frequency_resolution_hertz=11.0,
                amplitudes=samples_numpy_array,
            )
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and magnitude_rms) do not have same size.",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_with_waveforms_and_magnitude_peak_are_of_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating instance
        of `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `magnitude_peak`
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        samples_array = list(3.08 + random.random() * 0.1 for i in range(0, 200))
        samples_numpy_array = numpy.array(samples_array, dtype=numpy.float64)

        self._expected_magnitude_peak.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel3",
                spectrum_start_frequency_hertz=15684,
                spectrum_frequency_resolution_hertz=11.0,
                amplitudes=samples_numpy_array,
            )
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and magnitude_peak) do not have same size.",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_with_waveforms_and_detected_tones_are_of_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `detected_tones`
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        self._expected_detected_tones.append(
            daq.MultipleTonesMeasurementResultData(
                tones_amplitudes_volts=[1.0, 2.0],
                tones_frequencies_hertz=[100.12, 1000.00],
            )
        )

        print(len(self._expected_waveforms))
        print(len(self._expected_detected_tones))

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and detected_tones) do not have same size.",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data(self):
        """Test for proper functioning of `FrequencyDomainMeasurementResultData` class"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (277 > 100 characters) (auto-generated noqa)

        fdvm_result_data_instance = daq.FrequencyDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            magnitude_peak=self._expected_magnitude_peak,
            magnitude_rms=self._expected_magnitude_rms,
            detected_tones=self._expected_detected_tones,
        )

        actual_waveforms = fdvm_result_data_instance.waveforms
        actual_magnitude_peak = fdvm_result_data_instance.magnitude_peak
        actual_magnitude_rms = fdvm_result_data_instance.magnitude_rms
        actual_detected_tones = fdvm_result_data_instance.detected_tones

        logging.debug("%s = %s", nameof(fdvm_result_data_instance), fdvm_result_data_instance)

        self.assertListEqual(self._expected_waveforms, actual_waveforms)
        self.assertListEqual(self._expected_magnitude_peak, actual_magnitude_peak)
        self.assertListEqual(self._expected_magnitude_rms, actual_magnitude_rms)
        self.assertListEqual(self._expected_detected_tones, actual_detected_tones)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_measurement.py sha256=ba6f2510a05ab8834e68d1e91a56a820d0bae7ab1712b5f74f1aa619b4f82a8c bytes=2424 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_measurement.py`
- sha256: `ba6f2510a05ab8834e68d1e91a56a820d0bae7ab1712b5f74f1aa619b4f82a8c`
- bytes: 2424

````python
"""This module provides FrequencyDomainMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestFrequencyDomainMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `FrequencyDomainMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_frequency_domain_measurement(self):
        """Checks if class FrequencyDomainMeasurement is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)
        with nipcbatt.daq.FrequencyDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0"
                )
            )

            measurement.configure_and_measure(
                configuration=nipcbatt.daq.DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION
            )
            measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/__init__.py sha256=dc6e424fdafebf2da269b81f0d880d24c74d2aaa319b67c7e7c7903b48e2b0a4 bytes=459 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/__init__.py`
- sha256: `dc6e424fdafebf2da269b81f0d880d24c74d2aaa319b67c7e7c7903b48e2b0a4`
- bytes: 459

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.i2c_communications package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_data_types.py sha256=615f35fd90235e051234e56f1692c5719b77b598fcfc31e006be0a7a4f690c0b bytes=10775 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_data_types.py`
- sha256: `615f35fd90235e051234e56f1692c5719b77b598fcfc31e006be0a7a4f690c0b`
- bytes: 10775

````python
"""This module provides I2C data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import communications

class TestI2cDeviceParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cDeviceParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_device_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cDeviceParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_enable_i2c_pullup_resistor = False
        expected_voltage_level = nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_25

        instance = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=expected_enable_i2c_pullup_resistor,
            voltage_level=expected_voltage_level,
        )

        actual_enable_i2c_pullup_resistor = instance.enable_i2c_pullup_resistor
        actual_voltage_level = instance.voltage_level
        self.assertEqual(expected_enable_i2c_pullup_resistor, actual_enable_i2c_pullup_resistor)
        self.assertEqual(
            expected_voltage_level,
            actual_voltage_level,
        )


class TestI2cCommunicationParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cCommunicationParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_communication_parameters_init_fails_when_device_address_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = -50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 100
        expected_ack_poll_timeout_milliseconds = 1000

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value device_address must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters_init_fails_when_ack_poll_timeout_milliseconds_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 100
        expected_ack_poll_timeout_milliseconds = -1000

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value ack_poll_timeout_milliseconds must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters_init_fails_when_clock_rate_kilohertz_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 0
        expected_ack_poll_timeout_milliseconds = 1000

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters_init_fails_when_clock_rate_kilohertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = -100
        expected_ack_poll_timeout_milliseconds = 1000

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 100
        expected_ack_poll_timeout_milliseconds = 1000

        instance = communications.I2cCommunicationParameters(
            device_address=expected_device_address,
            addressing_type=expected_addressing_type,
            clock_rate_kilohertz=expected_clock_rate_kilohertz,
            ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
        )

        actual_device_address = instance.device_address
        actual_addressing_type = instance.addressing_type
        actual_clock_rate_kilohertz = instance.clock_rate_kilohertz
        actual_ack_poll_timeout_milliseconds = instance.ack_poll_timeout_milliseconds
        self.assertEqual(expected_device_address, actual_device_address)
        self.assertEqual(
            expected_addressing_type,
            actual_addressing_type,
        )
        self.assertEqual(
            expected_clock_rate_kilohertz,
            actual_clock_rate_kilohertz,
        )
        self.assertEqual(
            expected_ack_poll_timeout_milliseconds,
            actual_ack_poll_timeout_milliseconds,
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_communication.py sha256=ccf649bfb202616f3bf4810e0de7ff21c9ad56ace76364c3d5fc2f7ea87dd102 bytes=2464 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_communication.py`
- sha256: `ccf649bfb202616f3bf4810e0de7ff21c9ad56ace76364c3d5fc2f7ea87dd102`
- bytes: 2464

````python
"""This module provides I2CReadCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import communications
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions



class TestI2cReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the `I2cReadCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_i2c_read_communication(self):
        """Unit test of
        communications.pcbatt_library.i2c_communications.i2c_read_communication.I2cReadCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.I2cReadCommunication() as communication:
            communication.initialize("USB-8452")

            configuration = communications.DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=communication)
            print(f"results = {results}")
            self.assertIsNotNone(None, results)
            self.assertIsInstance(results, communications.I2cReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_data_types.py sha256=f44c90c3894191e2fc36ca9af5358fb57dfb1ee768219106b4abd9aadfa0f7f6 bytes=18849 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_data_types.py`
- sha256: `f44c90c3894191e2fc36ca9af5358fb57dfb1ee768219106b4abd9aadfa0f7f6`
- bytes: 18849

````python
"""This module provides I2C read communication data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt import communications


class TestI2cReadParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cReadParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_read_parameters_init_fails_when_memory_address_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = 7

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=None,
                )
            )

        self.assertEqual(
            "The object memory_address_parameters is None.",
            str(ctx.exception),
        )

    def test_i2c_read_parameters_init_fails_when_number_of_bytes_to_read_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = 0
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=expected_memory_address_parameters,
                )
            )

        self.assertEqual(
            "The value number_of_bytes_to_read must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_read_parameters_init_fails_when_number_of_bytes_to_read_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = -7
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=expected_memory_address_parameters,
                )
            )

        self.assertEqual(
            "The value number_of_bytes_to_read must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_read_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = 7
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        instance = communications.I2cReadParameters(
            number_of_bytes_to_read=expected_number_of_bytes_to_read,
            memory_address_parameters=expected_memory_address_parameters,
        )

        actual_number_of_bytes_to_read = instance.number_of_bytes_to_read
        actual_memory_address_parameters = instance.memory_address_parameters

        self.assertEqual(expected_number_of_bytes_to_read, actual_number_of_bytes_to_read)
        self.assertEqual(
            expected_memory_address_parameters,
            actual_memory_address_parameters,
        )


class TestI2cReadCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cReadCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_read_communication_configuration_init_fails_when_device_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_communication_parameters = communications.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )
        expected_communication_read_parameters = communications.I2cReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadCommunicationConfiguration(
                    device_parameters=None,
                    communication_parameters=expected_communication_parameters,
                    read_parameters=expected_communication_read_parameters,
                )
            )

        # Assert
        self.assertEqual("The object device_parameters is None.", str(ctx.exception))

    def test_i2c_read_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_device_parameters = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_read_parameters = communications.I2cReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadCommunicationConfiguration(
                    device_parameters=expected_device_parameters,
                    communication_parameters=None,
                    read_parameters=expected_communication_read_parameters,
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_i2c_read_communication_configuration_init_fails_when_read_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_device_parameters = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_parameters = communications.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadCommunicationConfiguration(
                    device_parameters=expected_device_parameters,
                    communication_parameters=expected_communication_parameters,
                    read_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object read_parameters is None.", str(ctx.exception))

    def test_i2c_read_communication_configuration(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_parameters = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_parameters = communications.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )
        expected_communication_read_parameters = communications.I2cReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        instance = communications.I2cReadCommunicationConfiguration(
            device_parameters=expected_device_parameters,
            communication_parameters=expected_communication_parameters,
            read_parameters=expected_communication_read_parameters,
        )

        actual_device_parameters = instance.device_parameters
        actual_communication_parameters = instance.communication_parameters
        actual_communication_read_parameters = instance.read_parameters

        self.assertEqual(expected_device_parameters, actual_device_parameters)
        self.assertEqual(
            expected_communication_parameters,
            actual_communication_parameters,
        )
        self.assertEqual(
            expected_communication_read_parameters, actual_communication_read_parameters
        )


class TestI2cReadCommunicationData(unittest.TestCase):
    """Defines a test fixture that checks
    `TestI2cReadCommunicationData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_read_communication_data_init_fails_when_data_bytes_read_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadCommunicationData(
                    data_bytes_read=None,
                )
            )

        self.assertEqual(
            "The object data_bytes_read is None.",
            str(ctx.exception),
        )

    def test_i2c_read_communication_data_init_fails_when_data_bytes_read_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationData.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cReadCommunicationData(
                    data_bytes_read=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable data_bytes_read of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_i2c_read_communication_data(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_data_bytes_read_count = 30
        expected_data_bytes_read_list = list(
            random.randint(0, 255) for i in range(0, expected_data_bytes_read_count)
        )
        expected_data_bytes_read = numpy.array(expected_data_bytes_read_list, dtype=numpy.ubyte)

        instance = communications.I2cReadCommunicationData(data_bytes_read=expected_data_bytes_read)

        actual_data_bytes_read = instance.data_bytes_read

        self.assertTrue(numpy.array_equal(a1=expected_data_bytes_read, a2=actual_data_bytes_read))


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_communication.py sha256=132dda64efb2a4ce5904d49557596f6a8d438300417bf9553dc6060e339782fa bytes=2229 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_communication.py`
- sha256: `132dda64efb2a4ce5904d49557596f6a8d438300417bf9553dc6060e339782fa`
- bytes: 2229

````python
"""This module provides I2CWriteCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestI2cWriteCommunication(unittest.TestCase):
    """Defines a test fixture that checks the `I2cWriteCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_i2c_write_communication(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_communication.I2cWriteCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with nipcbatt.I2cWriteCommunication() as communication:
            communication.initialize("USB-8452")

            configuration = nipcbatt.DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION

            print(f"parameters = {configuration}")
            communication.configure_and_write_data(configuration=configuration)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_data_types.py sha256=678d4dd934da0946f36641c61993467901f7a673a2d4451938cb46dd6f20a323 bytes=21320 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_data_types.py`
- sha256: `678d4dd934da0946f36641c61993467901f7a673a2d4451938cb46dd6f20a323`
- bytes: 21320

````python
"""This module provides I2C write communication data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt import communications


class TestI2cWriteParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cWriteParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_write_parameters_init_fails_when_memory_address_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.zeros(shape=10),
                    memory_address_parameters=None,
                )
            )

        self.assertEqual(
            "The object memory_address_parameters is None.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_data_to_be_written_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=None,
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The object data_to_be_written is None.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_data_to_be_written_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The iterable data_to_be_written of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_number_of_bytes_per_page_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteParameters(
                    number_of_bytes_per_page=-128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value number_of_bytes_per_page must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_number_of_bytes_per_page_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteParameters(
                    number_of_bytes_per_page=0,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value number_of_bytes_per_page must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_delay_between_page_write_operations_milliseconds_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=-10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value delay_between_page_write_operations_milliseconds must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_per_page = 128
        expected_delay_between_page_write_operations_milliseconds = 10
        expected_data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        expected_data_to_be_written = numpy.array(
            expected_data_to_be_written_list, dtype=numpy.ubyte
        )
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        instance = communications.I2cWriteParameters(
            number_of_bytes_per_page=expected_number_of_bytes_per_page,
            delay_between_page_write_operations_milliseconds=(
                expected_delay_between_page_write_operations_milliseconds
            ),
            data_to_be_written=expected_data_to_be_written,
            memory_address_parameters=expected_memory_address_parameters,
        )

        actual_number_of_bytes_per_page = instance.number_of_bytes_per_page
        actual_delay_between_page_write_operations_milliseconds = (
            instance.delay_between_page_write_operations_milliseconds
        )
        actual_data_to_be_written = instance.data_to_be_written
        actual_memory_address_parameters = instance.memory_address_parameters

        self.assertEqual(expected_number_of_bytes_per_page, actual_number_of_bytes_per_page)
        self.assertEqual(
            expected_delay_between_page_write_operations_milliseconds,
            actual_delay_between_page_write_operations_milliseconds,
        )
        self.assertTrue(
            numpy.array_equal(a1=expected_data_to_be_written, a2=actual_data_to_be_written)
        )
        self.assertEqual(
            expected_memory_address_parameters,
            actual_memory_address_parameters,
        )


class TestI2cWriteCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cWriteCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_i2c_write_communication_configuration_init_fails_when_device_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        communication_parameters = communications.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        communication_write_parameters = communications.I2cWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteCommunicationConfiguration(
                    device_parameters=None,
                    communication_parameters=communication_parameters,
                    write_parameters=communication_write_parameters,
                )
            )

        # Assert
        self.assertEqual("The object device_parameters is None.", str(ctx.exception))

    def test_i2c_write_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        device_parameters = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        communication_write_parameters = communications.I2cWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteCommunicationConfiguration(
                    device_parameters=device_parameters,
                    communication_parameters=None,
                    write_parameters=communication_write_parameters,
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_i2c_write_communication_configuration_init_fails_when_write_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        device_parameters = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        communication_parameters = communications.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.I2cWriteCommunicationConfiguration(
                    device_parameters=device_parameters,
                    communication_parameters=communication_parameters,
                    write_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object write_parameters is None.", str(ctx.exception))

    def test_i2c_write_communication_configuration(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        expected_device_parameters = communications.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        expected_communication_parameters = communications.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        expected_communication_write_parameters = communications.I2cWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        instance = communications.I2cWriteCommunicationConfiguration(
            device_parameters=expected_device_parameters,
            communication_parameters=expected_communication_parameters,
            write_parameters=expected_communication_write_parameters,
        )

        # Assert
        actual_device_parameters = instance.device_parameters
        actual_communication_parameters = instance.communication_parameters
        actual_communication_write_parameters = instance.write_parameters

        self.assertEqual(expected_device_parameters, actual_device_parameters)
        self.assertEqual(
            expected_communication_parameters,
            actual_communication_parameters,
        )
        self.assertEqual(
            expected_communication_write_parameters,
            actual_communication_write_parameters,
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/__init__.py sha256=0fda2ff2a72299672534e1751f05be5f677625cc5e2ee182fc5281e491dc522a bytes=73 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/__init__.py`
- sha256: `0fda2ff2a72299672534e1751f05be5f677625cc5e2ee182fc5281e491dc522a`
- bytes: 73

````python
"""Provides Unit tests for mixed measurements in the pcbatt_library."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/test_mixed_measurement.py sha256=59c6048ade12cd1584ec4f5940bab0fc8104662dc94e010b0ac873bfbcfa58a2 bytes=2132 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/test_mixed_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/test_mixed_measurement.py`
- sha256: `59c6048ade12cd1584ec4f5940bab0fc8104662dc94e010b0ac873bfbcfa58a2`
- bytes: 2132

````python
# pylint: disable=C0301
"""This module provides MixedMeasurement check."""

import importlib.metadata
import logging
from pathlib import Path
import sys
import unittest

# Force using local source tree instead of installed package in venv.
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))

import nipcbatt
from nipcbatt import dmm


class TestMixedMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `MixedMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("used_nidaqmx_version = %s", used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_mixed_measurement(self):
        """Checks if class MixedMeasurement is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        measurement = dmm.MixedMeasurement()
        try:
            measurement.initialize(dmm_resource_name="Sim_DMM", powerline_frequency=50)

            measurement.configure_and_measure(
                configuration=dmm.DEFAULT_MIXED_MEASUREMENT_CONFIGURATION
            )
        finally:
            measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/__init__.py sha256=4fd03871a36d0173e244a68d0649331b1ce9166f398645c4ba0eaa3332c5feff bytes=84 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/__init__.py`
- sha256: `4fd03871a36d0173e244a68d0649331b1ce9166f398645c4ba0eaa3332c5feff`
- bytes: 84

````python
"""Provides Unit tests for dc cc source and measurements in the pcbatt_library."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/test_dc_cc_source_and_measure.py sha256=d3ed0bc22fd4d73b7d464d7852ecafecd248e069d78eacaba5ef47f94713e2d5 bytes=32240 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/test_dc_cc_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/test_dc_cc_source_and_measure.py`
- sha256: `d3ed0bc22fd4d73b7d464d7852ecafecd248e069d78eacaba5ef47f94713e2d5`
- bytes: 32240

````python
# pylint: disable=C0301
"""This module provides DC constant current source and measure data types unit tests."""

import importlib.metadata
import logging
import math
import sys
import unittest

import nidcpower
from varname import nameof

from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_data_types import (
    CurrentChannelSettings,
    DCCurrentSourceAndMeasureParameters,
    DCCurrentSourceAndMeasureResultData,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_constants import (
    ConstantsForDCCurrentSourceAndMeasure,
    DEFAULT_DC_CC_CHANNEL_SETTINGS,
    DEFAULT_DC_CC_EXECUTION_SETTINGS,
    DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_DC_CC_TIMING_PARAMETERS,
    DEFAULT_DC_CC_TRIGGER_PARAMETERS,
)


class TestMeasurementExecutionType(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementExecutionType` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_measurement_execution_type_members(self):
        """Checks MeasurementExecutionType enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE.value,
            "CONFIGURE_SOURCE_AND_MEASURE",
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_ONLY.value,
            "CONFIGURE_ONLY",
        )
        self.assertEqual(
            MeasurementExecutionType.START_SOURCE_ONLY.value,
            "START_SOURCE_ONLY",
        )
        self.assertEqual(
            MeasurementExecutionType.MEASURE_ONLY.value,
            "MEASURE_ONLY",
        )
        self.assertEqual(len(MeasurementExecutionType), 4)


class TestSourceTriggerBehavior(unittest.TestCase):
    """Defines a test fixture that checks
    `SourceTriggerBehavior` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_source_trigger_behavior_members(self):
        """Checks SourceTriggerBehavior enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            SourceTriggerBehavior.Start_Source_Trigger.value,
            "Start_Source_Trigger",
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger.value,
            "Disable_Source_Trigger",
        )
        self.assertEqual(len(SourceTriggerBehavior), 2)


class TestExportEvent(unittest.TestCase):
    """Defines a test fixture that checks
    `ExportEvent` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_export_event_members(self):
        """Checks ExportEvent enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(ExportEvent.NONE.value, "NONE")
        self.assertEqual(ExportEvent.Route_Event.value, "Route_Event")
        self.assertEqual(len(ExportEvent), 2)


class TestEventSignalToExport(unittest.TestCase):
    """Defines a test fixture that checks
    `EventSignalToExport` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_event_signal_to_export_members(self):
        """Checks EventSignalToExport enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event.value,
            "source_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Measure_Complete_Event.value,
            "measure_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Iteration_Complete_Event.value,
            "sequence_iteration_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Engine_Done_Event.value,
            "sequence_engine_done_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Pulse_Complete_Event.value,
            "pulse_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Ready_for_Pulse_Trigger_Event.value,
            "ready_for_pulse_trigger_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Start_Trigger.value,
            "exported_start_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Source_Trigger.value,
            "exported_source_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Measure_Trigger.value,
            "exported_measure_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Advance_Trigger.value,
            "exported_sequence_advance_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Pulse_Trigger.value,
            "exported_pulse_trigger_output_terminal",
        )
        self.assertEqual(len(EventSignalToExport), 11)


class TestExecutionSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `ExecutionSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_execution_settings(self):
        """Checks ExecutionSettings construction and property getters."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
        expected_skip_analysis = True

        instance = ExecutionSettings(
            execution_type=expected_execution_type,
            skip_analysis=expected_skip_analysis,
        )

        self.assertEqual(expected_execution_type, instance.execution_type)
        self.assertEqual(expected_skip_analysis, instance.skip_analysis)

    def test_execution_settings_configure_only(self):
        """Checks ExecutionSettings with CONFIGURE_ONLY execution type."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_ONLY
        expected_skip_analysis = False

        instance = ExecutionSettings(
            execution_type=expected_execution_type,
            skip_analysis=expected_skip_analysis,
        )

        self.assertEqual(expected_execution_type, instance.execution_type)
        self.assertEqual(expected_skip_analysis, instance.skip_analysis)


class TestCurrentChannelSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `CurrentChannelSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_current_channel_settings_remote_sensing(self):
        """Checks CurrentChannelSettings construction and property getters with REMOTE sensing."""  # noqa: D415, W505
        expected_current_level = 10e-6
        expected_current_level_range = 0.1
        expected_voltage_limit = 1.0
        expected_voltage_limit_range = 2.0
        expected_sensing = nidcpower.Sense.REMOTE
        expected_enable_output = True

        instance = CurrentChannelSettings(
            current_level=expected_current_level,
            current_level_range=expected_current_level_range,
            voltage_limit=expected_voltage_limit,
            voltage_limit_range=expected_voltage_limit_range,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
        )

        self.assertEqual(expected_current_level, instance.current_level)
        self.assertEqual(expected_current_level_range, instance.current_level_range)
        self.assertEqual(expected_voltage_limit, instance.voltage_limit)
        self.assertEqual(expected_voltage_limit_range, instance.voltage_limit_range)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)

    def test_current_channel_settings_local_sensing_output_disabled(self):
        """Checks CurrentChannelSettings with LOCAL sensing and output disabled."""  # noqa: D415, W505
        expected_current_level = 50e-3
        expected_current_level_range = 0.2
        expected_voltage_limit = 5.0
        expected_voltage_limit_range = 6.0
        expected_sensing = nidcpower.Sense.LOCAL
        expected_enable_output = False

        instance = CurrentChannelSettings(
            current_level=expected_current_level,
            current_level_range=expected_current_level_range,
            voltage_limit=expected_voltage_limit,
            voltage_limit_range=expected_voltage_limit_range,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
        )

        self.assertEqual(expected_current_level, instance.current_level)
        self.assertEqual(expected_current_level_range, instance.current_level_range)
        self.assertEqual(expected_voltage_limit, instance.voltage_limit)
        self.assertEqual(expected_voltage_limit_range, instance.voltage_limit_range)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)


class TestTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_timing_parameters(self):
        """Checks TimingParameters construction and property getters."""  # noqa: D415, W505
        expected_source_delay = 0.1
        expected_aperture_time = 0.02
        expected_transient_response = nidcpower.TransientResponse.NORMAL

        instance = TimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)

    def test_timing_parameters_fast_transient(self):
        """Checks TimingParameters with FAST transient response."""  # noqa: D415, W505
        expected_source_delay = 0.05
        expected_aperture_time = 0.01
        expected_transient_response = nidcpower.TransientResponse.FAST

        instance = TimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)


class TestTriggerParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_trigger_parameters_with_trigger_enabled(self):
        """Checks TriggerParameters with source trigger enabled and event routing."""  # noqa: D415, W505
        expected_source_trigger_behavior = SourceTriggerBehavior.Start_Source_Trigger
        expected_start_source_name = "/PXI1Slot2/PXI_Trig0"
        expected_export_event = ExportEvent.Route_Event
        expected_event_signal_to_export = EventSignalToExport.Source_Complete_Event
        expected_output_event_signal_terminal = "/PXI1Slot2/PXI_Trig1"

        instance = TriggerParameters(
            source_trigger_behavior=expected_source_trigger_behavior,
            start_source_name=expected_start_source_name,
            export_event=expected_export_event,
            event_signal_to_export=expected_event_signal_to_export,
            output_event_signal_terminal=expected_output_event_signal_terminal,
        )

        self.assertEqual(expected_source_trigger_behavior, instance.source_trigger_behavior)
        self.assertEqual(expected_start_source_name, instance.start_source_name)
        self.assertEqual(expected_export_event, instance.export_event)
        self.assertEqual(expected_event_signal_to_export, instance.event_signal_to_export)
        self.assertEqual(expected_output_event_signal_terminal, instance.output_event_signal_terminal)

    def test_trigger_parameters_with_trigger_disabled(self):
        """Checks TriggerParameters with source trigger disabled and no event routing."""  # noqa: D415, W505
        expected_source_trigger_behavior = SourceTriggerBehavior.Disable_Source_Trigger
        expected_start_source_name = ""
        expected_export_event = ExportEvent.NONE
        expected_event_signal_to_export = EventSignalToExport.Source_Complete_Event
        expected_output_event_signal_terminal = ""

        instance = TriggerParameters(
            source_trigger_behavior=expected_source_trigger_behavior,
            start_source_name=expected_start_source_name,
            export_event=expected_export_event,
            event_signal_to_export=expected_event_signal_to_export,
            output_event_signal_terminal=expected_output_event_signal_terminal,
        )

        self.assertEqual(expected_source_trigger_behavior, instance.source_trigger_behavior)
        self.assertEqual(expected_start_source_name, instance.start_source_name)
        self.assertEqual(expected_export_event, instance.export_event)
        self.assertEqual(expected_event_signal_to_export, instance.event_signal_to_export)
        self.assertEqual(expected_output_event_signal_terminal, instance.output_event_signal_terminal)


class TestDCCurrentSourceAndMeasureParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DCCurrentSourceAndMeasureParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_current_source_and_measure_parameters(self):
        """Checks DCCurrentSourceAndMeasureParameters construction and property getters."""  # noqa: D415, W505
        expected_current_channel_settings = CurrentChannelSettings(
            current_level=10e-6,
            current_level_range=0.1,
            voltage_limit=1.0,
            voltage_limit_range=2.0,
            sensing=nidcpower.Sense.REMOTE,
            enable_output=True,
        )
        expected_execution_settings = ExecutionSettings(
            execution_type=MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            skip_analysis=False,
        )
        expected_timing_parameters = TimingParameters(
            source_delay=0.1,
            aperture_time=0.02,
            transient_response=nidcpower.TransientResponse.NORMAL,
        )
        expected_trigger_parameters = TriggerParameters(
            source_trigger_behavior=SourceTriggerBehavior.Disable_Source_Trigger,
            start_source_name="",
            export_event=ExportEvent.NONE,
            event_signal_to_export=EventSignalToExport.Source_Complete_Event,
            output_event_signal_terminal="",
        )

        instance = DCCurrentSourceAndMeasureParameters(
            current_channel_settings=expected_current_channel_settings,
            execution_settings=expected_execution_settings,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        self.assertIs(expected_current_channel_settings, instance.current_channel_settings)
        self.assertIs(expected_execution_settings, instance.execution_settings)
        self.assertIs(expected_timing_parameters, instance.timing_parameters)
        self.assertIs(expected_trigger_parameters, instance.trigger_parameters)


class TestDCCurrentSourceAndMeasureResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DCCurrentSourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_current_source_and_measure_result_data(self):
        """Checks DCCurrentSourceAndMeasureResultData construction and property getters."""  # noqa: D415, W505
        expected_execution_settings = {
            "Current Level Setting (A)": "10.0 uA",
            "Current Level Range (A)": "100.00 mA",
            "Voltage Limit Setting (V)": "1.000000 V",
            "Voltage Limit Range (V)": "2.00 V",
            "Aperture Time (Sec)": "20.0 ms",
            "Output Function": "DC_CURRENT",
            "Device Model": "NI PXIe-4141",
        }
        expected_measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": "1.000000 V",
                "Current Measurement": "10.0 uA",
                "Power": "10.0 uW",
                "Resistance": "100.00 kOhm",
            },
            "raw_measurements": {
                "Voltage Measurement (V)": 1.0,
                "Current Measurement (A)": 10e-6,
                "Power (W)": 10e-6,
                "Resistance (Ohm)": 100000.0,
            },
            "Compliance/Limit Reached": False,
        }

        instance = DCCurrentSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertEqual(expected_execution_settings, instance.execution_settings)
        self.assertEqual(expected_measurement_results, instance.measurement_results)

    def test_dc_current_source_and_measure_result_data_with_nan_values(self):
        """Checks DCCurrentSourceAndMeasureResultData with NaN values when no measurement is performed."""  # noqa: D415, W505
        expected_execution_settings = {
            "Current Level Setting (A)": math.nan,
            "Current Level Range (A)": math.nan,
            "Voltage Limit Setting (V)": math.nan,
            "Voltage Limit Range (V)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": "DC_CURRENT",
        }
        expected_measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": math.nan,
                "Current Measurement": math.nan,
            },
            "raw_measurements": {
                "Voltage Measurement (V)": math.nan,
                "Current Measurement (A)": math.nan,
            },
            "Compliance/Limit Reached": False,
        }

        instance = DCCurrentSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertTrue(math.isnan(instance.execution_settings["Current Level Setting (A)"]))
        self.assertTrue(math.isnan(instance.execution_settings["Aperture Time (Sec)"]))
        self.assertEqual("DC_CURRENT", instance.execution_settings["Output Function"])
        self.assertTrue(
            math.isnan(
                instance.measurement_results["formatted_measurements"]["Voltage Measurement"]
            )
        )
        self.assertTrue(
            math.isnan(
                instance.measurement_results["raw_measurements"]["Voltage Measurement (V)"]
            )
        )
        self.assertFalse(instance.measurement_results["Compliance/Limit Reached"])

    def test_dc_current_source_and_measure_result_data_compliance_reached(self):
        """Checks DCCurrentSourceAndMeasureResultData when compliance limit is reached."""  # noqa: D415, W505
        expected_execution_settings = {
            "Current Level Setting (A)": 10e-6,
            "Output Function": "DC_CURRENT",
        }
        expected_measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": "5.000000 V",
                "Current Measurement": "10.0 uA",
            },
            "raw_measurements": {
                "Voltage Measurement (V)": 5.0,
                "Current Measurement (A)": 10e-6,
            },
            "Compliance/Limit Reached": True,
        }

        instance = DCCurrentSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertTrue(instance.measurement_results["Compliance/Limit Reached"])


class TestConstantsForDCCurrentSourceAndMeasure(unittest.TestCase):
    """Defines a test fixture that checks
    `ConstantsForDCCurrentSourceAndMeasure` and default instances are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_default_execution_settings(self):
        """Checks DEFAULT_DC_CC_EXECUTION_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            DEFAULT_DC_CC_EXECUTION_SETTINGS.execution_type,
        )
        self.assertEqual(False, DEFAULT_DC_CC_EXECUTION_SETTINGS.skip_analysis)

    def test_default_channel_settings(self):
        """Checks DEFAULT_DC_CC_CHANNEL_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.current_level,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_RANGE_AMPERES,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.current_level_range,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_VOLTS,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.voltage_limit,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.voltage_limit_range,
        )
        self.assertEqual(
            nidcpower.Sense.REMOTE,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.sensing,
        )
        self.assertEqual(True, DEFAULT_DC_CC_CHANNEL_SETTINGS.enable_output)

    def test_default_timing_parameters(self):
        """Checks DEFAULT_DC_CC_TIMING_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            DEFAULT_DC_CC_TIMING_PARAMETERS.source_delay,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
            DEFAULT_DC_CC_TIMING_PARAMETERS.aperture_time,
        )
        self.assertEqual(
            nidcpower.TransientResponse.NORMAL,
            DEFAULT_DC_CC_TIMING_PARAMETERS.transient_response,
        )

    def test_default_trigger_parameters(self):
        """Checks DEFAULT_DC_CC_TRIGGER_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            DEFAULT_DC_CC_TRIGGER_PARAMETERS.source_trigger_behavior,
        )
        self.assertEqual("", DEFAULT_DC_CC_TRIGGER_PARAMETERS.start_source_name)
        self.assertEqual(ExportEvent.NONE, DEFAULT_DC_CC_TRIGGER_PARAMETERS.export_event)
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event,
            DEFAULT_DC_CC_TRIGGER_PARAMETERS.event_signal_to_export,
        )
        self.assertEqual("", DEFAULT_DC_CC_TRIGGER_PARAMETERS.output_event_signal_terminal)

    def test_default_source_and_measure_parameters(self):
        """Checks DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS has expected default sub-objects."""  # noqa: D415, W505
        params = DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS

        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES,
            params.current_channel_settings.current_level,
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            params.execution_settings.execution_type,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            params.timing_parameters.source_delay,
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            params.trigger_parameters.source_trigger_behavior,
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/__init__.py sha256=aec9a1bad3d889345608fa2a0535cc7cc011e78c481a6ca25261cdc3e2764e22 bytes=85 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/__init__.py`
- sha256: `aec9a1bad3d889345608fa2a0535cc7cc011e78c481a6ca25261cdc3e2764e22`
- bytes: 85

````python
"""Provides Unit tests for dc cv source and Smeasurements in the pcbatt_library."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/test_dc_cv_source_and_measure.py sha256=55f56bc0176710c46a79d275aff2fdea817a0afebbc30a435fe8bb33e1d17199 bytes=30470 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/test_dc_cv_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/test_dc_cv_source_and_measure.py`
- sha256: `55f56bc0176710c46a79d275aff2fdea817a0afebbc30a435fe8bb33e1d17199`
- bytes: 30470

````python
# pylint: disable=C0301
"""This module provides DC constant voltage source and measure data types unit tests."""

import importlib.metadata
import logging
import math
import sys
import unittest

import nidcpower
from varname import nameof

from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    DCVoltageSourceAndMeasureResultData,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_constants import (
    ConstantsForDCVoltageSourceAndMeasure,
    DEFAULT_DC_CV_CHANNEL_SETTINGS,
    DEFAULT_DC_CV_EXECUTION_SETTINGS,
    DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_DC_CV_TIMING_PARAMETERS,
    DEFAULT_DC_CV_TRIGGER_PARAMETERS,
)


class TestMeasurementExecutionType(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementExecutionType` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_measurement_execution_type_members(self):
        """Checks MeasurementExecutionType enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE.value,
            "CONFIGURE_SOURCE_AND_MEASURE",
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_ONLY.value,
            "CONFIGURE_ONLY",
        )
        self.assertEqual(
            MeasurementExecutionType.START_SOURCE_ONLY.value,
            "START_SOURCE_ONLY",
        )
        self.assertEqual(
            MeasurementExecutionType.MEASURE_ONLY.value,
            "MEASURE_ONLY",
        )
        self.assertEqual(len(MeasurementExecutionType), 4)


class TestSourceTriggerBehavior(unittest.TestCase):
    """Defines a test fixture that checks
    `SourceTriggerBehavior` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_source_trigger_behavior_members(self):
        """Checks SourceTriggerBehavior enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            SourceTriggerBehavior.Start_Source_Trigger.value,
            "Start_Source_Trigger",
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger.value,
            "Disable_Source_Trigger",
        )
        self.assertEqual(len(SourceTriggerBehavior), 2)


class TestExportEvent(unittest.TestCase):
    """Defines a test fixture that checks
    `ExportEvent` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_export_event_members(self):
        """Checks ExportEvent enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(ExportEvent.NONE.value, "NONE")
        self.assertEqual(ExportEvent.Route_Event.value, "Route_Event")
        self.assertEqual(len(ExportEvent), 2)


class TestEventSignalToExport(unittest.TestCase):
    """Defines a test fixture that checks
    `EventSignalToExport` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_event_signal_to_export_members(self):
        """Checks EventSignalToExport enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event.value,
            "source_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Measure_Complete_Event.value,
            "measure_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Iteration_Complete_Event.value,
            "sequence_iteration_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Engine_Done_Event.value,
            "sequence_engine_done_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Pulse_Complete_Event.value,
            "pulse_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Ready_for_Pulse_Trigger_Event.value,
            "ready_for_pulse_trigger_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Start_Trigger.value,
            "exported_start_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Source_Trigger.value,
            "exported_source_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Measure_Trigger.value,
            "exported_measure_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Advance_Trigger.value,
            "exported_sequence_advance_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Pulse_Trigger.value,
            "exported_pulse_trigger_output_terminal",
        )
        self.assertEqual(len(EventSignalToExport), 11)


class TestExecutionSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `ExecutionSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_execution_settings(self):
        """Checks ExecutionSettings construction and property getters."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
        expected_skip_analysis = True

        instance = ExecutionSettings(
            execution_type=expected_execution_type,
            skip_analysis=expected_skip_analysis,
        )

        self.assertEqual(expected_execution_type, instance.execution_type)
        self.assertEqual(expected_skip_analysis, instance.skip_analysis)

    def test_execution_settings_configure_only(self):
        """Checks ExecutionSettings with CONFIGURE_ONLY execution type."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_ONLY
        expected_skip_analysis = False

        instance = ExecutionSettings(
            execution_type=expected_execution_type,
            skip_analysis=expected_skip_analysis,
        )

        self.assertEqual(expected_execution_type, instance.execution_type)
        self.assertEqual(expected_skip_analysis, instance.skip_analysis)


class TestVoltageChannelSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageChannelSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_voltage_channel_settings(self):
        """Checks VoltageChannelSettings construction and property getters."""  # noqa: D415, W505
        expected_voltage_level = 5.0
        expected_voltage_level_range = 6.0
        expected_current_limit = 0.01
        expected_current_limit_range = 0.1
        expected_sensing = nidcpower.Sense.REMOTE
        expected_enable_output = True

        instance = VoltageChannelSettings(
            voltage_level=expected_voltage_level,
            voltage_level_range=expected_voltage_level_range,
            current_limit=expected_current_limit,
            current_limit_range=expected_current_limit_range,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
        )

        self.assertEqual(expected_voltage_level, instance.voltage_level)
        self.assertEqual(expected_voltage_level_range, instance.voltage_level_range)
        self.assertEqual(expected_current_limit, instance.current_limit)
        self.assertEqual(expected_current_limit_range, instance.current_limit_range)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)

    def test_voltage_channel_settings_local_sensing(self):
        """Checks VoltageChannelSettings with LOCAL sensing and output disabled."""  # noqa: D415, W505
        expected_voltage_level = 3.3
        expected_voltage_level_range = 5.0
        expected_current_limit = 0.05
        expected_current_limit_range = 0.5
        expected_sensing = nidcpower.Sense.LOCAL
        expected_enable_output = False

        instance = VoltageChannelSettings(
            voltage_level=expected_voltage_level,
            voltage_level_range=expected_voltage_level_range,
            current_limit=expected_current_limit,
            current_limit_range=expected_current_limit_range,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
        )

        self.assertEqual(expected_voltage_level, instance.voltage_level)
        self.assertEqual(expected_voltage_level_range, instance.voltage_level_range)
        self.assertEqual(expected_current_limit, instance.current_limit)
        self.assertEqual(expected_current_limit_range, instance.current_limit_range)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)


class TestTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_timing_parameters(self):
        """Checks TimingParameters construction and property getters."""  # noqa: D415, W505
        expected_source_delay = 0.1
        expected_aperture_time = 0.02
        expected_transient_response = nidcpower.TransientResponse.NORMAL

        instance = TimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)

    def test_timing_parameters_fast_transient(self):
        """Checks TimingParameters with FAST transient response."""  # noqa: D415, W505
        expected_source_delay = 0.05
        expected_aperture_time = 0.01
        expected_transient_response = nidcpower.TransientResponse.FAST

        instance = TimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)


class TestTriggerParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_trigger_parameters_with_trigger_enabled(self):
        """Checks TriggerParameters with source trigger enabled and event routing."""  # noqa: D415, W505
        expected_source_trigger_behavior = SourceTriggerBehavior.Start_Source_Trigger
        expected_start_source_name = "/PXI1Slot2/PXI_Trig0"
        expected_export_event = ExportEvent.Route_Event
        expected_event_signal_to_export = EventSignalToExport.Source_Complete_Event
        expected_output_event_signal_terminal = "/PXI1Slot2/PXI_Trig1"

        instance = TriggerParameters(
            source_trigger_behavior=expected_source_trigger_behavior,
            start_source_name=expected_start_source_name,
            export_event=expected_export_event,
            event_signal_to_export=expected_event_signal_to_export,
            output_event_signal_terminal=expected_output_event_signal_terminal,
        )

        self.assertEqual(expected_source_trigger_behavior, instance.source_trigger_behavior)
        self.assertEqual(expected_start_source_name, instance.start_source_name)
        self.assertEqual(expected_export_event, instance.export_event)
        self.assertEqual(expected_event_signal_to_export, instance.event_signal_to_export)
        self.assertEqual(expected_output_event_signal_terminal, instance.output_event_signal_terminal)

    def test_trigger_parameters_with_trigger_disabled(self):
        """Checks TriggerParameters with source trigger disabled and no event routing."""  # noqa: D415, W505
        expected_source_trigger_behavior = SourceTriggerBehavior.Disable_Source_Trigger
        expected_start_source_name = ""
        expected_export_event = ExportEvent.NONE
        expected_event_signal_to_export = EventSignalToExport.Source_Complete_Event
        expected_output_event_signal_terminal = ""

        instance = TriggerParameters(
            source_trigger_behavior=expected_source_trigger_behavior,
            start_source_name=expected_start_source_name,
            export_event=expected_export_event,
            event_signal_to_export=expected_event_signal_to_export,
            output_event_signal_terminal=expected_output_event_signal_terminal,
        )

        self.assertEqual(expected_source_trigger_behavior, instance.source_trigger_behavior)
        self.assertEqual(expected_start_source_name, instance.start_source_name)
        self.assertEqual(expected_export_event, instance.export_event)
        self.assertEqual(expected_event_signal_to_export, instance.event_signal_to_export)
        self.assertEqual(expected_output_event_signal_terminal, instance.output_event_signal_terminal)


class TestDCVoltageSourceAndMeasureParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DCVoltageSourceAndMeasureParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_voltage_source_and_measure_parameters(self):
        """Checks DCVoltageSourceAndMeasureParameters construction and property getters."""  # noqa: D415, W505
        expected_voltage_channel_settings = VoltageChannelSettings(
            voltage_level=5.0,
            voltage_level_range=6.0,
            current_limit=0.01,
            current_limit_range=0.1,
            sensing=nidcpower.Sense.REMOTE,
            enable_output=True,
        )
        expected_execution_settings = ExecutionSettings(
            execution_type=MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            skip_analysis=False,
        )
        expected_timing_parameters = TimingParameters(
            source_delay=0.1,
            aperture_time=0.02,
            transient_response=nidcpower.TransientResponse.NORMAL,
        )
        expected_trigger_parameters = TriggerParameters(
            source_trigger_behavior=SourceTriggerBehavior.Disable_Source_Trigger,
            start_source_name="",
            export_event=ExportEvent.NONE,
            event_signal_to_export=EventSignalToExport.Source_Complete_Event,
            output_event_signal_terminal="",
        )

        instance = DCVoltageSourceAndMeasureParameters(
            voltage_channel_settings=expected_voltage_channel_settings,
            execution_settings=expected_execution_settings,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        self.assertIs(expected_voltage_channel_settings, instance.voltage_channel_settings)
        self.assertIs(expected_execution_settings, instance.execution_settings)
        self.assertIs(expected_timing_parameters, instance.timing_parameters)
        self.assertIs(expected_trigger_parameters, instance.trigger_parameters)


class TestDCVoltageSourceAndMeasureResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DCVoltageSourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_voltage_source_and_measure_result_data(self):
        """Checks DCVoltageSourceAndMeasureResultData construction and property getters."""  # noqa: D415, W505
        expected_execution_settings = {
            "Voltage Level Setting (V)": "1.000000 V",
            "Voltage Level Range (V)": "1.00 V",
            "Current Limit Setting (A)": "10.0 mA",
            "Current Limit Range (A)": "100.00 mA",
            "Aperture Time (Sec)": "20.0 ms",
            "Output Function": "DC_VOLTAGE",
            "Device Model": "NI PXIe-4141",
        }
        expected_measurement_results = {
            "Voltage Measurement (V)": "1.000000 V",
            "Current Measurement (A)": "5.00 mA",
            "Power (W)": "5.00 mW",
            "Resistance (Ohm)": "200 Ohm",
            "Compliance/Limit Reached": False,
        }

        instance = DCVoltageSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertEqual(expected_execution_settings, instance.execution_settings)
        self.assertEqual(expected_measurement_results, instance.measurement_results)

    def test_dc_voltage_source_and_measure_result_data_with_nan_values(self):
        """Checks DCVoltageSourceAndMeasureResultData with NaN values when no measurement is performed."""  # noqa: D415, W505
        expected_execution_settings = {
            "Voltage Level Setting (V)": math.nan,
            "Voltage Level Range (V)": math.nan,
            "Current Limit Setting (A)": math.nan,
            "Current Limit Range (A)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": "DC_VOLTAGE",
        }
        expected_measurement_results = {
            "Voltage Measurement (V)": math.nan,
            "Current Measurement (A)": math.nan,
            "Power (W)": math.nan,
            "Resistance (Ohm)": math.nan,
            "Compliance/Limit Reached": False,
        }

        instance = DCVoltageSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertTrue(math.isnan(instance.execution_settings["Voltage Level Setting (V)"]))
        self.assertTrue(math.isnan(instance.execution_settings["Aperture Time (Sec)"]))
        self.assertEqual("DC_VOLTAGE", instance.execution_settings["Output Function"])
        self.assertTrue(math.isnan(instance.measurement_results["Voltage Measurement (V)"]))
        self.assertFalse(instance.measurement_results["Compliance/Limit Reached"])


class TestConstantsForDCVoltageSourceAndMeasure(unittest.TestCase):
    """Defines a test fixture that checks
    `ConstantsForDCVoltageSourceAndMeasure` and default instances are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_default_execution_settings(self):
        """Checks DEFAULT_DC_CV_EXECUTION_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            DEFAULT_DC_CV_EXECUTION_SETTINGS.execution_type,
        )
        self.assertEqual(False, DEFAULT_DC_CV_EXECUTION_SETTINGS.skip_analysis)

    def test_default_channel_settings(self):
        """Checks DEFAULT_DC_CV_CHANNEL_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_VOLTS,
            DEFAULT_DC_CV_CHANNEL_SETTINGS.voltage_level,
        )
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
            DEFAULT_DC_CV_CHANNEL_SETTINGS.voltage_level_range,
        )
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES,
            DEFAULT_DC_CV_CHANNEL_SETTINGS.current_limit,
        )
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES,
            DEFAULT_DC_CV_CHANNEL_SETTINGS.current_limit_range,
        )
        self.assertEqual(
            nidcpower.Sense.REMOTE,
            DEFAULT_DC_CV_CHANNEL_SETTINGS.sensing,
        )
        self.assertEqual(True, DEFAULT_DC_CV_CHANNEL_SETTINGS.enable_output)

    def test_default_timing_parameters(self):
        """Checks DEFAULT_DC_CV_TIMING_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            DEFAULT_DC_CV_TIMING_PARAMETERS.source_delay,
        )
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
            DEFAULT_DC_CV_TIMING_PARAMETERS.aperture_time,
        )
        self.assertEqual(
            nidcpower.TransientResponse.NORMAL,
            DEFAULT_DC_CV_TIMING_PARAMETERS.transient_response,
        )

    def test_default_trigger_parameters(self):
        """Checks DEFAULT_DC_CV_TRIGGER_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            DEFAULT_DC_CV_TRIGGER_PARAMETERS.source_trigger_behavior,
        )
        self.assertEqual("", DEFAULT_DC_CV_TRIGGER_PARAMETERS.start_source_name)
        self.assertEqual(ExportEvent.NONE, DEFAULT_DC_CV_TRIGGER_PARAMETERS.export_event)
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event,
            DEFAULT_DC_CV_TRIGGER_PARAMETERS.event_signal_to_export,
        )
        self.assertEqual("", DEFAULT_DC_CV_TRIGGER_PARAMETERS.output_event_signal_terminal)

    def test_default_source_and_measure_parameters(self):
        """Checks DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS has expected default sub-objects."""  # noqa: D415, W505
        params = DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS

        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_VOLTS,
            params.voltage_channel_settings.voltage_level,
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            params.execution_settings.execution_type,
        )
        self.assertEqual(
            ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            params.timing_parameters.source_delay,
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            params.trigger_parameters.source_trigger_behavior,
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/__init__.py sha256=a1e1034901e78df318cebb042c209ef9e4414e086535cd6c318a067151e99fc6 bytes=477 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/__init__.py`
- sha256: `a1e1034901e78df318cebb042c209ef9e4414e086535cd6c318a067151e99fc6`
- bytes: 477

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.power_supply_source_and_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_and_measure.py sha256=7dce30034df255ad8e8e8fae56f1520def99af3ad04f99b33b9153bc04048f52 bytes=7459 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_and_measure.py`
- sha256: `7dce30034df255ad8e8e8fae56f1520def99af3ad04f99b33b9153bc04048f52`
- bytes: 7459

````python
# pylint: disable=C0301
"""This module provides PowerSupplySourceAndMeasure check."""
import importlib.metadata
import logging
import sys
import unittest

import numpy as np
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterPowerSupplySourceAndMeasure,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestPowerSupplySourceAndMeasure(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasure` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_InterpreterPowerSupplySourceAndMeasure)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_power_supply_source_and_measure(self):
        """Checks if class PowerSupplySourceAndMeasure is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.daq.PowerSupplySourceAndMeasure()

        measurement.initialize(power_channel_name="Sim_PXIeDAQ/power")

        measurement.configure_and_measure(
            configuration=nipcbatt.daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION
        )

        measurement.close()

    def test_analyze_measurement_data_results_when_providing_valid_data(self):
        """unit test of PowerSupplySourceAndMeasureData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)
        ############ ARRANGE ######################################
        # create data objects for test
        voltage_samples1 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])
        voltage_samples2 = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0])
        voltage_samples4 = np.asarray([-99.0, 0.0, 99.0, 0.0, -99.0])

        current_samples1 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])
        current_samples2 = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0])
        current_samples4 = np.asarray([-99.0, 0.0, 99.0, 0.0, -99.0])

        sample_rate1 = 1000000000  # 1 GHz
        sample_rate2 = 100000000  # 100 MHz
        sample_rate4 = 1000000  # 1 MHz

        data_1 = nipcbatt.daq.PowerSupplySourceAndMeasureData(
            "data1", voltage_samples1, current_samples1, sample_rate1
        )

        data_2 = nipcbatt.daq.PowerSupplySourceAndMeasureData(
            "data2", voltage_samples2, current_samples2, sample_rate2
        )

        data_4 = nipcbatt.daq.PowerSupplySourceAndMeasureData(
            "data4", voltage_samples4, current_samples4, sample_rate4
        )

        #################### ACT ######################################################
        # generate result objects
        res_data_1 = nipcbatt.daq.PowerSupplySourceAndMeasure.analyze_measurement_data(
            self, data_1, nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )
        res_data_2 = nipcbatt.daq.PowerSupplySourceAndMeasure.analyze_measurement_data(
            self, data_2, nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )
        res_data_4 = nipcbatt.daq.PowerSupplySourceAndMeasure.analyze_measurement_data(
            self, data_4, nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        #################### ASSERT ###################################################
        # test max voltage
        self.assertAlmostEqual(res_data_1.max_voltage_level_volts, 2.0, places=5)
        self.assertAlmostEqual(res_data_2.max_voltage_level_volts, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.max_voltage_level_volts, 99.0, places=5)

        # test max current
        self.assertAlmostEqual(res_data_1.max_current_level_amperes, 2.0, places=5)
        self.assertAlmostEqual(res_data_2.max_current_level_amperes, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.max_current_level_amperes, 99.0, places=5)

        # test max power
        self.assertAlmostEqual(res_data_1.max_power_level_watts, 4.0, places=5)
        self.assertAlmostEqual(res_data_2.max_power_level_watts, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.max_power_level_watts, 9801.0, places=5)

        # test average power
        self.assertAlmostEqual(res_data_1.average_power_value_watts, 2.0, places=5)
        self.assertAlmostEqual(res_data_2.average_power_value_watts, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.average_power_value_watts, 5880.6, places=5)

        # test acquisition duration
        self.assertAlmostEqual(res_data_1.acquisition_duration_seconds, 5e-09, places=5)
        self.assertAlmostEqual(res_data_2.acquisition_duration_seconds, 5e-08, places=5)
        self.assertAlmostEqual(res_data_4.acquisition_duration_seconds, 5e-06, places=5)

    def test_analyze_measurement_data_results_when_providing_undefined_data(self):
        """unit test of PowerSupplySourceAndMeasureData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)
        ############ ARRANGE ######################################
        # create data objects for test
        voltage_samples1 = None
        voltage_samples2 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])

        current_samples1 = None
        current_samples2 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])

        sample_rate1 = None
        sample_rate2 = 1000000  # 1 MHz

        #################### ACT & ASSERT ###################################################
        # test PowerSupplySourceAndMeasureData constructor
        with self.assertRaises(ValueError):
            print(
                nipcbatt.daq.PowerSupplySourceAndMeasureData(
                    "data1", voltage_samples1, current_samples2, sample_rate2
                )
            )

            print(
                nipcbatt.daq.PowerSupplySourceAndMeasureData(
                    "data2", voltage_samples2, current_samples1, sample_rate2
                )
            )

            print(
                nipcbatt.daq.PowerSupplySourceAndMeasureData(
                    "data3", voltage_samples2, current_samples2, sample_rate1
                )
            )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_data_types.py sha256=f9987af10d6d5f88daa7d0cf435c5bf894751fca0b7b8c5bc59eee00a0e8113d bytes=21432 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_data_types.py`
- sha256: `f9987af10d6d5f88daa7d0cf435c5bf894751fca0b7b8c5bc59eee00a0e8113d`
- bytes: 21432

````python
"""This module provides Power supply source data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
import numpy.testing
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestPowerSupplySourceAndMeasureTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_power_supply_source_and_measure_terminal_parameters(self):
        """unit test of PowerSupplySourceAndMeasureTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        expected_voltage_setpoint_volts = 5.0
        expected_current_setpoint_amperes = 0.5
        expected_power_sense = nidaqmx.constants.Sense.LOCAL
        expected_idle_output_behaviour = nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED
        expected_enable_output = True

        instance = daq.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=expected_voltage_setpoint_volts,
            current_setpoint_amperes=expected_current_setpoint_amperes,
            power_sense=expected_power_sense,
            idle_output_behaviour=expected_idle_output_behaviour,
            enable_output=expected_enable_output,
        )

        actual_voltage_setpoint_volts = instance.voltage_setpoint_volts
        actual_current_setpoint_amperes = instance.current_setpoint_amperes
        actual_power_sense = instance.power_sense
        actual_idle_output_behaviour = instance.idle_output_behaviour
        actual_enable_output = instance.enable_output

        self.assertEqual(expected_voltage_setpoint_volts, actual_voltage_setpoint_volts)
        self.assertEqual(expected_current_setpoint_amperes, actual_current_setpoint_amperes)
        self.assertEqual(expected_power_sense, actual_power_sense)
        self.assertEqual(expected_idle_output_behaviour, actual_idle_output_behaviour)
        self.assertEqual(expected_enable_output, actual_enable_output)


class TestPowerSupplySourceAndMeasureConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_power_supply_source_and_measure_configuration(self):
        """unit test of PowerSupplySourceAndMeasureConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        expected_voltage_setpoint_volts = 0.5
        expected_current_setpoint_amperes = 0.02
        expected_power_sense = nidaqmx.constants.Sense.REMOTE
        expected_idle_output_behaviour = nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED
        expected_enable_output = False

        expected_terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=expected_voltage_setpoint_volts,
            current_setpoint_amperes=expected_current_setpoint_amperes,
            power_sense=expected_power_sense,
            idle_output_behaviour=expected_idle_output_behaviour,
            enable_output=expected_enable_output,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 1000
        expected_number_of_samples_per_channel = 500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        instance = daq.PowerSupplySourceAndMeasureConfiguration(
            terminal_parameters=expected_terminal_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_voltage_setpoint_volts = instance.terminal_parameters.voltage_setpoint_volts
        actual_current_setpoint_amperes = instance.terminal_parameters.current_setpoint_amperes
        actual_power_sense = instance.terminal_parameters.power_sense
        actual_idle_output_behaviour = instance.terminal_parameters.idle_output_behaviour
        actual_enable_output = instance.terminal_parameters.enable_output

        actual_execution_option = instance.measurement_options.execution_option
        actual_measurement_analysis_requirement = (
            instance.measurement_options.measurement_analysis_requirement
        )
        actual_sample_clock_source = instance.sample_clock_timing_parameters.sample_clock_source
        actual_sampling_rate_hertz = instance.sample_clock_timing_parameters.sampling_rate_hertz
        actual_number_of_samples_per_channel = (
            instance.sample_clock_timing_parameters.number_of_samples_per_channel
        )
        actual_sample_timing_engine = instance.sample_clock_timing_parameters.sample_timing_engine

        self.assertEqual(expected_voltage_setpoint_volts, actual_voltage_setpoint_volts)
        self.assertEqual(expected_current_setpoint_amperes, actual_current_setpoint_amperes)
        self.assertEqual(expected_power_sense, actual_power_sense)
        self.assertEqual(expected_idle_output_behaviour, actual_idle_output_behaviour)
        self.assertEqual(expected_enable_output, actual_enable_output)

        self.assertEqual(expected_execution_option, actual_execution_option)
        self.assertEqual(
            expected_measurement_analysis_requirement,
            actual_measurement_analysis_requirement,
        )
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_number_of_samples_per_channel, actual_number_of_samples_per_channel
        )
        self.assertEqual(
            expected_sample_timing_engine,
            actual_sample_timing_engine,
        )


class TestPowerSupplySourceAndMeasureData(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_power_supply_source_and_measure_data(self):
        """unit test of PowerSupplySourceAndMeasureData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)
        expected_source_name = "test_power_source_name"
        expected_voltage_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_current_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_sampling_rate_hertz = 5000

        instance = daq.PowerSupplySourceAndMeasureData(
            source_name=expected_source_name,
            voltage_samples=expected_voltage_samples,
            current_samples=expected_current_samples,
            sampling_rate_hertz=expected_sampling_rate_hertz,
        )

        actual_source_name = instance.source_name
        actual_voltage_samples = instance.voltage_samples
        actual_current_samples = instance.current_samples
        actual_sampling_rate = instance.sampling_rate_hertz

        self.assertEqual(expected_source_name, actual_source_name)
        self.assertTrue((expected_voltage_samples == actual_voltage_samples).all())
        self.assertTrue((expected_current_samples == actual_current_samples).all())
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate)

    def test_power_supply_source_and_measure_data_with_invalid_data(self):
        """Tests if expected error is thrown when creating an instance of
        `PowerSupplySourceAndMeasureData` with invalid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        expected_source_name = "test_power_source_name"
        expected_voltage_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_current_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_sampling_rate_hertz = 5000

        # Test if the value error is thrown if voltage_samples is None
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=None,
                current_samples=expected_current_samples,
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if voltage_samples is empty
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=[],
                current_samples=expected_current_samples,
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if current_samples is None
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=expected_voltage_samples,
                current_samples=None,
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if current_samples is empty
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=expected_voltage_samples,
                current_samples=[],
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if sampling_rate is 0
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=expected_voltage_samples,
                current_samples=expected_current_samples,
                sampling_rate_hertz=0,
            ),
        )


class TestPowerSupplySourceAndMeasureResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_power_supply_source_and_measure_result_data(self):
        """unit test of PowerSupplySourceAndMeasureResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)
        # todo: write test code
        expected_voltage_waveform = nipcbatt.AnalogWaveform(
            channel_name="Dev/pow0",
            delta_time_seconds=1.0 / 10000,
            samples=numpy.array(
                [random.random() * 0.1 for item in range(0, 1000)],
                dtype=numpy.float64,
            ),
        )

        expected_current_waveform = nipcbatt.AnalogWaveform(
            channel_name="Dev/pow1",
            delta_time_seconds=1.0 / 10000,
            samples=numpy.array(
                [random.random() * 0.1 for item in range(0, 1000)], dtype=numpy.float64
            ),
        )

        expected_max_voltage_level_volts = 1.0
        expected_max_current_level_amperes = 0.1
        expected_max_power_level_watts = 0.2
        expected_average_power_value_watts = 0.8
        expected_acquisition_duration_seconds = 0.01

        instance = daq.PowerSupplySourceAndMeasureResultData(
            voltage_waveform=expected_voltage_waveform,
            current_waveform=expected_current_waveform,
            max_voltage_level_volts=expected_max_voltage_level_volts,
            max_current_level_amperes=expected_max_current_level_amperes,
            max_power_level_watts=expected_max_power_level_watts,
            average_power_value_watts=expected_average_power_value_watts,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
        )

        actual_voltage_waveform = instance.voltage_waveform
        actual_current_waveform = instance.current_waveform
        actual_max_voltage_level_volts = instance.max_voltage_level_volts
        actual_max_current_level_amperes = instance.max_current_level_amperes
        actual_max_power_level_watts = instance.max_power_level_watts
        actual_average_power_value_watts = instance.average_power_value_watts
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds

        self.assertEqual(expected_voltage_waveform, actual_voltage_waveform)
        self.assertEqual(expected_current_waveform, actual_current_waveform)
        self.assertEqual(expected_max_voltage_level_volts, actual_max_voltage_level_volts)
        self.assertEqual(expected_max_current_level_amperes, actual_max_current_level_amperes)
        self.assertEqual(expected_max_power_level_watts, actual_max_power_level_watts)
        self.assertEqual(expected_average_power_value_watts, actual_average_power_value_watts)
        self.assertEqual(expected_acquisition_duration_seconds, actual_acquisition_duration_seconds)

    def test_power_supply_source_and_measure_result_data_with_invalid_waveforms(
        self,
    ):
        """Test if the expected error is thrown if the current or voltage waveform is None"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (281 > 100 characters) (auto-generated noqa)

        test_sample_waveform = nipcbatt.AnalogWaveform(
            channel_name="Dev/pow0",
            delta_time_seconds=1.0 / 10000,
            samples=numpy.array(
                [random.random() * 0.1 for item in range(0, 1000)],
                dtype=numpy.float64,
            ),
        )
        # Test if Value error is raised in voltage_waveform instance is None
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureResultData(
                voltage_waveform=None,
                current_waveform=test_sample_waveform,
                max_voltage_level_volts=0.0,
                max_current_level_amperes=0.0,
                max_power_level_watts=0.0,
                average_power_value_watts=0.01,
                acquisition_duration_seconds=0.05,
            ),
        )

        # Test if Value error is raised in current_waveform instance is None
        self.assertRaises(
            ValueError,
            lambda: daq.PowerSupplySourceAndMeasureResultData(
                voltage_waveform=test_sample_waveform,
                current_waveform=None,
                max_voltage_level_volts=0.0,
                max_current_level_amperes=0.0,
                max_power_level_watts=0.0,
                average_power_value_watts=0.01,
                acquisition_duration_seconds=0.05,
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/test_dmm_resistance_measurements.py sha256=8d1647147c9cdce5722bc36d858b53f7f47f65f1c30fa9f9fd2ea4259d463afb bytes=5944 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/test_dmm_resistance_measurements.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/test_dmm_resistance_measurements.py`
- sha256: `8d1647147c9cdce5722bc36d858b53f7f47f65f1c30fa9f9fd2ea4259d463afb`
- bytes: 5944

````python
""" Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based resistance measurements """

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import dmm


class TestDmmResistance(unittest.TestCase):
    """Defines a test fixture that ensures the data types of the 
        dmm.Resistance class are created correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidmm_version = importlib.metadata.version("nidmm")
        logging.debug("%s = %s", nameof(used_nidmm_version), used_nidmm_version)
        
    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    
    def test_enum_members_shape_and_types(self):
        "Tests the creation of different type and shapes of enums"

        range_values = [member.value for member in dmm.ResistanceRangeAndFunctions]

        for value in range_values:
            data = dmm.ResistanceRangeAndFunctions(value)
            self.assertEqual(value, data.value)

    def test_function_params_basic_construction_and_properties(self):
        """Create a ResistanceMeasurementFunctionParameters and verify properties."""

        RESOLUTION = 6.5

        target_member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=target_member,
            resolution_in_digits=resolution,
        )

        # Verify properties return exactly what we passed in
        self.assertIs(params.measurement_function, target_member)
        self.assertIs(params.resolution_in_digits, resolution)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    def test_properties_are_effectively_read_only(self):
        """Attempting to assign to properties should raise AttributeError."""
        RESOLUTION = 5.5

        initial_member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=initial_member,
            resolution_in_digits=resolution,
        )

        # The class exposes read-only properties (no setters). Direct assignment should fail.
        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        # Confirm original values unchanged
        self.assertIs(params.measurement_function, initial_member)
        self.assertIs(params.resolution_in_digits, resolution)

    
    def test_basic_construction_and_properties(self):
        """Create params and verify properties return the same objects."""

        RESOLUTION = 6.5

        member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        res = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    def test_construct_for_every_current_range_enum_value(self):
        """Iterate all CurrentRangeAndFunctions, instantiate params, and verify."""
       
        res = dmm.ResolutionInDigits(5.5)

        for member in dmm.ResistanceRangeAndFunctions:
            params = dmm.ResistanceMeasurementFunctionParameters(
                measurement_function=member,
                resolution_in_digits=res,
            )
            self.assertIs(params.measurement_function, member)
            self.assertIs(params.resolution_in_digits, res)


    def test_dcrms_meas_config_properties_are_read_only(self):

        "Ensure all function properties are read only"

        member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        res = dmm.ResolutionInDigits(6.5)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)


    def test_identity_of_references(self):

        "Make sure the same object is returned, not a copy"

        member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_100k_Ohm
        res = dmm.ResolutionInDigits(7.5)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/__init__.py sha256=390b5c8f9565d7b8c451985e858eab97ed38741c9c97455543daae81f62c77f4 bytes=462 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/__init__.py`
- sha256: `390b5c8f9565d7b8c451985e858eab97ed38741c9c97455543daae81f62c77f4`
- bytes: 462

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.serial_communications package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (352 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_communication.py sha256=099ad9ece2ef4d4275d81abac702f994661f864bba79888269fb5b1e1544cd70 bytes=2918 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_communication.py`
- sha256: `099ad9ece2ef4d4275d81abac702f994661f864bba79888269fb5b1e1544cd70`
- bytes: 2918

````python
"""This module provides SerialCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import communications

class TestSerialCommunication(unittest.TestCase):
    """Defines a test fixture that checks `SerialCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skip(
        "The execution of test is skipped"
        + " because it requires a serial device that responds to VISA query.",
    )
    def test_serial_communication(self):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_communication.SerialCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.SerialCommunication() as communication:
            communication.initialize("ASRL7::INSTR")

            communication_parameters = communications.SerialCommunicationParameters(
                data_rate_bauds=9600,
                number_of_bits_in_data_frame=8,
                delay_before_receive_response_milliseconds=100,
                parity=communications.ConstantsForSerialCommunication.DEFAULT_PARITY,
                stop_bits=communications.ConstantsForSerialCommunication.DEFAULT_STOP_BITS,
                flow_control=communications.ConstantsForSerialCommunication.DEFAULT_FLOW_CONTROL_MODE,
            )
            configuration = communications.SerialCommunicationConfiguration(
                communication_parameters=communication_parameters,
                command_to_send="*IDN?",
            )

            print(f"parameters = {configuration}")
            results = communication.configure_then_send_command_and_receive_response(
                configuration=configuration
            )
            print(f"results = {results}")
            self.assertIsNotNone(results)
            self.assertIsInstance(results, communications.SerialCommunicationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_data_types.py sha256=9b494aa2bddb2c6afb7f745892c873deb779887d5a0aa1e9500ccdf7e2105776 bytes=25606 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_data_types.py`
- sha256: `9b494aa2bddb2c6afb7f745892c873deb779887d5a0aa1e9500ccdf7e2105776`
- bytes: 25606

````python
"""This module provides Serial communication data types check."""

import importlib.metadata
import logging
import sys
import unittest

import pyvisa.constants
from varname import nameof

import nipcbatt
from nipcbatt import communications


class TestSerialCommunicationParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SerialCommunicationParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_serial_communication_parameters_init_fails_when_data_rate_bauds_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationParameters(
                    data_rate_bauds=0,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value data_rate_bauds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_data_rate_bauds_is_lower_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationParameters(
                    data_rate_bauds=-7,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value data_rate_bauds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_number_of_bits_in_data_frame_is_lower_than_four(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=2,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value of number_of_bits_in_data_frame must"
            + " be greater than or equal to 4 and less than or equal to 8.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_number_of_bits_in_data_frame_is_greater_than_eight(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=10,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value of number_of_bits_in_data_frame must"
            + " be greater than or equal to 4 and less than or equal to 8.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_delay_before_receive_response_milliseconds_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=0,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value delay_before_receive_response_milliseconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_delay_before_receive_response_milliseconds_is_lower_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=-100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value delay_before_receive_response_milliseconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        # Act
        instance = communications.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )

        actual_data_rate_bauds = instance.data_rate_bauds
        actual_number_of_bits_in_data_frame = instance.number_of_bits_in_data_frame
        actual_delay_before_receive_response_milliseconds = (
            instance.delay_before_receive_response_milliseconds
        )
        actual_parity = instance.parity
        actual_stop_bits = instance.stop_bits
        actual_flow_control = instance.flow_control

        # Assert
        self.assertEqual(expected_data_rate_bauds, actual_data_rate_bauds)
        self.assertEqual(
            expected_number_of_bits_in_data_frame,
            actual_number_of_bits_in_data_frame,
        )
        self.assertEqual(
            expected_delay_before_receive_response_milliseconds,
            actual_delay_before_receive_response_milliseconds,
        )
        self.assertEqual(
            expected_parity,
            actual_parity,
        )
        self.assertEqual(
            expected_stop_bits,
            actual_stop_bits,
        )
        self.assertEqual(
            expected_flow_control,
            actual_flow_control,
        )


class TestSerialCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SerialCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_serial_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationConfiguration(
                    communication_parameters=None, command_to_send="HELO\r"
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_serial_communication_configuration_init_fails_when_command_to_send_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        communication_parameters = communications.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationConfiguration(
                    communication_parameters=communication_parameters,
                    command_to_send=None,
                )
            )

        # Assert
        self.assertEqual(
            "The string value command_to_send is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_configuration_init_fails_when_command_to_send_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        communication_parameters = communications.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationConfiguration(
                    communication_parameters=communication_parameters,
                    command_to_send="",
                )
            )

        # Assert
        self.assertEqual(
            "The string value command_to_send is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_configuration_init_fails_when_command_to_send_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        communication_parameters = communications.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SerialCommunicationConfiguration(
                    communication_parameters=communication_parameters,
                    command_to_send=" ",
                )
            )

        # Assert
        self.assertEqual(
            "The string value command_to_send is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_configuration(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff
        expected_command_to_send = "HELO\r"

        expected_communication_parameters = communications.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )

        # Act
        instance = communications.SerialCommunicationConfiguration(
            communication_parameters=expected_communication_parameters,
            command_to_send=expected_command_to_send,
        )
        actual_communication_parameters = instance.communication_parameters
        actual_command_to_send = instance.command_to_send

        # Assert
        self.assertEqual(expected_communication_parameters, actual_communication_parameters)
        self.assertEqual(
            expected_command_to_send,
            actual_command_to_send,
        )


class TestSerialCommunicationData(unittest.TestCase):
    """Defines a test fixture that checks
    `SerialCommunicationData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_serial_communication_data_init_fails_when_received_response_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(communications.SerialCommunicationData(received_response=None))

        # Assert
        self.assertEqual(
            "The string value received_response is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_data_init_fails_when_received_response_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(communications.SerialCommunicationData(received_response=""))

        # Assert
        self.assertEqual(
            "The string value received_response is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_data_init_fails_when_received_response_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(communications.SerialCommunicationData(received_response=" "))

        # Assert
        self.assertEqual(
            "The string value received_response is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_data(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_received_response = "HELO 0000 MP 300 1.11 5.27"

        # Act
        instance = communications.SerialCommunicationData(
            received_response=expected_received_response,
        )
        actual_received_response = instance.received_response

        # Assert
        self.assertEqual(expected_received_response, actual_received_response)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/__init__.py sha256=bcfc8b992cd87d807ed8de19b6f347c1758f629c0b4e12df02a582045fa2afa6 bytes=467 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/__init__.py`
- sha256: `bcfc8b992cd87d807ed8de19b6f347c1758f629c0b4e12df02a582045fa2afa6`
- bytes: 467

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.signal_voltage_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (357 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_data_types.py sha256=d5b745849e3087e2cc5d8d7f0b25f2bce808f4a4d6de2646f2ba1637f01e85d0 bytes=56808 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_data_types.py`
- sha256: `d5b745849e3087e2cc5d8d7f0b25f2bce808f4a4d6de2646f2ba1637f01e85d0`
- bytes: 56808

````python
"""This module provides Signal Voltage data types check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestToneParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'ToneParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_tone_parameters(self):
        """Tests if the instance of `ToneParameters` is created as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (189 > 100 characters) (auto-generated noqa)
        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0

        instance = daq.ToneParameters(
            tone_frequency_hertz=expected_tone_frequency,
            tone_amplitude_volts=expected_amplitude,
            tone_phase_radians=expected_phase,
        )

        actual_tone_frequency = instance.tone_frequency_hertz
        actual_amplitude = instance.tone_amplitude_volts
        actual_phase = instance.tone_phase_radians

        self.assertEqual(expected_tone_frequency, actual_tone_frequency)
        self.assertEqual(expected_amplitude, actual_amplitude)
        self.assertEqual(expected_phase, actual_phase)

    def test_tone_parameters_with_invalid_parameters(self):
        """Tests if  expected ValueError is thrown when an instance of
        `ToneParameters` is created with invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0.785

        self.assertRaises(
            ValueError,
            lambda: daq.ToneParameters(
                tone_frequency_hertz=0,
                tone_amplitude_volts=expected_amplitude,
                tone_phase_radians=expected_phase,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.ToneParameters(
                tone_frequency_hertz=expected_tone_frequency,
                tone_amplitude_volts=0,
                tone_phase_radians=expected_phase,
            ),
        )


class TestSignalVoltageGenerationTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SignalVoltageGenerationTimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=None,
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationTimingParameters(
                    sample_clock_source="",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=" ",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sampling_rate_hertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_sample_clock_source = "OnboardClock"
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=expected_sample_clock_source,
                    sampling_rate_hertz=-6,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The value sampling_rate_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_generated_signal_duration_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_sample_clock_source = "OnboardClock"
        # expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=expected_sample_clock_source,
                    sampling_rate_hertz=1000,
                    generated_signal_duration_seconds=0,
                )
            )

        self.assertEqual(
            "The value generated_signal_duration_seconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        instance = daq.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
        )

        actual_sample_clock_source = instance.sample_clock_source
        actual_sampling_rate_hertz = instance.sampling_rate_hertz
        actual_generated_signal_duration_seconds = instance.generated_signal_duration_seconds
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_generated_signal_duration_seconds,
            actual_generated_signal_duration_seconds,
        )


class TestSignalVoltageGenerationSineWaveParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'ToneParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_sine_wave_parameters(self):
        """Tests if the instance of `SignalVoltageGenerationSineWaveParameters`
        is created as expected"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)
        expected_generated_signal_offset_volts = 0.25
        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0

        expected_generated_signal_tone_parameters = daq.ToneParameters(
            tone_frequency_hertz=expected_tone_frequency,
            tone_amplitude_volts=expected_amplitude,
            tone_phase_radians=expected_phase,
        )

        instance = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=expected_generated_signal_offset_volts,
            generated_signal_tone_parameters=expected_generated_signal_tone_parameters,
        )
        actual_generated_signal_offset_volts = instance.generated_signal_offset_volts
        actual_tone_frequency = instance.generated_signal_tone_parameters.tone_frequency_hertz
        actual_amplitude = instance.generated_signal_tone_parameters.tone_amplitude_volts
        actual_phase = instance.generated_signal_tone_parameters.tone_phase_radians

        self.assertEqual(expected_amplitude, actual_amplitude)
        self.assertEqual(expected_tone_frequency, actual_tone_frequency)
        self.assertEqual(expected_phase, actual_phase)
        self.assertEqual(
            expected_generated_signal_offset_volts, actual_generated_signal_offset_volts
        )

    def test_signal_voltage_generation_sine_wave_parameters_init_fails_when_tone_parameters_is_none(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSineWaveParameters` is created with signal_tone_parameters is none.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationSineWaveParameters(
                    generated_signal_offset_volts=0.0,
                    generated_signal_tone_parameters=None,
                )
            )
        self.assertEqual("The object generated_signal_tone_parameters is None.", str(ctx.exception))


class TestSignalVoltageGenerationSquareWaveParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'SignalVoltageGenerationSquareWaveParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self._expected_generated_signal_offset_volts = 0.1
        self._expected_generated_signal_frequency_hertz = 50
        self._expected_generated_signal_amplitude_volts = 0.5
        self._expected_generated_signal_duty_cycle_percent = 50.0
        self._expected_generated_signal_phase_radians = 0.2

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_square_wave_parameters(self):
        """Tests if the instance of `SignalVoltageGenerationSquareWaveParameters`
        is created as expected"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        instance = daq.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
            generated_signal_frequency_hertz=self._expected_generated_signal_frequency_hertz,
            generated_signal_amplitude_volts=self._expected_generated_signal_amplitude_volts,
            generated_signal_duty_cycle_percent=self._expected_generated_signal_duty_cycle_percent,
            generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
        )
        actual_generated_signal_offset_volts = instance.generated_signal_offset_volts
        actual_generated_signal_frequency_hertz = instance.generated_signal_frequency_hertz
        actual_generated_signal_amplitude_volts = instance.generated_signal_amplitude_volts
        actual_generated_signal_duty_cycle_percent = instance.generated_signal_duty_cycle_percent
        actual_generated_signal_phase_radians = instance.generated_signal_phase_radians
        self.assertEqual(
            self._expected_generated_signal_offset_volts,
            actual_generated_signal_offset_volts,
        )
        self.assertEqual(
            self._expected_generated_signal_frequency_hertz,
            actual_generated_signal_frequency_hertz,
        )
        self.assertEqual(
            self._expected_generated_signal_amplitude_volts,
            actual_generated_signal_amplitude_volts,
        )
        self.assertEqual(
            self._expected_generated_signal_duty_cycle_percent,
            actual_generated_signal_duty_cycle_percent,
        )
        self.assertEqual(
            self._expected_generated_signal_phase_radians,
            actual_generated_signal_phase_radians,
        )

    def test_signal_voltage_generation_square_wave_parameters_init_fails_when_signal_frequency_is_less_than_zero(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created with signal frequency is set to 0.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=0.0,
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    generated_signal_duty_cycle_percent=(
                        self._expected_generated_signal_duty_cycle_percent
                    ),
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value generated_signal_frequency_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_square_wave_parameters_init_fails_when_signal_amplitude_is_less_than_zero(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created with signal amplitude is set to 0.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=(
                        self._expected_generated_signal_frequency_hertz
                    ),
                    generated_signal_amplitude_volts=0.0,
                    generated_signal_duty_cycle_percent=(
                        self._expected_generated_signal_duty_cycle_percent
                    ),
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value generated_signal_amplitude_volts must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_square_wave_parameters_init_fails_when_duty_cycle_is_not_within_limits(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created
        with duty_cycle value not within 0 and 100.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=(
                        self._expected_generated_signal_frequency_hertz
                    ),
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    generated_signal_duty_cycle_percent=102.0,
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value of generated_signal_duty_cycle_percent must be greater than 0 and less than 100.",
            str(ctx.exception),
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=(
                        self._expected_generated_signal_frequency_hertz
                    ),
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    generated_signal_duty_cycle_percent=0.0,
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value of generated_signal_duty_cycle_percent must be greater than 0 and less than 100.",
            str(ctx.exception),
        )


class TestSignalVoltageGenerationMultipleTonesWaveParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'SignalVoltageGenerationMultipleTonesWaveParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self._expected_generated_signal_offset_volts = 0.05
        self._expected_generated_signal_amplitude_volts = 0.75

        self._expected_multiple_tones_parameters = []

        self._expected_multiple_tones_parameters.append(
            daq.ToneParameters(
                tone_frequency_hertz=100,
                tone_amplitude_volts=0.5,
                tone_phase_radians=0.2,
            )
        )

        self._expected_multiple_tones_parameters.append(
            daq.ToneParameters(
                tone_frequency_hertz=200,
                tone_amplitude_volts=1.0,
                tone_phase_radians=0,
            )
        )

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_multiple_tones_wave_parameters(self):
        """Tests if the instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
        is created as expected"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        instance = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
            generated_signal_amplitude_volts=self._expected_generated_signal_amplitude_volts,
            generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
            multiple_tones_parameters=self._expected_multiple_tones_parameters,
        )
        actual_generated_signal_offset_volts = instance.generated_signal_offset_volts
        actual_generated_signal_amplitude_volts = instance.generated_signal_amplitude_volts

        actual_multiple_tones_parameters = instance.multiple_tones_parameters

        self.assertEqual(
            self._expected_generated_signal_amplitude_volts,
            actual_generated_signal_amplitude_volts,
        )

        self.assertEqual(
            self._expected_generated_signal_offset_volts,
            actual_generated_signal_offset_volts,
        )
        self.assertCountEqual(
            self._expected_multiple_tones_parameters, actual_multiple_tones_parameters
        )
        self.assertEqual(self._expected_multiple_tones_parameters, actual_multiple_tones_parameters)

    def test_signal_voltage_generation_multiple_tones_wave_parameters_with_signal_amplitude_zero(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created
        with signal_amplitude is set to 0.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationMultipleTonesWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_amplitude_volts=0.0,
                    multiple_tones_parameters=self._expected_multiple_tones_parameters,
                )
            )

        self.assertEqual(
            "The value generated_signal_amplitude_volts must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_multiple_tones_wave_parameters_with_tones_parameter_is_none(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created with
        multiple_tones_parameters is set to None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationMultipleTonesWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    multiple_tones_parameters=None,
                )
            )

        self.assertEqual("The object multiple_tones_parameters is None.", str(ctx.exception))

    def test_signal_voltage_generation_multiple_tones_wave_parameters_with_tones_parameter_is_empty(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created with
        multiple_tones_parameters is set to empty list.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.SignalVoltageGenerationMultipleTonesWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    multiple_tones_parameters=[],
                )
            )

        self.assertEqual(
            "The iterable multiple_tones_parameters of type list is empty.",
            str(ctx.exception),
        )


class TestSignalVoltageGenerationSineWaveConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    'ToneParametersSignalVoltageGenerationSineWaveConfiguration' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_sine_wave_configuration(self):
        """Tests if the instance of `SignalVoltageGenerationSineWaveConfiguration`
        is created as expected"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.01

        expected_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for voltage generation range parameters.
        expected_range_min_volts = -1.0
        expected_range_max_volts = 1.0

        expected_voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        # Create test values for Sine wave signal parameters

        expected_generated_signal_offset_volts = 0.25
        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0

        expected_generated_signal_tone_parameters = daq.ToneParameters(
            tone_frequency_hertz=expected_tone_frequency,
            tone_amplitude_volts=expected_amplitude,
            tone_phase_radians=expected_phase,
        )

        expected_waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=expected_generated_signal_offset_volts,
            generated_signal_tone_parameters=expected_generated_signal_tone_parameters,
        )

        instance = daq.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
            waveform_parameters=expected_waveform_parameters,
            timing_parameters=expected_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        # Log the class name with the values of the instance created for
        # SignalVoltageGenerationSineWaveConfiguration
        logging.debug(
            "%s = %s",
            nameof(daq.SignalVoltageGenerationSineWaveConfiguration),
            instance,
        )

        self.assertEqual(
            expected_voltage_generation_range_parameters,
            instance.voltage_generation_range_parameters,
        )
        self.assertEqual(expected_waveform_parameters, instance.waveform_parameters)
        self.assertEqual(
            expected_timing_parameters,
            instance.timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            instance.digital_start_trigger_parameters,
        )

    def test_signal_voltage_generation_sine_wave_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (208 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=None,
                waveform_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=None,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
                timing_parameters=None,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=None,
            ),
        )


class TestSignalVoltageGenerationSquareWaveConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    'SignalVoltageGenerationSquareWaveConfiguration' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_square_wave_configuration(self):
        """Tests if the instance of `SignalVoltageGenerationSquareWaveConfiguration`
        is created as expected"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)
        # Create test values for signal voltage generation square wave parameters.
        expected_generated_signal_duration_seconds = 0.01
        expected_generated_signal_offset_volts = 0.1
        expected_generated_signal_frequency_hertz = 50
        expected_generated_signal_amplitude_volts = 0.5
        expected_generated_signal_duty_cycle_percent = 50.0
        expected_generated_signal_phase_radians = 0.2

        expected_square_wave_generation_parameters = (
            daq.SignalVoltageGenerationSquareWaveParameters(
                generated_signal_offset_volts=expected_generated_signal_offset_volts,
                generated_signal_frequency_hertz=expected_generated_signal_frequency_hertz,
                generated_signal_amplitude_volts=expected_generated_signal_amplitude_volts,
                generated_signal_duty_cycle_percent=expected_generated_signal_duty_cycle_percent,
                generated_signal_phase_radians=expected_generated_signal_phase_radians,
            )
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000

        expected_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for voltage generation range parameters.
        expected_range_min_volts = -1.0
        expected_range_max_volts = 1.0

        expected_voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        square_wave_configuration = daq.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
            waveform_parameters=expected_square_wave_generation_parameters,
            timing_parameters=expected_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        self.assertEqual(
            expected_voltage_generation_range_parameters,
            square_wave_configuration.voltage_generation_range_parameters,
        )
        self.assertEqual(
            expected_square_wave_generation_parameters,
            square_wave_configuration.waveform_parameters,
        )
        self.assertEqual(
            expected_timing_parameters,
            square_wave_configuration.timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            square_wave_configuration.digital_start_trigger_parameters,
        )

    def test_signal_voltage_generation_square_wave_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveConfiguration` is created with invalid parameters
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=None,
                waveform_parameters=(
                    daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS
                ),
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=None,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=(
                    daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS
                ),
                timing_parameters=None,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=(
                    daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS
                ),
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=None,
            ),
        )


class TestSignalVoltageGenerationMultipleTonesConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SignalVoltageGenerationMultipleTonesConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_multiple_tones_configuration(self):
        """Tests if the instance of `SignalVoltageGenerationMultipleTonesConfiguration`
        is created as expected"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)
        # Create test values for signal voltage generation multi-tone wave parameters.
        expected_generated_signal_duration_seconds = 0.20
        expected_generated_signal_offset_volts = 0.05
        expected_generated_signal_amplitude_volts = 0.75

        expected_multiple_tones_parameters = []

        expected_multiple_tones_parameters.append(
            daq.ToneParameters(
                tone_frequency_hertz=100,
                tone_amplitude_volts=0.5,
                tone_phase_radians=0.2,
            )
        )

        expected_multiple_tones_parameters.append(
            daq.ToneParameters(
                tone_frequency_hertz=200,
                tone_amplitude_volts=1.0,
                tone_phase_radians=0,
            )
        )

        expected_multi_tone_parameters = (
            daq.SignalVoltageGenerationMultipleTonesWaveParameters(
                generated_signal_amplitude_volts=expected_generated_signal_amplitude_volts,
                generated_signal_offset_volts=expected_generated_signal_offset_volts,
                multiple_tones_parameters=expected_multiple_tones_parameters,
            )
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000

        expected_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for voltage generation range parameters.
        expected_range_min_volts = -1.0
        expected_range_max_volts = 1.0

        expected_voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        multi_tone_generation_configuration = (
            daq.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
                waveform_parameters=expected_multi_tone_parameters,
                timing_parameters=expected_timing_parameters,
                digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
            )
        )

        self.assertEqual(
            expected_voltage_generation_range_parameters,
            multi_tone_generation_configuration.voltage_generation_range_parameters,
        )
        self.assertEqual(
            expected_multi_tone_parameters,
            multi_tone_generation_configuration.waveform_parameters,
        )
        self.assertEqual(
            expected_timing_parameters,
            multi_tone_generation_configuration.timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            multi_tone_generation_configuration.digital_start_trigger_parameters,
        )

    def test_signal_voltage_generation_multiple_tones_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (285 > 100 characters) (auto-generated noqa)

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=None,
                waveform_parameters=daq.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=None,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=daq.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
                timing_parameters=None,
                digital_start_trigger_parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: daq.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=(
                    daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=daq.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=None,
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_generation.py sha256=d6589c3a9eec7ef953a10e988242207d811455740427f785b1421997024d0e8b bytes=4236 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_generation.py`
- sha256: `d6589c3a9eec7ef953a10e988242207d811455740427f785b1421997024d0e8b`
- bytes: 4236

````python
"""This module provides SignalVoltageGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestSignalVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks
    `SignalVoltageGeneration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_sine_wave(self):
        """Checks if class `SignalVoltageGeneration` is ready for use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (260 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.daq.SignalVoltageGeneration()
        # Test for Sine wave generation
        generation.initialize(
            channel_expression="Sim_PXIeDAQ/ao0:1"
        )
        generation.configure_and_generate_sine_waveform(
            configuration=nipcbatt.daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION,
        )
        generation.close()

    def test_signal_voltage_generation_square_wave(self):
        """Checks if class `daq.PowerSupplySourceAndMeasureData` is ready for use for square wave generation"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.daq.SignalVoltageGeneration()
        # Test for Square wave generation
        generation.initialize(
            channel_expression="Sim_PXIeDAQ/ao0:1"
        )
        generation.configure_and_generate_square_waveform(
            configuration=nipcbatt.daq.DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION,
        )
        generation.close()

    def test_signal_voltage_generation_multiple_tones_wave(self):
        """Checks if class `SignalVoltageGeneration` is ready for use
        for Multiple-tones generation"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (410 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.daq.SignalVoltageGeneration()
        # Test for multi-tone sine wave generation
        generation.initialize(
            channel_expression="Sim_PXIeDAQ/ao0:1"
        )
        generation.configure_and_generate_multiple_tones_waveform(
            configuration=nipcbatt.daq.DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION,
        )
        generation.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/__init__.py sha256=dc53d51bf3b2ad46f87b0ed5ac7b24273224591da66f68fde3979f7ccb74a018 bytes=459 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/__init__.py`
- sha256: `dc53d51bf3b2ad46f87b0ed5ac7b24273224591da66f68fde3979f7ccb74a018`
- bytes: 459

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.spi_communications package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_data_types.py sha256=5cb14db77dd184cc838e085604269ae2fddb3cf0dff7586f094f55f0f161af1b bytes=7351 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_data_types.py`
- sha256: `5cb14db77dd184cc838e085604269ae2fddb3cf0dff7586f094f55f0f161af1b`
- bytes: 7351

````python
"""This module provides SPI data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import communications


class TestSpiDeviceParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiDeviceParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_device_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiDeviceParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_voltage_level = nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_25

        instance = communications.SpiDeviceParameters(
            voltage_level=expected_voltage_level,
        )

        actual_voltage_level = instance.voltage_level
        self.assertEqual(
            expected_voltage_level,
            actual_voltage_level,
        )


class TestSpiCommunicationParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiCommunicationParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_communication_parameters_init_fails_when_clock_rate_kilohertz_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_chip_select = 50
        expected_clock_rate_kilohertz = 0

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiCommunicationParameters(
                    chip_select=expected_chip_select,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
                    clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_communication_parameters_init_fails_when_clock_rate_kilohertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_chip_select = 50
        expected_clock_rate_kilohertz = -100

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiCommunicationParameters(
                    chip_select=expected_chip_select,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
                    clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_communication_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_chip_select = 50
        expected_clock_rate_kilohertz = 100
        expected_clock_phase = nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE
        expected_clock_polarity = nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW

        instance = communications.SpiCommunicationParameters(
            chip_select=expected_chip_select,
            clock_rate_kilohertz=expected_clock_rate_kilohertz,
            clock_phase=expected_clock_phase,
            clock_polarity=expected_clock_polarity,
        )

        actual_chip_select = instance.chip_select
        actual_clock_rate_kilohertz = instance.clock_rate_kilohertz
        actual_clock_phase = instance.clock_phase
        actual_clock_polarity = instance.clock_polarity

        self.assertEqual(expected_chip_select, actual_chip_select)
        self.assertEqual(
            expected_clock_rate_kilohertz,
            actual_clock_rate_kilohertz,
        )
        self.assertEqual(expected_clock_phase, actual_clock_phase)
        self.assertEqual(expected_clock_polarity, actual_clock_polarity)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_communication.py sha256=202573b2aff32c7aa030e86a7fd722492f9647dcebe87cbc4483427e0144c96c bytes=2457 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_communication.py`
- sha256: `202573b2aff32c7aa030e86a7fd722492f9647dcebe87cbc4483427e0144c96c`
- bytes: 2457

````python
"""This module provides SpiReadCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt import communications


class TestSpiReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the `SpiReadCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_spi_read_communication(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_communication.SpiReadCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.SpiReadCommunication() as communication:
            communication.initialize("USB-8452")

            configuration = communications.DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=communication)
            print(f"results = {results}")
            self.assertIsNotNone(None, results)
            self.assertIsInstance(results, communications.SpiReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_data_types.py sha256=e3ce42cfc00af24f48b2e95d55419c24753882c7ef6893d450bc6b275bc90eca bytes=18846 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_data_types.py`
- sha256: `e3ce42cfc00af24f48b2e95d55419c24753882c7ef6893d450bc6b275bc90eca`
- bytes: 18846

````python
"""This module provides SPI read communication data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt import communications


class TestSpiReadParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiReadParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_read_parameters_init_fails_when_memory_address_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = 7

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=None,
                )
            )

        self.assertEqual(
            "The object memory_address_parameters is None.",
            str(ctx.exception),
        )

    def test_spi_read_parameters_init_fails_when_number_of_bytes_to_read_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = 0
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=expected_memory_address_parameters,
                )
            )

        self.assertEqual(
            "The value number_of_bytes_to_read must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_read_parameters_init_fails_when_number_of_bytes_to_read_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = -7
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=expected_memory_address_parameters,
                )
            )

        self.assertEqual(
            "The value number_of_bytes_to_read must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_read_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_to_read = 7
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        instance = communications.SpiReadParameters(
            number_of_bytes_to_read=expected_number_of_bytes_to_read,
            memory_address_parameters=expected_memory_address_parameters,
        )

        actual_number_of_bytes_to_read = instance.number_of_bytes_to_read
        actual_memory_address_parameters = instance.memory_address_parameters

        self.assertEqual(expected_number_of_bytes_to_read, actual_number_of_bytes_to_read)
        self.assertEqual(
            expected_memory_address_parameters,
            actual_memory_address_parameters,
        )


class TestSpiReadCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiReadCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_read_communication_configuration_init_fails_when_device_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_communication_parameters = communications.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )
        expected_communication_read_parameters = communications.SpiReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadCommunicationConfiguration(
                    device_parameters=None,
                    communication_parameters=expected_communication_parameters,
                    read_parameters=expected_communication_read_parameters,
                )
            )

        # Assert
        self.assertEqual("The object device_parameters is None.", str(ctx.exception))

    def test_spi_read_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_device_parameters = communications.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_read_parameters = communications.SpiReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadCommunicationConfiguration(
                    device_parameters=expected_device_parameters,
                    communication_parameters=None,
                    read_parameters=expected_communication_read_parameters,
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_spi_read_communication_configuration_init_fails_when_read_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_device_parameters = communications.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_parameters = communications.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadCommunicationConfiguration(
                    device_parameters=expected_device_parameters,
                    communication_parameters=expected_communication_parameters,
                    read_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object read_parameters is None.", str(ctx.exception))

    def test_spi_read_communication_configuration(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_parameters = communications.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_parameters = communications.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )
        expected_communication_read_parameters = communications.SpiReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        instance = communications.SpiReadCommunicationConfiguration(
            device_parameters=expected_device_parameters,
            communication_parameters=expected_communication_parameters,
            read_parameters=expected_communication_read_parameters,
        )

        actual_device_parameters = instance.device_parameters
        actual_communication_parameters = instance.communication_parameters
        actual_communication_read_parameters = instance.read_parameters

        self.assertEqual(expected_device_parameters, actual_device_parameters)
        self.assertEqual(
            expected_communication_parameters,
            actual_communication_parameters,
        )
        self.assertEqual(
            expected_communication_read_parameters, actual_communication_read_parameters
        )


class TestSpiReadCommunicationData(unittest.TestCase):
    """Defines a test fixture that checks
    `TestSpiReadCommunicationData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_read_communication_data_init_fails_when_data_bytes_read_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadCommunicationData(
                    data_bytes_read=None,
                )
            )

        self.assertEqual(
            "The object data_bytes_read is None.",
            str(ctx.exception),
        )

    def test_spi_read_communication_data_init_fails_when_data_bytes_read_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiReadCommunicationData(
                    data_bytes_read=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable data_bytes_read of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_spi_read_communication_data(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_data_bytes_read_count = 30
        expected_data_bytes_read_list = list(
            random.randint(0, 255) for i in range(0, expected_data_bytes_read_count)
        )
        expected_data_bytes_read = numpy.array(expected_data_bytes_read_list, dtype=numpy.ubyte)

        instance = communications.SpiReadCommunicationData(data_bytes_read=expected_data_bytes_read)

        actual_data_bytes_read = instance.data_bytes_read

        self.assertTrue(numpy.array_equal(a1=expected_data_bytes_read, a2=actual_data_bytes_read))


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_communication.py sha256=f566ceb44dcb0caca2d722eef1e8ccff97548157361552bd79249bbffc7b3066 bytes=3693 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_communication.py`
- sha256: `f566ceb44dcb0caca2d722eef1e8ccff97548157361552bd79249bbffc7b3066`
- bytes: 3693

````python
"""This module provides SpiWriteCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt import communications


class TestSpiWriteCommunication(unittest.TestCase):
    """Defines a test fixture that checks the `SpiWriteCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_spi_write_communication(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_communication.SpiWriteCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.SpiWriteCommunication() as communication:
            communication.initialize("USB-8452")

            write_parameters = communications.SpiWriteParameters(
                number_of_bytes_per_page=1,
                delay_between_page_write_operations_milliseconds=500,
                data_to_be_written=numpy.array(
                    [
                        175,
                        166,
                        174,
                        175,
                        129,
                        207,
                        174,
                        175,
                        1,
                        129,
                        32,
                        129,
                        96,
                        129,
                        96,
                        129,
                        207,
                        174,
                    ]
                ),
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = communications.SpiWriteCommunicationConfiguration(
                device_parameters=communications.DEFAULT_SPI_DEVICE_PARAMETERS,
                communication_parameters=communications.DEFAULT_SPI_COMMUNICATION_PARAMETERS,
                write_parameters=write_parameters,
            )

            print(f"parameters = {configuration}")
            communication.configure_and_write_data(configuration=configuration)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_data_types.py sha256=c3cc59e8ec4aff5637f616466709c33d4658f725bea16079cf5b867e982f95f1 bytes=21317 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_data_types.py`
- sha256: `c3cc59e8ec4aff5637f616466709c33d4658f725bea16079cf5b867e982f95f1`
- bytes: 21317

````python
"""This module provides SPI write communication data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt import communications


class TestSpiWriteParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiWriteParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_write_parameters_init_fails_when_memory_address_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.zeros(shape=10),
                    memory_address_parameters=None,
                )
            )

        self.assertEqual(
            "The object memory_address_parameters is None.",
            str(ctx.exception),
        )

    def test_spi_write_parameters_init_fails_when_data_to_be_written_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=None,
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The object data_to_be_written is None.",
            str(ctx.exception),
        )

    def test_spi_write_parameters_init_fails_when_data_to_be_written_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The iterable data_to_be_written of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_spi_write_parameters_init_fails_when_number_of_bytes_per_page_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteParameters(
                    number_of_bytes_per_page=-128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value number_of_bytes_per_page must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_write_parameters_init_fails_when_number_of_bytes_per_page_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteParameters(
                    number_of_bytes_per_page=0,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value number_of_bytes_per_page must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_write_parameters_init_fails_when_delay_between_page_write_operations_milliseconds_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=-10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value delay_between_page_write_operations_milliseconds must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_spi_write_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_number_of_bytes_per_page = 128
        expected_delay_between_page_write_operations_milliseconds = 10
        expected_data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        expected_data_to_be_written = numpy.array(
            expected_data_to_be_written_list, dtype=numpy.ubyte
        )
        expected_memory_address_parameters = nipcbatt.communications.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        instance = communications.SpiWriteParameters(
            number_of_bytes_per_page=expected_number_of_bytes_per_page,
            delay_between_page_write_operations_milliseconds=(
                expected_delay_between_page_write_operations_milliseconds
            ),
            data_to_be_written=expected_data_to_be_written,
            memory_address_parameters=expected_memory_address_parameters,
        )

        actual_number_of_bytes_per_page = instance.number_of_bytes_per_page
        actual_delay_between_page_write_operations_milliseconds = (
            instance.delay_between_page_write_operations_milliseconds
        )
        actual_data_to_be_written = instance.data_to_be_written
        actual_memory_address_parameters = instance.memory_address_parameters

        self.assertEqual(expected_number_of_bytes_per_page, actual_number_of_bytes_per_page)
        self.assertEqual(
            expected_delay_between_page_write_operations_milliseconds,
            actual_delay_between_page_write_operations_milliseconds,
        )
        self.assertTrue(
            numpy.array_equal(a1=expected_data_to_be_written, a2=actual_data_to_be_written)
        )
        self.assertEqual(
            expected_memory_address_parameters,
            actual_memory_address_parameters,
        )


class TestSpiWriteCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiWriteCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_spi_write_communication_configuration_init_fails_when_device_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        communication_parameters = communications.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )

        communication_write_parameters = communications.SpiWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteCommunicationConfiguration(
                    device_parameters=None,
                    communication_parameters=communication_parameters,
                    write_parameters=communication_write_parameters,
                )
            )

        # Assert
        self.assertEqual("The object device_parameters is None.", str(ctx.exception))

    def test_spi_write_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        device_parameters = communications.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        communication_write_parameters = communications.SpiWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteCommunicationConfiguration(
                    device_parameters=device_parameters,
                    communication_parameters=None,
                    write_parameters=communication_write_parameters,
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_spi_write_communication_configuration_init_fails_when_write_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        device_parameters = communications.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        communication_parameters = communications.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                communications.SpiWriteCommunicationConfiguration(
                    device_parameters=device_parameters,
                    communication_parameters=communication_parameters,
                    write_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object write_parameters is None.", str(ctx.exception))

    def test_spi_write_communication_configuration(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        expected_device_parameters = communications.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        expected_communication_parameters = communications.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )

        expected_communication_write_parameters = communications.SpiWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.communications.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        instance = communications.SpiWriteCommunicationConfiguration(
            device_parameters=expected_device_parameters,
            communication_parameters=expected_communication_parameters,
            write_parameters=expected_communication_write_parameters,
        )

        # Assert
        actual_device_parameters = instance.device_parameters
        actual_communication_parameters = instance.communication_parameters
        actual_communication_write_parameters = instance.write_parameters

        self.assertEqual(expected_device_parameters, actual_device_parameters)
        self.assertEqual(
            expected_communication_parameters,
            actual_communication_parameters,
        )
        self.assertEqual(
            expected_communication_write_parameters,
            actual_communication_write_parameters,
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/test_static_digital_path_data_types.py sha256=f6411942e06a5c8180ebfa5f9a10fc090e569a4eed670b96bea30c329949849d bytes=10485 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/test_static_digital_path_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/test_static_digital_path_data_types.py`
- sha256: `f6411942e06a5c8180ebfa5f9a10fc090e569a4eed670b96bea30c329949849d`
- bytes: 10485

````python
"""This module provides static digital path data types check."""

import importlib.metadata
import logging
import random
import string
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.switch.static_digital_path_generations.static_digital_path_data_types import (
    StaticDigitalPathGenerationPathStatus,
    StaticDigitalPathGenerationChannelParameters,
    StaticDigitalPathGenerationModuleCharacteristics,
    StaticDigitalPathGenerationStateParameters,
    StaticDigitalPathGenerationTerminalAndStateSettings,
    StaticDigitalPathGenerationTimingParameters
)

class TestStaticDigitalPathGenerationData(unittest.TestCase):
    """Defines a test fixture that ensures the class 
       'StaticDigitalStateGenerationData' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass 

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    
    def test_static_digital_path_generation_channel_parameters(self):
        """Test the creation of a StaticDigitalStateGenerationData object"""
        channel_one = 'chan1'
        channel_two = 'chan2'

        instance = StaticDigitalPathGenerationChannelParameters(channel_one, channel_two)
        
        self.assertTrue(instance.channel_one == channel_one)
        self.assertTrue(instance.channel_two == channel_two)

    def test_static_digital_generation_channel_parameters_with_invalid_data(self):
        """Tests the creation of StaticDigitalStateGenerationData object with
            invalid data. The value errors should be caught."""
        
        channel_one = 'chan1'
        channel_two = 'chan2'
        
        #Test if a value error is thrown when channel_one is None
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters(None, channel_two)
        )

        #Test if a value error is thrown when channel_one is an empty string
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters('', channel_two)
        )

        #Test if a value error is thrown when channel_two is None
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters(channel_one, None)
        )

        #Test if a value erro is thrown when channel_two is empty 
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters(channel_one, "")
        )

    def test_static_digital_path_generation_status_with_valid_data(self):
        """Tests the generation static digital path status with valid data"""

        path_status = True 
        instance = StaticDigitalPathGenerationPathStatus(path_status)
        self.assertTrue(instance.path_status == path_status)

    def test_static_digital_path_generation_status_false_is_valid(self):
        """False should also be accepted as a valid status (non-float, non-None)."""

        path_status = False
        instance = StaticDigitalPathGenerationPathStatus(path_status)
        self.assertIs(instance.path_status, False)

    def test_static_digital_path_generation_status_with_invalid_data(self):
        """Tests the generation static digital path status with invalid data
            throws a ValueError as expected"""

        #Tests if a path is None and will throw an error if so
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationPathStatus(None)
        )

        #Tests if a path is a float and will throw an error if so
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationPathStatus(1.1)
        )
        
    def test_static_digital_path_generation_timing_parameters_with_valid_data(self):
        """Tests if a StaticDigitalTimingParameters object correctly 
        instantiates when given valid data"""

        max_wait = 100

        parameters = StaticDigitalPathGenerationTimingParameters(max_wait)

        self.assertTrue(parameters.max_debounce_wait == max_wait)

    
    def test_static_digital_generation_channel_parameters_with_whitespace(self):
        """Whitespace-only channel names should be rejected."""
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters("   ", "chan2"),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters("chan1", " \t "),
        )


    def test_static_digital_path_generation_state_parameters_valid_true_false(self):
        """Both True and False should be accepted."""
        p_true = StaticDigitalPathGenerationStateParameters(True)
        p_false = StaticDigitalPathGenerationStateParameters(False)

        self.assertTrue(p_true.connect is True)
        self.assertTrue(p_false.connect is False)

    def test_static_digital_path_generation_state_parameters_invalid(self):
        """Invalid types should be rejected."""
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationStateParameters(None)
        )
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationStateParameters(1.0)
        )


    def test_static_digital_path_generation_timing_parameters_zero_and_positive(self):
        """Zero and positive max_debounce_wait are valid."""
        p0 = 0
        p100 = 100

        p0 = StaticDigitalPathGenerationTimingParameters(p0)
        p100 = StaticDigitalPathGenerationTimingParameters(p100)

        self.assertEqual(p0.max_debounce_wait, 0)
        self.assertEqual(p100.max_debounce_wait, 100)

    def test_static_digital_path_generation_timing_parameters_invalid_negative(self):
        """Negative values should be rejected."""
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationTimingParameters(-1)
        )
        # If Guard compares numerically, negative floats should also fail:
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationTimingParameters(-1.0)
        )

    def test_static_digital_path_generation_terminal_and_state_settings_valid(self):
        """Valid aggregation of channel + state parameters."""
        ch = StaticDigitalPathGenerationChannelParameters("c1", "c2")
        st = StaticDigitalPathGenerationStateParameters(True)
        settings = StaticDigitalPathGenerationTerminalAndStateSettings(ch, st)

        self.assertIs(settings.channel_parameters, ch)
        self.assertIs(settings.connection_state, st)
        self.assertEqual(settings.channel_parameters.channel_one, "c1")
        self.assertEqual(settings.channel_parameters.channel_two, "c2")
        self.assertIs(settings.connection_state.connect, True)

    def test_static_digital_path_generation_terminal_and_state_settings_invalid(self):
        """None for either parameter should be rejected."""
        ch = StaticDigitalPathGenerationChannelParameters("c1", "c2")
        st = StaticDigitalPathGenerationStateParameters(False)

        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationTerminalAndStateSettings(None, st),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationTerminalAndStateSettings(ch, None),
        )


    def test_static_digital_path_generation_module_characteristics_valid(self):
        """Non-negative floats should be accepted; properties should return exact values."""
        mc = StaticDigitalPathGenerationModuleCharacteristics(
            max_dc_voltage=5.0,
            max_ac_voltage=10.0,
            max_switching_dc_current=0.5,
            max_switching_ac_current=0.75,
        )
        self.assertEqual(mc.max_dc_voltage, 5.0)
        self.assertEqual(mc.max_ac_voltage, 10.0)


    def test_static_digital_path_generation_module_characteristics_invalid_none(self):
        """Each field None should be rejected individually."""
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                None, 10.0, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, None, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, None, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, 0.5, None
            ),
        )

    def test_static_digital_path_generation_module_characteristics_invalid_negative(self):
        """Negative values should be rejected for each field."""
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                -1.0, 10.0, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, -1.0, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, -0.01, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, 0.5, -0.01
            ),
        )


    
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/__init__.py sha256=f7c54f6ec732bf1a38b4a295283289a21524924e762cb7fe79ac3abce15ef2e0 bytes=473 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/__init__.py`
- sha256: `f7c54f6ec732bf1a38b4a295283289a21524924e762cb7fe79ac3abce15ef2e0`
- bytes: 473

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.static_digital_state_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_data_types.py sha256=82857263fdf88e132dcae76b97ff45ab961f7c03495ea84b54c7d809cb100f83 bytes=5179 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_data_types.py`
- sha256: `82857263fdf88e132dcae76b97ff45ab961f7c03495ea84b54c7d809cb100f83`
- bytes: 5179

````python
"""This module provides state digital state data types check."""

import importlib.metadata
import logging
import random
import string
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

class TestStaticDigitalStateGenerationData(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateGenerationData' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_static_digital_state_generation_data(self):
        """Tests the creation of a StaticDigitalStateGenerationData object"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        num_channels = 20
        name_length = 9

        expected_channel_identifiers = [
            "".join(random.choice(string.ascii_letters + string.digits) for n in range(name_length))
            for item in range(num_channels)
        ]

        instance = daq.StaticDigitalStateGenerationData(
            channel_identifiers=expected_channel_identifiers
        )

        actual_channel_identifiers = instance.channel_identifiers
        self.assertTrue((expected_channel_identifiers == actual_channel_identifiers))

    def test_static_digital_state_generation_data_with_invalid_data(self):
        """Tests the creation of an instance of StaticDigitalStateGeneration
        when using invalid data. It should produce and catch the associated error.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Test if a value error is thrown when channel_identifiers is None
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateGenerationData(channel_identifiers=None),
        )

        # Test is a value error is thrown when channel_identifiers is empty
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateGenerationData(channel_identifiers=[]),
        )

    def test_static_digital_state_generation_configuration(self):
        """Tests the creation of an instance of StaticDigitalStateGeneration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
        num_states = 20

        expected_data_to_write = [random.choice([True, False]) for item in range(0, num_states)]

        # create instance with generated digital states
        instance = daq.StaticDigitalStateGenerationConfiguration(
            data_to_write=expected_data_to_write
        )

        # verify states are created correctly
        actual_data_to_write = instance.data_to_write

        self.assertTrue((expected_data_to_write == actual_data_to_write))

    def test_static_digital_state_generation_configuration_with_invalid_data(self):
        """Create an instance of DigitalStateGenerationConfiguration which is
        invalid and ensure this throws an error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # create instance with data_to_write as None
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateGenerationConfiguration(data_to_write=None),
        )

        # create instance with data_to_write empty
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateGenerationConfiguration(data_to_write=[]),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_generation.py sha256=ebb8c4b4a3679fb8f32d791c801d12d92075bcd91c6c872778033cff4a35c80a bytes=2541 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_generation.py`
- sha256: `ebb8c4b4a3679fb8f32d791c801d12d92075bcd91c6c872778033cff4a35c80a`
- bytes: 2541

````python
"""This module provides StaticDigitalStateGeneration check."""

import importlib.metadata
import logging
import random
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestStaticDigitalStateGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateGeneration' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_static_digital_state_generation(self):
        """Checks if class 'StaticDigitalStateGeneration' is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (264 > 100 characters) (auto-generated noqa)

        num_channels = 3
        test_data_to_write = [random.choice([True, False]) for item in range(num_channels)]
        test_cfg = nipcbatt.daq.StaticDigitalStateGenerationConfiguration(
            data_to_write=test_data_to_write
        )

        gen = nipcbatt.daq.StaticDigitalStateGeneration()
        gen.initialize("NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:2")
        gen.configure_and_generate(configuration=test_cfg)
        gen.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/__init__.py sha256=79eb0218ff1f96a72418b5a643a7fb3f524f049673f359c63e212998ea5f901f bytes=474 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/__init__.py`
- sha256: `79eb0218ff1f96a72418b5a643a7fb3f524f049673f359c63e212998ea5f901f`
- bytes: 474

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.static_digital_state_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_data_types.py sha256=c0ccf3c663fecdf7fc2b839a795759a0f9193f22b2d45d08ae1d68f0fcf9d1b9 bytes=5438 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_data_types.py`
- sha256: `c0ccf3c663fecdf7fc2b839a795759a0f9193f22b2d45d08ae1d68f0fcf9d1b9`
- bytes: 5438

````python
"""This module provides Static digital state data types check."""

import importlib.metadata
import logging
import random
import string
import sys
import unittest
from typing import Dict

from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestStaticDigitalStateMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateMeasurementResultData' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_static_digital_state_measurement_result_data(self):
        """Tests the creation of a StaticDigitalStateMeasurementResultData object"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (195 > 100 characters) (auto-generated noqa)
        expected_digital_states = [random.choice([True, False]) for item in range(0, 20)]
        expected_channel_identifiers = [
            "".join(random.choice(string.ascii_letters + string.digits) for n in range(4))
            for item in range(20)
        ]

        # create channel states map to check against instance
        expected_states_per_channels: Dict[str, bool] = {}
        for i, state in enumerate(expected_digital_states):
            expected_states_per_channels[expected_channel_identifiers[i]] = state

        instance = daq.StaticDigitalStateMeasurementResultData(
            digital_states=expected_digital_states,
            channel_identifiers=expected_channel_identifiers,
        )

        actual_digital_states = instance.digital_states
        actual_channel_identifiers = instance.channel_identifiers
        actual_states_per_channels = instance.states_per_channels

        self.assertTrue((expected_digital_states == actual_digital_states))
        self.assertTrue((expected_channel_identifiers == actual_channel_identifiers))
        self.assertTrue((expected_states_per_channels == actual_states_per_channels))

    def test_static_digital_state_measurement_result_data_with_invalid_data(self):
        """Tests if expected error is thrown when creating an instance of
        'StaticDigitalStateMeasurementResultData with invalid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (439 > 100 characters) (auto-generated noqa)

        expected_digital_states = [random.choice([True, False]) for item in range(0, 20)]
        expected_channel_identifiers = [
            "".join(random.choice(string.ascii_letters + string.digits) for n in range(4))
            for item in range(20)
        ]

        # create channel states map to check against instance
        expected_channel_states: Dict[str, bool] = {}
        for i, state in enumerate(expected_digital_states):
            expected_channel_states[expected_channel_identifiers[i]] = state

        # Test if a value error is thrown when digital_states is None
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateMeasurementResultData(
                digital_states=None, channel_identifiers=expected_channel_identifiers
            ),
        )

        # Test if a value error is thrown when digital_states is empty
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateMeasurementResultData(
                digital_states=[], channel_identifiers=expected_channel_identifiers
            ),
        )

        # Test if a value error is thrown when channel_identifiers is None
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateMeasurementResultData(
                digital_states=expected_digital_states, channel_identifiers=None
            ),
        )

        # Test if a value error is thrown when channel_identifiers is empty
        self.assertRaises(
            ValueError,
            lambda: daq.StaticDigitalStateMeasurementResultData(
                digital_states=expected_digital_states, channel_identifiers=[]
            ),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_measurement.py sha256=8f2d1d6b2c1358c4b56fa99d1be925efd4fc20201c8b7a43e3e5216cad310050 bytes=2300 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_measurement.py`
- sha256: `8f2d1d6b2c1358c4b56fa99d1be925efd4fc20201c8b7a43e3e5216cad310050`
- bytes: 2300

````python
"""This module provides StaticDigitalStateMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.daq.static_digital_state_measurements.static_digital_state_measurement import (
    StaticDigitalStateMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestStaticDigitalStateMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateMeasurement' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_static_digital_state_measurement(self):
        """Checks if class 'StaticDigitalStateMeasurement' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (189 > 100 characters) (auto-generated noqa)
        meas = StaticDigitalStateMeasurement()
        meas.initialize("NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:7")
        meas.configure_and_measure()
        meas.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/__init__.py sha256=b014b6834eadefb797aa1aaebca9ff276fb8553191126cde6b6c5bf7fe931bf0 bytes=457 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/__init__.py`
- sha256: `b014b6834eadefb797aa1aaebca9ff276fb8553191126cde6b6c5bf7fe931bf0`
- bytes: 457

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.synchronizations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (347 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/test_synchronization_signal_routing.py sha256=25a4a85d7eb80b8af924c9d73d178a1fff00b94d3a9962f3f4b7169fef717b62 bytes=8575 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/test_synchronization_signal_routing.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/test_synchronization_signal_routing.py`
- sha256: `25a4a85d7eb80b8af924c9d73d178a1fff00b94d3a9962f3f4b7169fef717b62`
- bytes: 8575

````python
"""This module provides SynchronizationSignalsRouting check."""

import importlib.metadata
import logging
import sys
import unittest

from nidaqmx.constants import AcquisitionType

from varname import nameof
from nipcbatt import daq


class TestSynchronizationSignalRouting(unittest.TestCase):
    """Defines a test fixture that checks
    `SynchronizationSignalRouting` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        #_replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_none(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = daq.SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(terminal_name=None)

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_empty(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = daq.SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(terminal_name="")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_whitespace(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = daq.SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(terminal_name=" ")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_sample_clock_signal_to_terminal(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)
        # Arrange
        with daq.SynchronizationSignalRouting() as synchronization_signal_routing:
            synchronization_signal_routing.task.ai_channels.add_ai_voltage_chan(
                "Sim_PXIeDAQ/ai0"
            )

            synchronization_signal_routing.task.timing.cfg_samp_clk_timing(
                rate=10_000.0,
                sample_mode=AcquisitionType.CONTINUOUS,
                samps_per_chan=1000,
            )

            # Act
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(
                terminal_name="/Sim_PXIeDAQ/PFI0"
            )
            # Assert

    def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_none(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (270 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = daq.SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(
                terminal_name=None
            )

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_empty(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (270 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = daq.SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(terminal_name="")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_whitespace(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)
        synchronization_signal_routing = daq.SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(terminal_name=" ")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_start_trigger_signal_to_terminal(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)
        # Arrange
        with daq.SynchronizationSignalRouting() as synchronization_signal_routing:
            synchronization_signal_routing.task.ai_channels.add_ai_voltage_chan(
                "Sim_PXIeDAQ/ai0"
            )

            synchronization_signal_routing.task.timing.cfg_samp_clk_timing(
                rate=10_000.0,
                sample_mode=AcquisitionType.CONTINUOUS,
                samps_per_chan=1000,
            )
            
            # Assert


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/__init__.py sha256=980c3e15ffacf69ff76d770e7133ffd88e71991333e61e0f123b6f5d62607714 bytes=465 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/__init__.py`
- sha256: `980c3e15ffacf69ff76d770e7133ffd88e71991333e61e0f123b6f5d62607714`
- bytes: 465

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.temperature_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)
````
