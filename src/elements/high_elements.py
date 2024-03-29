from .dfm_patterns import *
from .efm_patterns import *
from .dpelements import DPElement
from .utils import crc16


class VBID(DPElement):
    def __init__(self, start, end, data):
        super(VBID, self).__init__(start, end)
        self.__data = data

    def __str__(self):
        return f"VBID:\n" \
               f"   VerticalBlanking_Flag: {bool(self.__data >> 0 & 0x1)}\n" \
               f"   FieldID_Flag:          {bool(self.__data >> 1 & 0x1)}\n" \
               f"   Interlace_Flag:        {bool(self.__data >> 2 & 0x1)}\n" \
               f"   NoVideoStream_Flag:    {bool(self.__data >> 3 & 0x1)}\n" \
               f"   AudioMute_Flag:        {bool(self.__data >> 4 & 0x1)}\n" \
               f"   HDCP SYNC DETECT:      {bool(self.__data >> 5 & 0x1)}\n"

    def to_html(self):
        return f"""<div>{self.__str__()}</div>"""


class VideoFrame(DPElement):
    def __init__(self, start, end, data, width, height, bpc, color_format):
        super(VideoFrame, self).__init__(start, end)
        self.__data = data
        self.__size = (width, height)
        self.__bpc = bpc
        self.__color_format = color_format

    def __str__(self):
        return f"Frame:\n" \
               f"   Size:           {self.__size[0]}x{self.__size[1]}\n" \
               f"   BPC:            {self.__bpc}\n" \
               f"   Color Format:   {bool(self.__data >> 2 & 0x1)}\n" \
               f"   CRC:            0x{crc16(self.__data[0::3], 0xFFFE)} 0x{crc16(self.__data[1::3], 0xFFFE)} 0x{crc16(self.__data[2::3], 0xFFFE)}\n"

    def to_html(self):
        return f"""<div>{self.__str__()}</div>"""


class SDP(DPElement):
    def __init__(self, start, end, data):
        super(SDP, self).__init__(start, end)
        self.__header = data[:4]
        self.__body = data[4:]

    def __str__(self):
        return f"SDP:\n" \
               f"   Header:  {self.__header}\n" \
               f"   Body:    {self.__body}\n"

    def to_html(self):
        return f"""<div>{self.__str__()}</div>"""


class MSA(DPElement):
    def __init__(self, start, end, data):
        super(MSA, self).__init__(start, end)
        self.__data = data

    def __str__(self):
        return f"MSA:\n" \
               f"   HTotal:  {int.from_bytes(self.__data[3:5], byteorder='big')}\n" \
               f"   VTotal:  {int.from_bytes(self.__data[5:7], byteorder='big')}\n" \
               f"   HSync:   {int.from_bytes(self.__data[8:10] & 0x7F, byteorder='big') * (1 if self.__data[8] & 0x80 else -1)}\n" \
               f"   HStart:  {int.from_bytes(self.__data[14:16], byteorder='big')}\n" \
               f"   VStart:  {int.from_bytes(self.__data[16:18], byteorder='big')}\n" \
               f"   VSync:   {int.from_bytes(self.__data[18:20] & 0x7F, byteorder='big') * (1 if self.__data[18] & 0x80 else -1)}\n" \
               f"   MISC:    {hex(int.from_bytes(self.__data[0:2], byteorder='big'))}\n"

    def to_html(self):
        return f"""<div>{self.__str__()}</div>"""

