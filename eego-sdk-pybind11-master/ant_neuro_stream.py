import eego_sdk
import itertools
import time

class EEGO_Connection():
    def __init__(self) -> None:
        self.factory = eego_sdk.factory()
        self.amplifiers = self.factory.getAmplifiers()
        for amplifier in amplifiers:
            try:
                test_amplifier(amplifier)

                # add to cascaded dictionary
                if amplifier.getType() not in cascaded:
                    cascaded[amplifier.getType()]=[]
                    cascaded[amplifier.getType()].append(amplifier)
            except Exception as e:
                print('amplifier({}) error: {}'.format(amplifier_to_id(amplifier), e))

    def check_connection(self):
        """
        Checks if an ant neuro box is connected and prints its data
        """
        print('{}-{:06d}-{}'.format(amplifier.getType(), amplifier.getFirmwareVersion(), amplifier.getSerialNumber()))

    def open_stream(self):
        """
        Opens the stream to the ant neuro box, for receiving data
        """