import stream as st
import time

class EEGO_Connection():
    def __init__(self) -> None:
        self.factory = st.eego_sdk.factory()
        
        v = self.factory.getVersion()
        print('version: {}.{}.{}.{}'.format(v.major, v.minor, v.micro, v.build))
        
        print("Delaying to allow slower device to attach to computer")
        time.sleep(1)
        
        self.amplifiers = self.factory.getAmplifiers()
        self.cascaded = {}
        for amplifier in self.amplifiers:
            try:
                st.test_amplifier(amplifier)

                if amplifier.getType() not in self.self.cascaded:
                    self.cascaded[amplifier.getType()] = []
                self.cascaded[amplifier.getType()].append(amplifier)
            except Exception as e:
                print('amplifier({}) error: {}'.format(st.amplifier_to_id(amplifier), e))
                
        for key in self.cascaded:
            n = len(self.cascaded[key])
            print('cascaded({}) has {} amplifiers: {}'.format(key, n, ', '
                                                              .join(st.amplifier_to_id(a) for a in self.cascaded[key])))
            try:
                if n > 1 and hasattr(self.factory, "createCascadedAmplifier"):
                    st.test_cascaded(self.cascaded[key])
            except Exception as e:
                print("cascading({}) error: {}".format(key, e))

    def open_stream(self, time_to_read):
        """
        Opens the stream to the ant neuro box, for receiving data. time_to_read=seconds
        """
        # self.amplifiers[0]: index for chosen amplifier
        st.test_eeg(self.amplifiers[0], time_to_read=time_to_read)
        
if __name__ == "__main__":
    con = EEGO_Connection()
    con.open_stream(2)