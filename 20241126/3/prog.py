import struct
import sys 
data = sys.stdin.buffer.read(44)
if len(data)< 44: print('NO')
else: 
    riff, size, wave, fmt, fmt_size, audio_format, channels, rate, _, _, bits, data, data_size = struct.unpack('<4sI4s4sIHHIIHH4sI', data)    
    if riff != b'RIFF' or wave != b'WAVE' or fmt != b'fmt ' or data != b'data': print('NO')   
    else:
        print(
                f"Size={size}, "
                f"Type={audio_format}, "
                f"Channels={channels}, "
                f"Rate={rate}, "
                f"Bits={bits}, "
                f"Data size={data_size}"
            )